from selenium.webdriver.remote.webdriver import WebDriver
from ....data_model.quote import Quote
from ..cart_page import CartPage
from .base_page import TopPanelSection


class CoverlayCartPage(CartPage, TopPanelSection):

    def __init__(self, driver: WebDriver, product_list=None, quote: Quote = None,
                 user_lands_from_admin: bool = False):
        super().__init__(driver, product_list, quote, user_lands_from_admin)

        if self.is_cart_empty:
            assert self.is_text_present("Your cart is currently empty."), "Expected 'Empty Cart' message not Visible"
            return
