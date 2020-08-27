from selenium.webdriver.common.by import By


class ProductSearchResultsLocators:
    """A class for Product Search Results Page locators"""

    # Results Filters
    SORT_DROPDOWN = (By.CSS_SELECTOR, "#filter-sort")
    RESULTS_VIEW_DROPDOWN = (By.CSS_SELECTOR, "#filter-perpage")
    RESULTS_VIEW_MODE_SWITCH = (By.CSS_SELECTOR, ".wsm-prod-switch-view")

    # Pagination Info
    RESULTS_PAGINATION_LABEL = (By.CSS_SELECTOR, ".wsm-cat-pagination-top .wsm-cat-pag-pagemin")

    RESULT_ITEM_DETALS_BUTTON = \
        (By.XPATH,
         "//a[text()='Coverlay Interior Accessories Kit']/ancestor::div[contains(@class, 'wsm-cat-list-item')]")
