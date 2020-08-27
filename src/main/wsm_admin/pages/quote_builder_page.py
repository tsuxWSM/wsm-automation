from .base_page import AdminTopPanel
from ...utils.ui.web_element import BaseWebElement, GenericWebElement, DropdownWebElement, VisualWebElement
from .locators.quote_builder import QuoteBuilderLocators, AdvancedSearchLocator
from enum import Enum


class QuoteStatus(Enum):
    BACKORDER = "backorder"
    BUILDING = "building"
    CANCELED = "canceled"
    COMPLETE = "complete"
    DELETED = "deleted"
    DRAFT_OPEN = "draft_open"
    EXPIRED = "expired"
    FRAUD = "fraud"
    HELD = "held"
    NEW = "new"
    PENDING = "pending"
    PROCESSING = "processing"
    READY_TO_SHIP = "ready_to_ship"
    RETURN = "return"
    SHIPPED = "shipped"


class TestOption(Enum):
    ANY = "any"
    YES = "Yes"
    NO = "No"


class AdvancedSearchPanel(AdminTopPanel):

    def __init__(self, driver):
        super().__init__(driver)
        self.items_status_count = 0
        self.items_test_count = 0

        self.title_search = BaseWebElement(driver, AdvancedSearchLocator.TITLE_SEARCH)

        self.id_input = BaseWebElement(driver, AdvancedSearchLocator.ID_INPUT)
        self.id_to_input = BaseWebElement(driver, AdvancedSearchLocator.ID_TO_INPUT)
        self.name_input = BaseWebElement(driver, AdvancedSearchLocator.NAME_INPUT)
        self.customer_group_input = BaseWebElement(driver, AdvancedSearchLocator.CUSTOMER_GROUP_INPUT)
        self.email_input = BaseWebElement(driver, AdvancedSearchLocator.EMAIL_INPUT)
        self.company_input = BaseWebElement(driver, AdvancedSearchLocator.COMPANY_INPUT)
        self.account_number_input = BaseWebElement(driver, AdvancedSearchLocator.ACCOUNT_NUMBER_INPUT)
        self.browser_input = BaseWebElement(driver, AdvancedSearchLocator.BROWSER_INPUT)
        self.ip_input = BaseWebElement(driver, AdvancedSearchLocator.IP_INPUT)

        self.shipping_method_matrix_input = BaseWebElement(driver, AdvancedSearchLocator.SHIPPING_METHOD_MATRIX_INPUT)

        self.promotion_code = BaseWebElement(driver, AdvancedSearchLocator.PROMOTION_CODE)

        self.memo_input = BaseWebElement(driver, AdvancedSearchLocator.MEMO_INPUT)

        self.test_dropdown = None

        self.handling_input = BaseWebElement(driver, AdvancedSearchLocator.HANDLING_INPUT)
        self.handling_to_input = BaseWebElement(driver, AdvancedSearchLocator.HANDLING_TO_INPUT)
        self.discount_input = BaseWebElement(driver, AdvancedSearchLocator.DISCOUNT_INPUT)
        self.discount_to_input = BaseWebElement(driver, AdvancedSearchLocator.DISCOUNT_TO_INPUT)
        self.tax_input = BaseWebElement(driver, AdvancedSearchLocator.TAX_INPUT)
        self.tax_to_input = BaseWebElement(driver, AdvancedSearchLocator.TAX_TO_INPUT)

        self.added_date_input = BaseWebElement(driver, AdvancedSearchLocator.ADDED_DATE_INPUT)
        self.added_time_input = BaseWebElement(driver, AdvancedSearchLocator.ADDED_TIME_INPUT)
        self.added_to_date_input = BaseWebElement(driver, AdvancedSearchLocator.ADDED_TO_DATE_INPUT)
        self.added_to_time_input = BaseWebElement(driver, AdvancedSearchLocator.ADDED_TO_TIME_INPUT)
        self.stamp_date_input = BaseWebElement(driver, AdvancedSearchLocator.STAMP_DATE_INPUT)
        self.stamp_time_input = BaseWebElement(driver, AdvancedSearchLocator.STAMP_TIME_INPUT)
        self.stamp_to_date_input = BaseWebElement(driver, AdvancedSearchLocator.STAMP_TO_DATE_INPUT)
        self.added_time_input = BaseWebElement(driver, AdvancedSearchLocator.STAMP_TO_TIME_INPUT)
        self.search_button = BaseWebElement(driver, AdvancedSearchLocator.SEARCH_BUTTON)
        self.clear_search_button = BaseWebElement(driver, AdvancedSearchLocator.CLEAR_SEARCH_BUTTON)

    def select_test_option(self, option: TestOption):
        template = "$TEST_OPTION$"

        self.test_dropdown.select_option(AdvancedSearchLocator.GENERIC_TEST_OPTION, template, option)

    def check_status(self, status: QuoteStatus):
        template = "$STATUS$"

        check_box = GenericWebElement(self.driver, AdvancedSearchLocator.GENERIC_STATUS_CHECK, template, status)

        check_box.click()


class QuoteBuilderPage(AdvancedSearchPanel):

    def __init__(self, driver):
        super().__init__(driver)

        self.type_search_terms_input = VisualWebElement(driver, QuoteBuilderLocators.TYPE_SEARCH_TERMS_INPUT)
        self.search_button_input = VisualWebElement(driver, QuoteBuilderLocators.SEARCH_BUTTON_INPUT)
        self.advanced_button = VisualWebElement(driver, QuoteBuilderLocators.ADVANCED_BUTTON)
        self.add_quote_button = VisualWebElement(driver, QuoteBuilderLocators.ADD_QUOTE_BUTTON)
        self.add_quote_button_underneath = VisualWebElement(driver, QuoteBuilderLocators.ADD_QUOTE_BUTTON_UNDERNEATH)
        self.held_legend_th = VisualWebElement(driver, QuoteBuilderLocators.HELD_LEGEND_TITLE)
        self.held_legend_th_one = VisualWebElement(driver, QuoteBuilderLocators.HELD_LEGEND_TITLE_ONE)
        self.held_legend_th_two = VisualWebElement(driver, QuoteBuilderLocators.HELD_LEGEND_TITLE_TWO)
        self.held_legend_th_three = VisualWebElement(driver, QuoteBuilderLocators.HELD_LEGEND_TITLE_THREE)
        self.return_link = VisualWebElement(driver, QuoteBuilderLocators.RETURN_LINK)
        self.top_link = VisualWebElement(driver, QuoteBuilderLocators.TOP_LINK)

    def advanced_search_button_click(self):
        self.advanced_button.click()

        self.test_dropdown = DropdownWebElement(self.driver, AdvancedSearchLocator.TEST_DROPDOWN)

    def get_advanced_status_option(self, advanced_status: QuoteStatus):
        var_template = "$STATUS$"

        return VisualWebElement(self.driver,
                                (AdvancedSearchLocator.GENERIC_STATUS_CHECK[0],
                                 AdvancedSearchLocator.GENERIC_STATUS_CHECK[1].replace(var_template,
                                                                                       advanced_status.value)))

    def get_advanced_test_option(self, advanced_test: TestOption):
        var_template = "$TEST_OPTION$"

        return VisualWebElement(self.driver,
                                (AdvancedSearchLocator.GENERIC_TEST_OPTION[0],
                                 AdvancedSearchLocator.GENERIC_TEST_OPTION[1].replace(var_template,
                                                                                      advanced_test.value)))
