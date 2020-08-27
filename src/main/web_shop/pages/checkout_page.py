from selenium.webdriver.remote.webdriver import WebDriver
from .locators.checkout import CheckoutLocators
from ...utils.ui.base_page import GlobalBasePage
from ...utils.ui.web_element import VisualWebElement


class CheckoutPage(GlobalBasePage):
    """A page object for Shop's Checkout Page"""

    def __init__(self, driver: WebDriver, invoice_only: bool = False, signed_user: bool = False):
        super().__init__(driver)

        if not signed_user:
            self.account_section_title = VisualWebElement(driver, CheckoutLocators.ACCOUNT_SECTION_TITLE)
            self.checkout_as_guest_radio = VisualWebElement(driver, CheckoutLocators.CHECKOUT_AS_GUEST_RADIO)
            self.email_input = VisualWebElement(driver, CheckoutLocators.EMAIL_INPUT)
            self.subscribe_checkbox = VisualWebElement(driver, CheckoutLocators.SUBSCRIBE_CHECKBOX)

            self.create_new_account_radio = VisualWebElement(driver, CheckoutLocators.CREATE_NEW_ACCOUNT_RADIO)
            self.register_email_input = VisualWebElement(driver, CheckoutLocators.REGISTER_EMAIL_INPUT)
            self.first_name_input = VisualWebElement(driver, CheckoutLocators.FIRST_NAME_INPUT)
            self.last_name_input = VisualWebElement(driver, CheckoutLocators.LAST_NAME_INPUT)
            self.password_input = VisualWebElement(driver, CheckoutLocators.PASSWORD_INPUT)
            self.confirm_password_input = VisualWebElement(driver, CheckoutLocators.CONFIRM_PASSWORD_INPUT)
            self.guest_subscribe_checkbox = VisualWebElement(driver, CheckoutLocators.GUEST_SUBSCRIBE_CHECKBOX)
            self.register_new_account_input = VisualWebElement(driver, CheckoutLocators.REGISTER_NEW_ACCOUNT_INPUT)

            self.log_into_your_account_radio = VisualWebElement(driver, CheckoutLocators.LOG_INTO_YOUR_ACCOUNT_RADIO)
            self.log_email_input = VisualWebElement(driver, CheckoutLocators.LOG_EMAIL_INPUT)
            self.log_password_input = VisualWebElement(driver, CheckoutLocators.LOG_PASSWORD_INPUT)
            self.forgot_password_link = VisualWebElement(driver, CheckoutLocators.FORGOT_PASSWORD_LINK)
            self.login_input = VisualWebElement(driver, CheckoutLocators.LOGIN_INPUT)

        # Address Information
        self.address_information_title = VisualWebElement(driver, CheckoutLocators.ADDRESS_INFORMATION_TITLE)
        self.separate_shipping_address_checkbox = \
            VisualWebElement(driver, CheckoutLocators.SEPARATE_SHIPPING_ADDRESS_CHECKBOX)

        self.billing_and_shipping_address_title = \
            VisualWebElement(driver,CheckoutLocators.BILLING_AND_SHIPPING_ADDRESS_TITLE)
        self.company_input = VisualWebElement(driver, CheckoutLocators.COMPANY_INPUT)
        self.first_name_address_input = VisualWebElement(driver, CheckoutLocators.FIRST_NAME_ADDRESS_INPUT)
        self.last_name_address_input = VisualWebElement(driver, CheckoutLocators.LAST_NAME_ADDRESS_INPUT)
        # self.country_dropdown = VisualWebElement(driver, CheckoutLocators.COUNTRY_DROPDOWN)
        self.street_input = VisualWebElement(driver, CheckoutLocators.STREET_INPUT)
        self.suite_no_input = VisualWebElement(driver, CheckoutLocators.SUITE_NO_INPUT)
        self.city_input = VisualWebElement(driver, CheckoutLocators.CITY_INPUT)

        # Payment Information
        self.payment_information_title = VisualWebElement(driver, CheckoutLocators.PAYMENT_INFORMATION_TITLE)

        if not invoice_only:
            self.card_radio = VisualWebElement(driver, CheckoutLocators.CARD_RADIO)
            self.card_number_input = VisualWebElement(driver, CheckoutLocators.CARD_NUMBER_INPUT)
            self.name_on_card_input = VisualWebElement(driver, CheckoutLocators.NAME_ON_CARD_INPUT)
            self.cvv_input = VisualWebElement(driver, CheckoutLocators.CVV_INPUT)
            self.where_is_this_link = VisualWebElement(driver, CheckoutLocators.WHERE_IS_THIS_LINK)

            self.order_checkout_title = VisualWebElement(driver, CheckoutLocators.ORDER_CHECKOUT_TITLE)
            self.order_comments_input = VisualWebElement(driver, CheckoutLocators.ORDER_COMMENTS_INPUT)
            self.submit_order_button = VisualWebElement(driver, CheckoutLocators.SUBMIT_ORDER_BUTTON)
        else:
            self.checkout_label = VisualWebElement(driver, CheckoutLocators.CHECKOUT_LABEL)
            self.checkout_info = VisualWebElement(driver, CheckoutLocators.CHECKOUT_INFO)
            self.checkout_pm_logo = VisualWebElement(driver, CheckoutLocators.CHECKOUT_PM_LOGO)

            self.vehicle_verification = VisualWebElement(driver, CheckoutLocators.VEHICLE_VERIFICATION_FIELD)
            self.special_instructions = VisualWebElement(driver, CheckoutLocators.SPECIAL_INSTRUCTIONS_FIELD)
