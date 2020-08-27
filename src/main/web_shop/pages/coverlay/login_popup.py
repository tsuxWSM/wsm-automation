from selenium.webdriver.remote.webdriver import WebDriver
from .base_page import BaseShopPage
from .locators.login_popup import LoginPopupLocators
from ....wsm_admin.test_data.customer_data_provider import Customer
from ....utils.ui.web_element import VisualWebElement


class LoginPopup(BaseShopPage):
    """A Page Object for Shop's Login Popup"""

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

        self.email_input = VisualWebElement(driver, LoginPopupLocators.EMAIL_INPUT)
        self.password_input = VisualWebElement(driver, LoginPopupLocators.PASSWORD_INPUT)
        self.login_button = VisualWebElement(driver, LoginPopupLocators.LOGIN_BUTTON)
        self.forgot_pw_link = VisualWebElement(driver, LoginPopupLocators.FORGOT_PASSWORD_LINK)
        self.close_button = VisualWebElement(driver, LoginPopupLocators.CLOSE_BUTTON)

    def customer_login(self, customer: Customer):
        self.email_input.__set__(customer.email)
        self.password_input.__set__(customer.password)

        self.login_button.click()
