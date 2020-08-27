from selenium.webdriver.common.by import By


class SearchPanel:
    """A class for Admin's common Search Panel"""

    SEARCH_INPUT = (By.CSS_SELECTOR, "#pager_search_query")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "input.search_btn")
    ADVANCED_BUTTON = (By.CSS_SELECTOR, "form button.search_btn")
