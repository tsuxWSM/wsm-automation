from .base_page import BaseShopPage
from .locators.product_search_results import ProductSearchResultsLocators
from ....utils.ui.web_element import VisualWebElement


class ProductSearchResultsPage(BaseShopPage):

    def __init__(self, driver):
        super().__init__(driver)

        self.sort_dropdown = VisualWebElement(driver, ProductSearchResultsLocators.SORT_DROPDOWN)
        self.results_view_dropdown = VisualWebElement(driver, ProductSearchResultsLocators.RESULTS_VIEW_DROPDOWN)
        self.result_item_detals_button = \
            VisualWebElement(driver, ProductSearchResultsLocators.RESULT_ITEM_DETALS_BUTTON)
        self.results_pagination_label = VisualWebElement(driver, ProductSearchResultsLocators.RESULTS_PAGINATION_LABEL)
