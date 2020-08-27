from selenium.webdriver.common.by import By


class SearchPanelLocators:
    """Locators for Extreme Metal Products Search Panel"""

    LOGO_LINK = (By.CSS_SELECTOR, "a[title='Extreme Metal Products Homepage'] img")
    BAR_SEARCH_INPUT = (By.CSS_SELECTOR, "#q")
    CALL_US_LINK = (By.CSS_SELECTOR, "a[title='call us']")
    DEALER_LOCATOR_LINK = (By.CSS_SELECTOR, "a[title='See Our Dealer Locator']")
