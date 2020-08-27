from selenium.webdriver.common.by import By


class AdvancedSearchLocator:
    """Page Object for Quote Builder page sub locators"""

    # Quote Builder beta form
    TITLE_SEARCH = (By.XPATH, "//th[text() = 'Advanced Search']")
    ID_INPUT = (By.XPATH, "//input[@name='f[id][min]']")
    ID_TO_INPUT = (By.XPATH, "//input[@name='f[id][max]']")
    NAME_INPUT = (By.CSS_SELECTOR, "#pager_filter_name")
    CUSTOMER_GROUP_INPUT = (By.CSS_SELECTOR, "#pager_filter_customer_group")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#pager_filter_email")
    COMPANY_INPUT = (By.CSS_SELECTOR, "#pager_filter_company")
    ACCOUNT_NUMBER_INPUT = (By.CSS_SELECTOR, "#pager_filter_account_number")
    BROWSER_INPUT = (By.CSS_SELECTOR, "#pager_filter_browser")
    IP_INPUT = (By.CSS_SELECTOR, "#pager_filter_ip")

    SHIPPING_METHOD_MATRIX_INPUT = (By.CSS_SELECTOR, "#pager_filter_shipping_method_matrix_name")

    PROMOTION_CODE = (By.CSS_SELECTOR, "input[name='f[coupon_code]']")

    MEMO_INPUT = (By.CSS_SELECTOR, "#pager_filter_memo")
    TEST_DROPDOWN = (By.CSS_SELECTOR, "#pager_filter_test")

    # TODO: Still not sure which rule of conf provides the common SHIPPING METHODS for this filter, currently not in use
    FREE_SHIPPING_INPUT = (By.CSS_SELECTOR, "#pager_filter_shipping_method_$METHOD_NUMBER$")
    # TODO: Still not sure which rule of conf provides the common PAYMENT METHODS for this filter, currently not in use
    PAYMENT_METHOD_CHECKBOX = (By.CSS_SELECTOR, "#pager_filter_payment_method_$METHOD$")

    HANDLING_INPUT = (By.CSS_SELECTOR, "input[name='f[handling][min]']")
    HANDLING_TO_INPUT = (By.CSS_SELECTOR, "input[name='f[handling][max]']")
    DISCOUNT_INPUT = (By.CSS_SELECTOR, "input[name='f[discount][min]']")
    DISCOUNT_TO_INPUT = (By.CSS_SELECTOR, "input[name='f[discount][max]']")
    TAX_INPUT = (By.CSS_SELECTOR, "input[name='f[tax][min]']")
    TAX_TO_INPUT = (By.CSS_SELECTOR, "input[name='f[tax][max]']")
    # STATUS
    GENERIC_STATUS_CHECK = (By.CSS_SELECTOR, "#pager_filter_status_$STATUS$")
    # TEST
    GENERIC_TEST_OPTION = (By.XPATH, "//option[text()='$TEST_OPTION$']")
    # ADDED
    ADDED_DATE_INPUT = (By.CSS_SELECTOR, "#pager_filter_added_date")
    ADDED_TIME_INPUT = (By.CSS_SELECTOR, "#pager_filter_added_time")
    ADDED_TO_DATE_INPUT = (By.CSS_SELECTOR, "#pager_filter_added_max_date")
    ADDED_TO_TIME_INPUT = (By.CSS_SELECTOR, "#pager_filter_added_max_time")
    # TODO: PENDING THE TW0 ADDED IMG
    # EXPIRES ON
    # TODO: PENDING EXPIRES ON ALL BOXES
    # UPDATED
    STAMP_DATE_INPUT = (By.CSS_SELECTOR, "#pager_filter_stamp_date")
    STAMP_TIME_INPUT = (By.CSS_SELECTOR, "#pager_filter_stamp_time")
    STAMP_TO_DATE_INPUT = (By.CSS_SELECTOR, "#pager_filter_stamp_max_date")
    STAMP_TO_TIME_INPUT = (By.CSS_SELECTOR, "#pager_filter_stamp_max_time")
    # TODO: PENDING THE TW0 STAMP IMG
    SEARCH_BUTTON = (By.XPATH, "//button[text()='Search']")
    CLEAR_SEARCH_BUTTON = (By.XPATH, "//button[text()='Clear Search']")


class QuoteBuilderLocators(AdvancedSearchLocator):
    """Page Object for Quote Builder page locators"""

    # Quote Builder beta form
    TYPE_SEARCH_TERMS_INPUT = (By.CSS_SELECTOR, "#pager_search_query")
    SEARCH_BUTTON_INPUT = (By.CSS_SELECTOR, "input[value='Search']")
    ADVANCED_BUTTON = (By.XPATH, "//div[@id='search']//button[text()='Advanced']")
    ADD_QUOTE_BUTTON = (By.XPATH, "//div[@id='search']//button[text()='Add Quote']")
    ADD_QUOTE_BUTTON_UNDERNEATH = (By.XPATH, "//tfoot[@class='actions']//button[text()='Add Quote']")
    HELD_LEGEND_TITLE = (By.XPATH, "//div[@id='help_legend']//td[text()='Item Actions']")
    HELD_LEGEND_TITLE_ONE = (By.XPATH, "//div[@id='help_legend']//td[text()='Open the item for editing.']")
    HELD_LEGEND_TITLE_TWO = (By.XPATH,
                             "//div[@id='help_legend']//td[text()='Create a new Quote by cloning this Quote.']")
    HELD_LEGEND_TITLE_THREE = (By.XPATH,
                               "//div[@id='help_legend']//td[text()='Permanently removes the item from the system." 
                               "  WARNING: this cannot be undone!']")
    RETURN_LINK = (By.CSS_SELECTOR, "a[title='Return']")
    TOP_LINK = (By.CSS_SELECTOR, "a[title='Jump to Top']")
