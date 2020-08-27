from selenium.webdriver.remote.webdriver import WebDriver
from .base_page import SearchPanelSection
from ..checkout_page import CheckoutPage


class ExtremeMetalProductsCheckoutPage(SearchPanelSection, CheckoutPage):
    """A page object for Shop's Checkout Page"""

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        super().__init__(driver, self.get_site_from_url())
