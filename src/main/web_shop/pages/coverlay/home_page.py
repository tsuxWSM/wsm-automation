from selenium.webdriver.remote.webdriver import WebDriver
from .base_page import TopPanelSection
from .locators.home import HomeLocators
from ....utils.ui.web_element import VisualWebElement


class HomePage(TopPanelSection):
    """A Page Object for Shop's Home Page"""

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

        self.vehicle_search_panel = VisualWebElement(driver, HomeLocators.VEHICLE_SEARCH_PANEL_TITLE)
        # self.popular_categories = VisualWebElement(driver, HomeLocators.POPULAR_CATEGORIES_TITLE)

    def get_notification_message_element(self):
        return VisualWebElement(self.driver, HomeLocators.NOTIFICATION_MESSAGE)
