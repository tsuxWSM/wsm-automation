from .base_page import BaseAdminPage
from .locators.forgot_password import ForgotPassword
from ...utils.ui.web_element import BaseWebElement
from ...utils.ui.web_element import VisualWebElement


class ForgotPasswordAdminPage(BaseAdminPage):
    """A Page Object for Admin's Forgot Password Admin Page"""

    def __init__(self, driver):
        super().__init__(driver)

        self.dashboard_menu = VisualWebElement(driver, ForgotPassword.MENU_DASHBOARD)
        self.dashboard_submenu = BaseWebElement(driver, ForgotPassword.SUBMENU_DASHBOARD)
        self.tech_license_submenu = BaseWebElement(driver, ForgotPassword.SUBMENU_TECH_LICENSE)

        self.email_input = VisualWebElement(driver, ForgotPassword.EMAIL_INPUT)
        self.next_button = VisualWebElement(driver, ForgotPassword.NEXT_BUTTON)
        self.return_link = VisualWebElement(driver, ForgotPassword.RETURN_LINK)
        self.top_link = VisualWebElement(driver, ForgotPassword.TOP_LINK)

        self.title_header = VisualWebElement(driver, ForgotPassword.TITLE_HEADER)
        self.email_label = VisualWebElement(driver, ForgotPassword.EMAIL_LABEL)
