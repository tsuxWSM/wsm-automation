from selenium.webdriver.common.by import By


class ForgotPassword:
    """Page Object for Forgot Password page locators"""

    # Dashboard menu
    MENU_DASHBOARD = (By.CSS_SELECTOR, "a[title='My Dashboard']")
    SUBMENU_DASHBOARD = (By.CSS_SELECTOR, "#MenuBar1 a[title='WSM News']")
    SUBMENU_TECH_LICENSE = (By.CSS_SELECTOR, "#MenuBar1 a[title='Tech License']")

    # Forgot Email form
    EMAIL_INPUT = (By.CSS_SELECTOR, "input#login")
    NEXT_BUTTON = (By.CSS_SELECTOR, "input[value='Next']")
    RETURN_LINK = (By.CSS_SELECTOR, "a[title='Return']")
    TOP_LINK = (By.CSS_SELECTOR, "a[title='Jump to Top']")
    TITLE_HEADER = (By.CSS_SELECTOR, ".wsma_content_wrapper > h1")
    EMAIL_LABEL = (By.CSS_SELECTOR, "label[for='login']")
