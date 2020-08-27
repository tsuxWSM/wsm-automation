from selenium.webdriver.common.by import By


class HomeLocators:
    """A class for Web Shop's Home page locators"""

    VEHICLE_SEARCH_PANEL_TITLE = (By.CSS_SELECTOR, "section.home-ymm h2")
    POPULAR_CATEGORIES_TITLE = (By.CSS_SELECTOR, "section.home-tp h2")

    NOTIFICATION_MESSAGE = (By.CSS_SELECTOR, "li.wsm_message")
