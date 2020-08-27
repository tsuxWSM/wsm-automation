from .base_page import AdminTopPanel
from ...utils.ui.web_element import DropdownWebElement, VisualWebElement
from .locators.configuration import ConfigurationLocator, GeneralLocators, SiteInformationLocators
from enum import Enum


class CurrencyCodeOption(Enum):
    DOLAR = "USD"
    DOLAR_CAD = "CAD"
    PESO = "MXN"


class LanguageOption(Enum):
    ENG = "ENG"
    SPA = "SPA"


class OrderUpdateRedirect(Enum):
    STAY_ON_ORDER_PAGE = "Stay on the order page"
    REDIRECT_TO_THE_ALL_ORDERS_LIST = "Redirect to the \"All Orders\" list"
    REDIRECT_TO_THE_OPEN_ORDERS_LIST = "Redirect to the \"Open Orders\" list"


class ResultsPerPageInMyOrders(Enum):
    TEN = "10"
    TWENTY = "20"
    THIRTY = "30"
    FORTY = "40"
    FIFTY = "50"
    ONE_HUNDRED = "100"


class SubmissionLimit(Enum):
    ONE = "1"
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"
    SEVEN = "7"
    EIGHT = "8"
    NINE = "9"
    NUM_TEN = "10 (default)"
    ELEVEN = "11"
    TWELVE = "12"
    THIRTEEN = "13"
    FOURTEEN = "14"
    FIFTEEN = "15"
    SIXTEEN = "16"
    SEVENTEEN = "17"
    EIGHTEEN = "18"
    NINETEEN = "19"
    NUM_TWENTY = "20"


class WYSIWYGOptions(Enum):
    MINIMUM = "minimum"
    MEDIUM = "medium"
    MAXIMUM = "maximum"


class Configuration(AdminTopPanel):

    def __init__(self, driver):
        super().__init__(driver)

        self.configuration_title = VisualWebElement(driver, ConfigurationLocator.CONFIGURATION_TITLE)
        self.site_information_button = VisualWebElement(driver, ConfigurationLocator.SITE_INFORMATION_BUTTON)
        self.general_button = VisualWebElement(driver, ConfigurationLocator.GENERAL_BUTTON)
        self.catalog_button = VisualWebElement(driver, ConfigurationLocator.CATALOG_BUTTON)
        self.cart_button = VisualWebElement(driver, ConfigurationLocator.CART_BUTTON)
        self.checkout_button = VisualWebElement(driver, ConfigurationLocator.CHECKOUT_BUTTON)
        self.shipping_and_handling_button = VisualWebElement(driver, ConfigurationLocator.SHIPPING_AND_HANDLING_BUTTON)
        self.payment_and_precessing_button = VisualWebElement(driver,
                                                              ConfigurationLocator.PAYMENT_AND_PROCESSING_BUTTON)
        self.images_button = VisualWebElement(driver, ConfigurationLocator.IMAGES_BUTTON)
        self.integration_button = VisualWebElement(driver, ConfigurationLocator.INTEGRATION_BUTTON)
        # TODO: This tab is only present for CVL, RVR. Need to know what does this tab presence depend on
        self.ags_button = VisualWebElement(driver, ConfigurationLocator.AGS_BUTTON)
        self.dns_button = VisualWebElement(driver, ConfigurationLocator.DNS_BUTTON)
        self.advanced_button = VisualWebElement(driver, ConfigurationLocator.ADVANCED_BUTTON)
        self.admin_button = VisualWebElement(driver, ConfigurationLocator.ADMIN_BUTTON)
        self.mtl_button = VisualWebElement(driver, ConfigurationLocator.MTL_BUTTON)
        self.return_button = VisualWebElement(driver, ConfigurationLocator.RETURN_BUTTON)
        self.top_button = VisualWebElement(driver, ConfigurationLocator.TOP_BUTTON)
        self.save_changes_input = VisualWebElement(driver, ConfigurationLocator.SAVE_CHANGES_INPUT)

    def go_to_general(self):
        self.general_button.click()

        return GeneralPanel(self.driver)

    def go_to_site_information(self):
        self.site_information_button.click()

        return SiteInformationPanel(self.driver)


class SiteInformationPanel(Configuration):

    def __init__(self, driver):
        super().__init__(driver)

        self.site_information_title = VisualWebElement(driver, SiteInformationLocators.SITE_INFORMATION_TITLE)
        self.site_name_input = VisualWebElement(driver, SiteInformationLocators.SITE_NAME_INPUT)
        self.owners_name_input = VisualWebElement(driver, SiteInformationLocators.OWNERS_NAME_INPUT)
        self.company_input = VisualWebElement(driver, SiteInformationLocators.COMPANY_INPUT)
        self.address_one_input = VisualWebElement(driver, SiteInformationLocators.ADDRESS_ONE_INPUT)
        self.address_two_input = VisualWebElement(driver, SiteInformationLocators.ADDRESS_TWO_INPUT)
        self.city_input = VisualWebElement(driver, SiteInformationLocators.CITY_INPUT)

        self.currency_code_dropdown = DropdownWebElement(self.driver, SiteInformationLocators.CURRENCY_CODE_DROPDOWN)
        self.language_dropdown = DropdownWebElement(self.driver, SiteInformationLocators.LANGUAGE_DROPDOWN)

        self.country_dropdown = DropdownWebElement(driver, SiteInformationLocators.COUNTRY_DROPDOWN)
        self.state_province_dropdown = DropdownWebElement(driver, SiteInformationLocators.STATE_PROVINCE_DROPDOWN)

        self.zip_code_input = VisualWebElement(driver, SiteInformationLocators.ZIP_CODE_INPUT)
        self.toll_free_input = VisualWebElement(driver, SiteInformationLocators.TOLL_FREE_INPUT)
        self.phone_input = VisualWebElement(driver, SiteInformationLocators.PHONE_INPUT)
        self.fax_input = VisualWebElement(driver, SiteInformationLocators.FAX_INPUT)
        self.email_input = VisualWebElement(driver, SiteInformationLocators.EMAIL_INPUT)

        self.logo_url_input = VisualWebElement(driver, SiteInformationLocators.LOGO_URL_INPUT)
        # self.logo_url_img = VisualWebElement(driver, SiteInformationLocators.LOGO_URL_IMG)
        self.favorite_icon_input = VisualWebElement(driver, SiteInformationLocators.FAVORITE_ICON_INPUT)
        # self.favorite_icon_img = VisualWebElement(driver, SiteInformationLocators.FAVORITE_ICON_IMG)

    def select_currency_code_option(self, option: CurrencyCodeOption):
        template = "$OPTION$"

        self.currency_code_dropdown.select_option(SiteInformationLocators.GENERIC_CURRENCY_OPTION,
                                                  template, option)

    def select_language_option(self, option: CurrencyCodeOption):
        template = "$LANGUAGE$"

        self.language_dropdown.select_option(SiteInformationLocators.GENERIC_LANGUAGE_OPTION,
                                             template, option)


class GeneralPanel(Configuration):

    def __init__(self, driver):
        super().__init__(driver)

        self.general_title = VisualWebElement(self.driver, GeneralLocators.GENERAL_TITLE)
        self.new_articles_input = VisualWebElement(self.driver, GeneralLocators.NEWS_ARTICLES_INPUT)
        self.news_summary_characters_input = \
            VisualWebElement(self.driver, GeneralLocators.NEWS_SUMMARY_CHARACTERS_INPUT)
        self.contact_form_text_textarea = VisualWebElement(self.driver, GeneralLocators.CONTACT_FORM_TEXT_TEXTAREA)
        self.order_update_redirect_dropdown = \
            VisualWebElement(self.driver, GeneralLocators.ORDER_UPDATE_REDIRECT_DROPDOWN)

        self.customer_form_spam_settings_title = \
            VisualWebElement(self.driver, GeneralLocators.CUSTOMER_FORM_SPAM_SETTINGS_TITLE)
        self.recaptcha_site_key_input = VisualWebElement(self.driver, GeneralLocators.RECAPTCHA_SITE_KEY_INPUT)
        self.generate_recaptcha_site_key_link = \
            VisualWebElement(self.driver, GeneralLocators.GENERATE_RECAPTCHA_SITE_KEY_LINK)
        self.get_help_setting_up_recaptcha_link = \
            VisualWebElement(self.driver, GeneralLocators.GET_HELP_SETTING_UP_RECAPTCHA_LINK)
        self.recaptcha_secret_input = \
            VisualWebElement(self.driver, GeneralLocators.RECAPTCHA_SECRET_INPUT)
        self.submission_limit_interval_input = \
            VisualWebElement(self.driver, GeneralLocators.SUBMISSION_LIMIT_INTERVAL_INPUT)

        self.wysiwyg_editor_title = VisualWebElement(self.driver, GeneralLocators.WYSIWYG_EDITOR_TITLE)

        self.invoice_printing_title = VisualWebElement(self.driver, GeneralLocators.INVOICE_PRINTING_TITLE)

        self.order_update_redirect_dropdown = \
            DropdownWebElement(self.driver, GeneralLocators.ORDER_UPDATE_REDIRECT_DROPDOWN)
        self.results_per_page_in_my_orders_dropdown = \
            DropdownWebElement(self.driver, GeneralLocators.RESULTS_PER_PAGE_IN_MY_ORDERS_DROPDOWN)
        self.submission_limit_dropdown = DropdownWebElement(self.driver, GeneralLocators.SUBMISSION_LIMIT_DROPDOWN)

        # TODO: Implement Logic for Radio Buttons
        '''self.shipping_field_left_justification_dropdown = \
            DropdownWebElement(self.driver, GeneralLocators.SHIPPING_FIELD_LEFT_JUSTIFICATION_DROPDOWN)
        self.shipping_field_right_justification_dropdown = \
            DropdownWebElement(self.driver, GeneralLocators.SHIPPING_FIELD_RIGHT_JUSTIFICATION_DROPDOWN)
        self.shipping_method_left_justification_dropdown = \
            DropdownWebElement(self.driver, GeneralLocators.SHIPPING_METHOD_LEFT_JUSTIFICATION_DROPDOWN)
        self.shipping_method_right_justification_dropdown = \
            DropdownWebElement(self.driver, GeneralLocators.SHIPPING_METHOD_RIGHT_JUSTIFICATION_DROPDOWN)'''

    def select_order_update_redirect_option(self, option: OrderUpdateRedirect):
        template = "$TEXT$"

        self.order_update_redirect_dropdown.select_option(GeneralLocators.GENERIC_ORDER_UPDATE_REDIRECT_OPTION,
                                                          template, option)

    def select_results_per_page_in_my_orders_option(self, option: ResultsPerPageInMyOrders):
        template = "$VALUE$"

        self.results_per_page_in_my_orders_dropdown.select_option(GeneralLocators.GENERIC_RESULTS_PER_PAGE_OPTION,
                                                                  template, option)

    def select_submission_limit_option(self, option: SubmissionLimit):
        template = "$LIMIT$"

        self.submission_limit_dropdown.select_option(GeneralLocators.GENERIC_SUBMISSION_LIMIT_OPTION,
                                                     template, option)
