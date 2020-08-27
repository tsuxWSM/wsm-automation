from selenium.webdriver.common.by import By


class SearchPanelLocators:
    """Locators for Coverlay Search Panel"""

    LOGO_LINK = (By.CSS_SELECTOR, ".wsm-hdr__logo-link")
    BAR_SEARCH_INPUT = (By.CSS_SELECTOR, "form #edit-keys")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "input[title='Search']")
    CALL_US_LINK = (By.CSS_SELECTOR, ".wsm-hdr__main a[title='call us']")
    CHAT_LINK = (By.CSS_SELECTOR, ".wsm-hdr__chat a")
