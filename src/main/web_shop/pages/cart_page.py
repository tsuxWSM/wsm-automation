from selenium.webdriver.remote.webdriver import WebDriver
from ...data_model.quote import Quote
from ...utils.ui.webdriver_handler import WebDriverHandler
from .locators.cart import CartLocators
from ...utils.ui.base_page import GlobalBasePage
from ...utils.ui.web_element import GenericWebElement, VisualWebElement


class CartPage(GlobalBasePage):
    """A page object for Shop's Checkout Page"""

    def __init__(self, driver: WebDriver, product_list=None, quote: Quote = None,
                 user_lands_from_admin: bool = False):
        super().__init__(driver)
        self.is_cart_empty = False

        if product_list is None and quote is None and not self.is_partial_text_present("added to your cart!"):
            self.is_cart_empty = True

        self.cart_subtotal = VisualWebElement(driver, CartLocators.CART_SUBTOTAL)
        self.cart_total = VisualWebElement(driver, CartLocators.CART_TOTAL)

        # IMPORTANT NOTE: This logic is necessary for every page on Web Shop that a user can land from Admin Panel
        if user_lands_from_admin:
            WebDriverHandler(driver).patiently_switch_to_window(1)
            self.quote_button = GenericWebElement(driver, CartLocators.GENERIC_SAVE_QUOTE_BUTTON, "$QUOTE_NUMBER$",
                                                  subs_value=quote.quote_number)
            self.exit_quote_link = VisualWebElement(driver, CartLocators.EXIT_QUOTE_LINK)
        else:
            self.quote_button = VisualWebElement(driver, CartLocators.CREATE_QUOTE_BUTTON)

        self.proceed_to_checkout_button = VisualWebElement(driver, CartLocators.PROCEED_TO_CHECKOUT_BUTTON)
