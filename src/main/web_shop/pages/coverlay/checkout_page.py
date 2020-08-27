from selenium.webdriver.remote.webdriver import WebDriver
from ..checkout_page import CheckoutPage
from .base_page import SearchPanelSection


class CoverlayCheckoutPage(CheckoutPage, SearchPanelSection):
    """A page object for Shop's Checkout Page"""

    def __init__(self, driver: WebDriver, invoice_only=False, signed_user=False):
        super().__init__(driver, invoice_only=invoice_only, signed_user=signed_user)
