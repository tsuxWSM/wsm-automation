from .base_page import BaseAdminPage
from .locators.sign_in import SignInLocators
from ...utils.ui.web_element import VisualWebElement


class SignInAdminPage(BaseAdminPage):
    """A Page Object for Admin's Sign In Page"""

    def __init__(self, driver):
        super().__init__(driver)

        self.login_title = VisualWebElement(driver, SignInLocators.LOGIN_TITLE)
        self.user_name_input = VisualWebElement(driver, SignInLocators.USER_NAME_INPUT)
        self.password_input = VisualWebElement(driver, SignInLocators.PASSWORD_INPUT)
        self.auto_login_checkbox = VisualWebElement(driver, SignInLocators.AUTO_LOGIN_CHECKBOX)
        self.forgot_pw_link = VisualWebElement(driver, SignInLocators.FORGOT_PW_LINK)
        self.login_button = VisualWebElement(driver, SignInLocators.LOGIN_BUTTON)

    def sign_in(self, user_name: str, password: str):
        self.user_name_input.__set__(user_name)
        self.password_input.__set__(password)

        self.login_button.click()

    def get_error_message_element(self):
        return VisualWebElement(self.driver, SignInLocators.CRED_ERROR_MESSAGE)

    def get_notification_message_element(self):
        return VisualWebElement(self.driver, SignInLocators.NOTIFICATION_MESSAGE)
