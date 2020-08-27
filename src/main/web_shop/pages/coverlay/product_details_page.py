from selenium.webdriver.remote.webdriver import WebDriver
from .base_page import TopPanelSection
from .....main.data_model.customer import Customer
from .....main.data_model.product import Product
from ....utils.ui.web_element import VisualWebElement
from .locators.product_details import ProductDetailsLocators

# TODO: Following value is just an approximation. Investigate the right min amount
_MIN_AMOUNT_FOR_AFFIRM = 250.00


class ProductDetailsPage(TopPanelSection):
    """A Page Object for Shop's Product Details Page"""

    def __init__(self, driver: WebDriver, product: Product, customer: Customer = None):
        """Initializes Product details page. A product is required as entry argument
        :param driver: WebDriver instance to be used
        :param product: Product which details we expect to see populating data in page
        :param customer: (Optional) Signed in customer, if any.
        """
        super().__init__(driver)
        self.product = product
        self.customer = customer

        self.product_title = VisualWebElement(driver, ProductDetailsLocators.PRODUCT_TITLE)
        self.product_sku = VisualWebElement(driver, ProductDetailsLocators.PRODUCT_SKU)
        self.product_summary = VisualWebElement(driver, ProductDetailsLocators.PRODUCT_SUMMARY)
        self.product_rotate_link = VisualWebElement(driver, ProductDetailsLocators.PRODUCT_IMAGE_ROTATOR_LINK)
        self.price = VisualWebElement(driver, ProductDetailsLocators.PRICE)

        self.item_inquiry_link = VisualWebElement(driver, ProductDetailsLocators.ITEM_INQUIRY_LINK)
        self.tell_a_friend_link = VisualWebElement(driver, ProductDetailsLocators.TELL_A_FRIEND_LINK)

        self.quantity_input = VisualWebElement(driver, ProductDetailsLocators.QUANTITY_INPUT)
        self.add_to_cart_button = VisualWebElement(driver, ProductDetailsLocators.ADD_TO_CART_BUTTON)

        self.affirm_link = None
        self.affirm_logo = None

        product_price = float(product.price)

        if customer is not None:
            if customer.affirm_allowed and product_price > _MIN_AMOUNT_FOR_AFFIRM:
                self.set_affirm_links(driver)
        elif product_price > _MIN_AMOUNT_FOR_AFFIRM:
            # For when there is no User logged in
            self.set_affirm_links(driver)

    def set_affirm_links(self, driver: WebDriver):
        self.affirm_link = VisualWebElement(driver, ProductDetailsLocators.AFFIRM_LINK)
        self.affirm_logo = VisualWebElement(driver, ProductDetailsLocators.AFFIRM_LOGO)
