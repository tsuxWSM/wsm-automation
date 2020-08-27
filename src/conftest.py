import os
import shutil
import pytest
from typing import Dict, Tuple
from _pytest.main import Session
from _pytest.python_api import RaisesContext
from selenium.webdriver.remote.webdriver import WebDriver
from .main.utils import setup_conf as setup

# store history of failures per test class name and per index in parametrize (if parametrize used)
_test_failed_incremental: Dict[str, Dict[Tuple[int, ...], str]] = {}

# Session global variables for configuration purposes
_driver: WebDriver
_browser: str
_url: str
_suite_name: str = ""


def pytest_addoption(parser):
    """Additional configurations based on customized argument options at command execution"""
    parser.addoption("--url",
                     action="store",
                     default="SDC",
                     # TODO: Investigate the command to get usage help on added options
                     help="Sets base url to be used as test target. Available base urls: "
                          "\n SDC -> https://wsmsdc.webshopmanager.com"
                          "\n HHP -> https://highwayandheavyparts.com"
                          "\n EMP -> https://extrememetalproducts.com"
                          "\n KTP -> https://ktperformance.net"
                          "\n CVL -> https://coverlaymfg.com"
                          "\n PSU -> https://pitstopusa.com"
                          "\n RVR -> https://rivaracing.com"
                          "\n EIB -> https://eibach.com")

    parser.addoption("--brw",
                     action="store",
                     default="CHR",
                     help="Sets a browser for UI Testing. Available browsers: "
                          "\n CHR -> For chrome browser"
                          "\n FFX -> For firefox browser")
    parser.addoption("--prx",
                     action="store",
                     default="NO-PROXY",
                     help="Sets a Proxy for UI Testing through Dev Env. Available Dev Proxies: ")


@pytest.fixture(name="webdriver", scope="class")
def webdriver(request):
    """Set ups a WebDriver instance and global test vars based on run configurations for every test class"""
    from selenium.webdriver.support.ui import WebDriverWait

    global _driver, _url

    request.cls.base_url = setup.set_url(request.config.getoption("--url"), request)
    request.cls.site = request.config.getoption("--url")
    request.cls.browser_options = \
        setup.setup_proxy(request.config.getoption("--prx"), request.config.getoption("--brw"))
    request.cls.driver = setup.set_browser(request.config.getoption("--brw"), request.cls.browser_options)
    _url = request.cls.base_url
    _driver = request.cls.driver

    request.cls.driver.maximize_window()
    request.cls.driver.implicitly_wait(10)
    request.cls.driver.get(request.cls.base_url)

    request.cls.wait = WebDriverWait(request.cls.driver, 15)

    request.addfinalizer(request.cls.driver.quit)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call: RaisesContext):
    """Report maker. Added here:
        1. Save Screenshot of the
        2. Handler conf for incremental [test execution] mark
    """
    html_report = item.config.pluginmanager.getplugin('html')

    # execute all other hooks to obtain the report object
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == "call":
        if report.failed:
            os.mkdir("test_results/screenshots")
            print("\nFailed Test>>> " + item.name)
            try:
                _driver.save_screenshot("test_results/screenshots/Test_" + item.name + "Snapshot.png")
                print("Saved Screenshot at test_results/screenshots")
                extra.append(html_report.extras.html("<div id='%s-failed'><p><strong>%s</strong></p></div>"
                                                     % (item.name, _suite_name)
                                                     )
                             )
            except IOError:
                print("Error saving screenshot !!")

    if "incremental" in item.keywords:
        # incremental marker is used
        if call.excinfo is not None:
            # the test has failed, retrieve the class name of the test
            cls_name = str(item.cls)
            # retrieve the index of the test (if parametrize is used in combination with incremental)
            parametrize_index = (
                tuple(item.callspec.indices.values())
                if hasattr(item, "callspec")
                else ()
            )
            # retrieve the name of the test function
            test_name = item.originalname or item.name
            # store in _test_failed_incremental the original name of the failed test
            _test_failed_incremental.setdefault(cls_name, {}).setdefault(parametrize_index, test_name)

    report.extra = extra


def pytest_html_report_title(report):
    report.title = _suite_name + " Test Results"


def pytest_runtest_setup(item):
    """Handles incremental keyword for plugin"""
    global _suite_name

    cls_name = str(item.cls)

    if not _suite_name and "Admin" not in _suite_name:
        _suite_name = setup.prettify_suite_name(cls_name)

    if "prestep" in item.keywords:
        print(">> INFO: Running test suite pre-steps")

    if "incremental" in item.keywords:
        # retrieve the class name of the test

        # check if a previous test has failed for this class
        if cls_name in _test_failed_incremental:
            # retrieve the index of the test (if parametrize is used in combination with incremental)
            parametrize_index = (
                tuple(item.callspec.indices.values())
                if hasattr(item, "callspec")
                else ()
            )
            # retrieve the name of the first test function to fail for this class name and index
            test_name = _test_failed_incremental[cls_name].get(parametrize_index, None)
            # if name found, test has failed for the combination of class name & test name
            if test_name is not None and "teardown_suite" not in item.name:
                pytest.skip("previous test failed ({})".format(test_name))


def pytest_runtestloop(session: Session):
    """Initializes Test Session"""
    print("Session: " + session.name)

    if setup.is_dir_in_path("test_results"):
        shutil.rmtree("test_results")
    os.mkdir("test_results")
