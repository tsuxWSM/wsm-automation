from .base_page import AdminTopPanel
from .locators.add_quote import AddQuoteLocators
from ...data_model.product import Product
from ...utils.ui.web_element import BaseWebElement, VisualWebElement, DropdownWebElement, GenericWebElement
from ...utils.data_handlers import DateTimeHandler
from enum import Enum


class OrdersSubmenus(Enum):
    ALL_ORDERS = "All Orders"
    OPEN = "Open"
    NEW = "New"
    PENDING = "Pending"
    PROCESSING = "Processing"
    READY_TO_SHIP = "Ready To Ship"
    RETURN = "Return"
    SHIPPED = "Shipped"
    BACKORDER = "Backorder"
    HELD = "Held"
    COMPLETE = "Complete"
    CANCELED = "Canceled"
    FRAUD = "Fraud"
    DELETED = "Deleted"
    ADD_ORDER = "Add Order"
    QUOTE_BUILDER_BETA = "Quote Builder (Beta)"
    ADD_QUOTE_BETA = "Add Quote (Beta)"


class ShippingMethods(Enum):
    FEDEX_SMART_POST_ECONOMY_SHIPPING = "FedEx SmartPost/Economy Shipping"
    FREE_SHIPPING = "Free Shipping"
    INTERNATIONAL_SHIPPING = "International Shipping"
    BASIC_SHIPPING = "Basic Shipping"
    FEDEX_1DAY_FREIGHT = "FedEx 1Day® Freight"
    FEDEX_2DAY_AIR = "FedEx 2Day (2-Day Air)"
    FEDEX_2DAY_FREIGHT = "FedEx 2Day® Freight"
    FEDEX_3DAY_FREIGHT = "FedEx 3Day® Freight"
    FEDEX_EXPRESS_SAVER = "FedEx Express Saver (3-Day Air)"
    FEDEX_FIRST_OVERNIGHT = "FedEx First Overnight®"
    SHIPPING_MATRIX = "Shipping Matrix"  # Has a Detail (There are more than one or at least the text)


class PaymentType(Enum):
    AUTHNET = "authnet"
    CHECK = "check"
    INVOICE = "invoice"


class ItemStatus(Enum):
    NEW = "new"
    BACK_ORDER = "backorder"
    SHIPPED = "shipped"
    CANCELED = "canceled"
    RETURNED = "returned"


class InformationDialog(Enum):
    TOTAL_AMOUNT_DUE = "This is the total amount due on the order after debits and credits are applied.  " \
                       "Pending, canceled, and voided transactions do not apply to this."
    ADDITIONAL_COMMENT = "You may enter additional order comments for the customer here.  " \
                         "A new comment is only sent to the customer when the order is updated."
    CALCULATE_TAX = "To calculate sales tax, click the calculator icon to the right, " \
                    "enter the tax rate to use, and click the \"calculate\" button."
    PROMOTION_CODE = "A single promotion code may be attached to the quote. The code will"


class Item:

    def __init__(self, name: str):
        self.name = name
        self.status = ItemStatus.NEW
        self.quantity = 1
        self.unit_price = 0.00
        self.total_price = 0.00


class AddQuotePage(AdminTopPanel):
    """A Page Object For Admin's Add Quote Page"""

    def __init__(self, driver, is_existing_quote=False):
        """Initialize Add Quote Page. Click """
        super().__init__(driver)
        self.is_existing_quote = is_existing_quote
        self.items_count = 0

        # Customer Information Section
        self.customer_information_title = VisualWebElement(driver, AddQuoteLocators.CUSTOMER_INFORMATION_TITLE)
        self.email_address_input = VisualWebElement(driver, AddQuoteLocators.EMAIL_ADDRESS_INPUT)
        self.account_number_input = VisualWebElement(driver, AddQuoteLocators.ACCOUNT_NUMBER_INPUT)
        self.quote_status_dropdown = VisualWebElement(driver, AddQuoteLocators.QUOTE_STATUS_DROPDOWN)
        self.memo_input = VisualWebElement(driver, AddQuoteLocators.MEMO_INPUT)
        self.expires_input = VisualWebElement(driver, AddQuoteLocators.EXPIRES_INPUT)
        self.calendar_img = VisualWebElement(driver, AddQuoteLocators.CALENDAR_ICON)

        # Quote status on Edit and validity check for page setup
        if is_existing_quote:
            self.page_title = VisualWebElement(driver, AddQuoteLocators.EDIT_QUOTE_TITLE)
            expiration_date = self.expires_input.get_attribute_value("value")
            if not DateTimeHandler.is_past_date(expiration_date):
                self.enable_quote_actions()
            else:
                self.copy_link = None
                self.load_to_cart_link = None
                self.print_quote_icon = None
        else:
            self.page_title = VisualWebElement(driver, AddQuoteLocators.ADD_QUOTE_TITLE)
            self.customer_input = VisualWebElement(driver, AddQuoteLocators.CUSTOMER_INPUT)

        # Address Information Section
        self.address_information_title = VisualWebElement(driver, AddQuoteLocators.ADDRESS_INFORMATION_TITLE)
        self.billing_address_link = VisualWebElement(driver, AddQuoteLocators.BILLING_ADDRESS_LINK)
        self.shipping_address_link = VisualWebElement(driver, AddQuoteLocators.SHIPPING_ADDRESS_LINK)
        self.shipping_method_dropdown = DropdownWebElement(driver, AddQuoteLocators.SHIPPING_METHOD_DROPDOWN)
        self.help_icon_total_amount_due = VisualWebElement(driver, AddQuoteLocators.HELP_ICON_TOTAL_AMOUNT_DUE)
        self.total_amount_due = VisualWebElement(driver, AddQuoteLocators.TOTAL_AMOUNT_DUE)

        # Payment Information Section
        self.billing_address_t = VisualWebElement(driver, AddQuoteLocators.BILLING_ADDRESS_TITLE)
        self.order_payment_dropdown = VisualWebElement(driver, AddQuoteLocators.ORDER_PAYMENT_DROPDOWN)
        self.add_payment_button = VisualWebElement(driver, AddQuoteLocators.ADD_PAYMENT_BUTTON)

        # Quote Information Section
        self.quote_information_title = VisualWebElement(driver, AddQuoteLocators.QUOTE_INFORMATION_TITLE)
        self.__add_custom_item_button = VisualWebElement(driver, AddQuoteLocators.ADD_CUSTOM_ITEM_BUTTON)
        self.__add_item_button = VisualWebElement(driver, AddQuoteLocators.ADD_ITEM_BUTTON)
        self.remove_item_icon = VisualWebElement(driver, AddQuoteLocators.REMOVE_ITEM_ICONS)

        # Discounts Section
        self.discounts_title = VisualWebElement(driver, AddQuoteLocators.DISCOUNTS_TITLE)
        self.use_markdowns_button = VisualWebElement(driver, AddQuoteLocators.USE_MARKDOWNS_BUTTON)

        self.use_promotion_button = VisualWebElement(driver, AddQuoteLocators.USE_PROMOTION_BUTTON)
        self.subtotal_span = VisualWebElement(driver, AddQuoteLocators.SUBTOTAL)
        self.shipping_input = VisualWebElement(driver, AddQuoteLocators.SHIPPING_INPUT)
        self.handling_input = VisualWebElement(driver, AddQuoteLocators.HANDLING_INPUT)
        self.sales_tax_input = VisualWebElement(driver, AddQuoteLocators.SALES_TAX_INPUT)
        self.discounts_span = VisualWebElement(driver, AddQuoteLocators.DISCOUNTS)
        self.grand_total = VisualWebElement(driver, AddQuoteLocators.GRAND_TOTAL)
        self.help_popup_icon_img = VisualWebElement(driver, AddQuoteLocators.HELP_ICON_CALCULATOR)
        self.tax_open_calculator_a = VisualWebElement(driver, AddQuoteLocators.TAX_OPEN_CALCULATOR_LINK)

        self.tax_rate_input = BaseWebElement(driver, AddQuoteLocators.TAX_RATE_INPUT)
        self.tax_shipping_input = BaseWebElement(driver, AddQuoteLocators.TAX_SHIPPING_INPUT)
        self.before_promotions_input = BaseWebElement(driver, AddQuoteLocators.BEFORE_PROMOTIONS_INPUT)
        self.calculate_button = BaseWebElement(driver, AddQuoteLocators.CALCULATE_BUTTON)

        # User Comments Section
        self.user_comments_title = VisualWebElement(driver, AddQuoteLocators.COMMENTS_TITLE)
        self.help_popup_icon_img_ulti = VisualWebElement(driver, AddQuoteLocators.HELP_ICON_COMMENTS)
        self.form_comment_testarea = VisualWebElement(driver, AddQuoteLocators.FORM_COMMENT_TEXTAREA)
        self.send_email_bcc_input = VisualWebElement(driver, AddQuoteLocators.SEND_EMAIL_BCC_INPUT)
        self.create_quote_button = VisualWebElement(driver, AddQuoteLocators.CREATE_QUOTE_BUTTON)

    def get_quote_number_from_title(self):
        return self.page_title.get_text().split("#")[1]

    def select_shipping_method_option_by_text(self, shipping_method: ShippingMethods):
        """Selects a Shipping Method in Dropdown
        :param shipping_method: Shipping Method to be selected"""
        var_template = "$SHIPPING_METHOD$"

        self.shipping_method_dropdown.select_option(AddQuoteLocators.GENERIC_SHIPPING_OPTION,
                                                    var_template,
                                                    shipping_method)

    def fill_item_title(self, item_name: str, position=0):
        """Fill Item title field based on position in list
        :param item_name: name to be placed as custom title for virtual products or entry search for regular products
        :param position: position in Item fields list"""
        self.update_item_input(item_name, AddQuoteLocators.GENERIC_ITEM_NAME_INPUT, position)

    def fill_item_sku(self, sku: int, position=0):
        """Fill Item sku field based on position in list
        :param sku: custom sku to be place for item
        :param position: position in Item fields list"""
        self.update_item_input(str(sku), AddQuoteLocators.SKU_INPUT, position)

    def set_item_price(self, price: float, position=0):
        """Fill Item price field based on position in list
        :param price: custom price to be set
        :param position: position in Item fields list"""
        price_element = self.get_item_input_by_position(AddQuoteLocators.UNIT_PRICE_INPUT, position)
        price_element.manually_clear()
        price_element.__set__(str(price))

    def get_item_input_by_position(self, locator: tuple, position: int):
        template = "$ITEM$"
        input_field = VisualWebElement(self.driver, (locator[0], locator[1].replace(template, str(position))))
        input_field.click()
        return input_field

    def select_result_item_by_position(self, position: int = 1):
        """Select a result item from a product search
        :param position: item position in result list, first result item by default [position=1]"""
        template = "$RESULT$"
        result_item = GenericWebElement(self.driver,
                                        AddQuoteLocators.GENERIC_SEARCH_RESULT_ITEM,
                                        template,
                                        subs_value=str(position))
        result_item.click()

    def select_result_item_by_name(self, input_string, position=0):
        self.fill_item_title(input_string, position)
        self.get_item_search_first_result().simulate_click()

    def search_item(self, product: Product):
        self.fill_item_title(product.title)
        self.select_result_item_by_position()

    def update_item_input(self, value: str, locator: tuple, position: int):
        if position is not 0:
            if position <= self.items_count:
                self.get_item_input_by_position(locator, position).__set__(str(value))
        else:
            self.get_item_input_by_position(locator, self.items_count).__set__(str(value))

    def get_item_search_first_result(self):
        return VisualWebElement(self.driver, AddQuoteLocators.FIRST_RESULT_ITEM)

    def add_item(self):
        self.__add_item_button.click()
        self.items_count += 1

    def add_custom_item(self):
        self.__add_custom_item_button.click()
        self.items_count += 1

    def create_quote_action(self):
        self.create_quote_button.click()
        self.is_existing_quote = True

    def enable_quote_actions(self):
        self.copy_link = VisualWebElement(self.driver, AddQuoteLocators.COPY_LINK_BUTTON)
        self.load_to_cart_link = VisualWebElement(self.driver, AddQuoteLocators.LOAD_TO_CART_LINK)
        self.print_quote_icon = VisualWebElement(self.driver, AddQuoteLocators.PRINTER_ICON)
