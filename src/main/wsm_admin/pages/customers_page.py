from selenium.webdriver.remote.webdriver import WebDriver
from .base_page import SearchBar
from .locators.customers import Customers
from ...utils.ui.web_element import VisualWebElement


class CustomersPage(SearchBar):
    """A Page Object for Admin's Customers Page"""

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

        self.add_customer_button_top = VisualWebElement(driver, Customers.TOP_ADD_CUSTOMER_BUTTON)
        self.export_button_top = VisualWebElement(driver, Customers.TOP_EXPORT_BUTTON)

        self.edit_icon = VisualWebElement(driver, Customers.EDIT_ICON)
        self.impersonate_icon = VisualWebElement(driver, Customers.IMPERSONATE_ICON)
        self.delete_icon = VisualWebElement(driver, Customers.DELETE_ICON)

        self.export_button_bottom = VisualWebElement(driver, Customers.BOTTOM_EXPORT_BUTTON)
        self.add_customer_button_bottom = VisualWebElement(driver, Customers.BOTTOM_ADD_CUSTOMER_BUTTON)

    def get_notification_message_element(self):
        """Returns the notification message element, which is only PRESENT after an action"""
        return VisualWebElement(self.driver, Customers.NOTIFICATION_MESSAGE)

    def search_customer(self, search_entry: str):
        """Search for a customer. Suggested fields to use for this search are email and name"""
        self.search_input.__set__(search_entry)
        self.search_button.click()
