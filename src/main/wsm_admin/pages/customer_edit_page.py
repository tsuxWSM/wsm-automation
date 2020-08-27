from .base_page import AdminTopPanel
from .locators.customer_edit import CustomerEdit
from ...utils.ui.web_element import VisualWebElement
from ..test_data.customer_data_provider import Customer


class CustomerEditPage(AdminTopPanel):
    """A Page Object for Admin's Customer Edit Page"""

    def __init__(self, driver):
        super().__init__(driver)

        self.active_user_true = VisualWebElement(driver, CustomerEdit.ACTIVE_USER_TRUE)
        self.active_user_false = VisualWebElement(driver, CustomerEdit.ACTIVE_USER_FALSE)

        self.email_input = VisualWebElement(driver, CustomerEdit.EMAIL_INPUT)
        self.password_input = VisualWebElement(driver, CustomerEdit.PASSWORD_INPUT)
        self.alt_id_input = VisualWebElement(driver, CustomerEdit.ALTERNATE_ID_INPUT)
        self.account_number_input = VisualWebElement(driver, CustomerEdit.ACCOUNT_NUMBER_INPUT)
        self.user_name_input = VisualWebElement(driver, CustomerEdit.NAME_INPUT)
        self.user_last_name_input = VisualWebElement(driver, CustomerEdit.LAST_NAME_INPUT)
        self.company_input = VisualWebElement(driver, CustomerEdit.COMPANY_INPUT)
        self.birth_date_input = VisualWebElement(driver, CustomerEdit.BIRTH_DATE_INPUT)
        self.account_status_drodown = VisualWebElement(driver, CustomerEdit.ACCOUNT_STATUS_DROPDOWN)

        # Radio button setup
        self.tax_exempt_true = VisualWebElement(driver, CustomerEdit.TAX_EXEMPT_TRUE)
        self.tax_exempt_false = VisualWebElement(driver, CustomerEdit.TAX_EXEMPT_FALSE)

        self.invoice_true = VisualWebElement(driver, CustomerEdit.INVOICE_TRUE)
        self.invoice_false = VisualWebElement(driver, CustomerEdit.INVOICE_FALSE)

        # Affirm radio buttons
        self.affirm_true = VisualWebElement(driver, CustomerEdit.AFFIRM_ALLOWED_TRUE)
        self.affirm_false = VisualWebElement(driver, CustomerEdit.AFFIRM_ALLOWED_FALSE)

        self.block_free_shipping_true = VisualWebElement(driver, CustomerEdit.BLOCK_FREE_SHIPPING_TRUE)
        self.block_free_shipping_false = VisualWebElement(driver, CustomerEdit.BLOCK_FREE_SHIPPING_FALSE)

        self.price_group_dropdown = VisualWebElement(driver, CustomerEdit.PRICE_GROUP_DROPDOWN)

        self.price_group_dropdown = VisualWebElement(driver, CustomerEdit.PRICE_GROUP_DROPDOWN)

        # Access group visual section
        self.sales_group = VisualWebElement(driver, CustomerEdit.SALES_GROUP_CHECKBOX)
        self.select_all_button = VisualWebElement(driver, CustomerEdit.SELECT_ALL_BUTTON)
        self.clear_all_button = VisualWebElement(driver, CustomerEdit.CLEAR_ALL_BUTTON)

        # Main Action Buttons
        self.save_button, self.delete_button = self.get_main_action_buttons()

    def get_main_action_buttons(self):
        """Checks if we land into Edit or Add page and returns Main Action button(s) accordingly"""
        if 'customer.edit' in self.driver.current_url:
            return VisualWebElement(self.driver, CustomerEdit.SAVE_CUSTOMER_BUTTON), \
                VisualWebElement(self.driver, CustomerEdit.DELETE_BUTTON)
        else:
            return VisualWebElement(self.driver, CustomerEdit.ADD_CUSTOMER_BUTTON), None

    def create_new_user(self, customer: Customer):
        self.email_input.__set__(customer.email)
        self.password_input.__set__(customer.password)

        self.account_number_input.__set__(customer.account_number)
        self.user_name_input.__set__(customer.name)
        self.user_last_name_input.__set__(customer.last_name)
        self.birth_date_input.__set__(customer.birth_date)

        if not customer.active:
            self.active_user_false.click()
        if not customer.affirm_allowed:
            self.affirm_false.click()
        if customer.tax_exempt:
            self.tax_exempt_true.click()
        if customer.invoice_only:
            self.invoice_true.click()
        if customer.block_free_shipping:
            self.block_free_shipping_true.click()

        self.save_button.click()
