from selenium.webdriver.common.by import By


class SignInLocators:
    """Page Object for SignIn page locators"""

    LOGIN_TITLE = (By.CSS_SELECTOR, ".wsma_login_text")
    USER_NAME_INPUT = (By.CSS_SELECTOR, "#login_login")
    PASSWORD_INPUT = (By.CSS_SELECTOR,"#login_password")
    AUTO_LOGIN_CHECKBOX = (By.CSS_SELECTOR, "#login_auto")
    FORGOT_PW_LINK = (By.XPATH, "//a[text()='forgot password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".wsma_btn")
    CRED_ERROR_MESSAGE = (By.CSS_SELECTOR, "li.wsm_error")
    NOTIFICATION_MESSAGE = (By.CSS_SELECTOR, "li.wsm_message")
