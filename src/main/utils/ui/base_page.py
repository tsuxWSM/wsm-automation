from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from .web_element import BaseWebElement


class GlobalBasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def is_text_present(self, text_entry: str) -> bool:
        """Look for specific text to be present at any element in page
        :param text_entry: Partial text expected to be present
        """
        try:
            self.driver.find_element(By.XPATH, "//*[text()='" + text_entry + "']")
            return True
        except (TimeoutException, NoSuchElementException):
            return False

    def is_partial_text_present(self, text_entry: str) -> bool:
        """Look for partial text to be present at any element in page. Use when text pattern varies based on test data
        :param text_entry: Partial text expected to be present
        """
        try:
            self.driver.find_element(By.XPATH, "//*[contains(text(), '" + text_entry + "')]")
            return True
        except (TimeoutException, NoSuchElementException):
            return False

    def get_site_from_url(self):
        url_sections = self.driver.current_url.split('.')
        return url_sections[1] if 'www' in url_sections[0] else url_sections[0]

    # TODO: Investigate on out of bounds issue while using move_to_element
    def move_to_element(self, web_element: BaseWebElement):
        """Applies hover action on a located element
        :param web_element: Web Element to hovered"""
        actions = ActionChains(self.driver)
        actions.move_to_element(web_element.element).perform()

    def switch_to_window(self, window_number):
        """Switch WebDriver to specified Window/tab
        :param window_number: The window position to be moved to"""
        self.driver.switch_to.window(self.driver.window_handles[window_number])

    def scroll_down(self):
        """Scrolls down the page"""
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight/3)")

    def scroll_up_to_element(self, element: BaseWebElement):
        """Scrolls up to specified element
        :param element: base web element """
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", element.element)
