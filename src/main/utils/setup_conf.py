import os
from .system_constants import SupportedBrowsers, Site
from .testrails import APIClient


# Dictionary of all Available base URLs that we have in place for tests targeting
_av_urls = {
    Site.SDC.value: 'https://wsmsdc.webshopmanager.com',
    Site.HHP.value: 'https://highwayandheavyparts.com',
    Site.EMP.value: 'https://extrememetalproducts.com',
    Site.KTP.value: 'https://ktperformance.net',
    Site.CVL.value: 'https://coverlaymfg.com',
    Site.PSU.value: 'https://pitstopusa.com',
    Site.RVR.value: 'https://rivaracing.com',
    Site.EIB.value: 'https://eibach.com'
}

# Dictionary of all Available Proxy configurations for each dev env av for testing purposes as a way of sandbox
_dev_env_proxies = {
    'NO-PROXY': None,
    'JS1': 'ms-dev-1.dev.wdsolutions.com:3128',
    'JS2': 'js-dev-2.dev.wdsolutions.com:3128',
    'SDC': 'js-dev-1.dev.wdsolutions.com:3128'
}


def set_browser(browser, options=None):
    """Initializes a WebDriver instance based on picked Browser, if no browser is defined, default will be Chrome"""
    from selenium.webdriver import Chrome, Firefox

    if browser == SupportedBrowsers.CHROME.value:
        driver = Chrome(executable_path='resources/drivers/chromedriver', chrome_options=options)
    elif browser == SupportedBrowsers.FIREFOX.value:
        driver = Firefox(executable_path='resources/drivers/geckodriver', firefox_options=options)
    else:
        raise Exception("Invalid Argument Error>> "
                        "Wrong Browser code provided. Use --brw-help to see available browsers")

    return driver


def set_url(url_option: str, request) -> str:
    """Gets a URL based on picked url command, if no url is defined un execution command, default will be WSMSDC"""
    if "Admin" in request.node.name:
        request.cls.test_platform = "ADMIN"
        return _av_urls[url_option] + "/admin"
    else:
        request.cls.test_platform = "WEB_SHOP"
        return _av_urls[url_option]


def setup_test_rails_plugin():
    client = APIClient('https://webshopmanager.testrail.io', "", "")


def setup_proxy(proxy_command, browser):
    """Sets Proxy for environment variable"""
    from selenium.webdriver import ChromeOptions
    from selenium.webdriver import FirefoxOptions

    if proxy_command == "NO-PROXY":
        return None
    elif proxy_command not in _dev_env_proxies.keys():
        raise Exception("Invalid Argument Error>> "
                        "Wrong Proxy code provided. Use --prx-help to see available dev environment proxies")

    try:
        if browser == SupportedBrowsers.CHROME.value:
            chrome_options = ChromeOptions()
            chrome_options.add_argument('--proxy-server=' + _dev_env_proxies[proxy_command])
            return chrome_options
        elif browser == SupportedBrowsers.FIREFOX.value:
            firefox_options = FirefoxOptions()
            firefox_options.add_argument('--proxy-server' + _dev_env_proxies[proxy_command])
            return firefox_options
    except Exception as exc:
        print(type(exc))
        print(exc.args)
        raise exc


def is_dir_in_path(directory: str, path="."):
    """Validates if a directory is already in path. Use before any os action attempt like create/delete directory
    :arg directory: Directory name
    :arg path: Relative path location where we expect to check for dir presence. Default set to current dir: '.'
    """
    return os.path.isdir(path + "/" + directory)


def prettify_item_name(name: str):
    """Prettifies Test Item Name for a more Human Readable format in report
    :arg name: Item name to be prettified"""
    return name.replace("_", " ")


def prettify_suite_name(name: str):
    """Prettifies Test Suite Name by cleaning all class symbol chars
    :arg name: Suite name to be prettified"""
    return (name.split(".")[name.split(".").__len__() - 1])[0:-2]
