from selenium.webdriver.common.by import By


class VehicleSearchPanelLocators:
    """A class for Shop'S Vehicle Search Panel locators"""

    VEHICLE_SEARCH_PANEL = (By.CSS_SELECTOR, "section.home-ymm")
    VEHICLE_SEARCH_FROM = (By.CSS_SELECTOR, "#vehicle_selector")
    YEAR_DROPDOWN = (By.CSS_SELECTOR, "#sidebar_year_select")
    MAKE_DROPDOWN = (By.CSS_SELECTOR, "#sidebar_make_select")
    MODEL_DROPDOWN = (By.CSS_SELECTOR, "#sidebar_model_select")
    VEHICLE_SEARCH_BUTTON = (By.CSS_SELECTOR, "button.wsmjs-attribute-search-shop")
    RESET_BUTTON = (By.CSS_SELECTOR, "#vehicle_selector_reset")
