from selenium.webdriver.common.by import By


class LoginPopupLocators:
    """A class for Login Popup locators"""

    EMAIL_INPUT = (By.CSS_SELECTOR, "#wsm_form_email")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#wsm_form_password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".widget_login_submit input.btn.btn-primary")
    FORGOT_PASSWORD_LINK = (By.CSS_SELECTOR, "a.widget_login_login_forgotpassword")
    CLOSE_BUTTON = (By.CSS_SELECTOR, ".modal.fade.in button.btn-default")
