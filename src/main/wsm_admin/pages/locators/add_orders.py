from selenium.webdriver.common.by import By


class AddOrdersLocators:
    """A Class for Add Order Page Locators"""

    ADD_ORDER_TITLE = (By.XPATH, "//th[text()='Add Order']")

    CUSTOMER_INFORMATION_TITLE = (By.XPATH, "//th[text()='Customer Information']")
    CUSTOMER_INPUT = (By.CSS_SELECTOR, "#order_name")
    EMAIL_ADDRESS_INPUT = (By.CSS_SELECTOR, "#order_email")
    SEND_EMAIL_IMG = (By.XPATH, "//img[@alt='Send Email']")
    ACCOUNT_NUMBER_INPUT = (By.CSS_SELECTOR, "#order_account_number")
    ORDER_STATUS_DROPDOWN = (By.CSS_SELECTOR, "#order_status")
    GENERIC_ORDER_STATUS_OPTION = (By.XPATH, "//select[@id='order_status']//option[text()='$New$']")
    MEMO_INPUT = (By.CSS_SELECTOR, "#order_memo")

    ADDRESS_INFORMATION_TITLE = (By.XPATH, "//th[text()='Address Information']")
    BILLING_ADDRESS_SUBTITLE = (By.XPATH, "//strong[text()='Billing Address']")
    COMPANY_BILLING_INPUT = (By.CSS_SELECTOR, "#order_company")
    FIRST_NAME_BILLING_INPUT = (By.CSS_SELECTOR, "#order_firstname")
    LAST_NAME_BILLING_INPUT = (By.CSS_SELECTOR, "#order_lastname")
    ADDRESS_BILLING_INPUT = (By.CSS_SELECTOR, "#order_address")  # Es infinito
    ADDRESS_OTHERS_BILLING_INPUT = (By.CSS_SELECTOR, "#order_address2")
    # FALTA CITY
    STATE_PROVINCE_BILLING_DROPDOWN = (By.CSS_SELECTOR, "#order_state")
    GENERIC_STATE_PROVINCE_BILLING_OPTION = \
        (By.XPATH, "//select[@id='order_state']//option[text()='- Select State or Province -']")
    # FALTA ZIP CODE
    # FALTA EL DROPDOWN DE COUNTRY
    GENERIC_COUNTRY_BILLING_OPTION = (By.XPATH, "//select[@id='order_country']//option[text()='United States']")
    PHONE_BILLING_INPUT = (By.CSS_SELECTOR, "#order_phone")
    PHONE_EXT_BILLING_INPUT = (By.CSS_SELECTOR, "#order_phone2")
    SHIPPING_ADDRESS_TITLE = (By.XPATH, "//strong[text()='Shipping Address']")
    SAME_AS_BILLING_ADDRESS_MESSAGE = (By.XPATH, "//div[@id='shipping_address_static']//i")
    ADD_NEW_ADDRESS_LINK = (By.CSS_SELECTOR, "#shipping_address_add")
    COMPANY_SHIPPING_INPUT = (By.CSS_SELECTOR, "#order_shipping_company")
    FIRST_NAME_SHIPPING_INPUT = (By.CSS_SELECTOR, "#order_shipping_firstname")
    LAST_NAME_SHIPPING_INPUT = (By.CSS_SELECTOR, "#order_shipping_lastname")
    # FALTA ADDRESS
    ADDRESS_OTHERS_SHIPPING_INPUT = (By.CSS_SELECTOR, "#order_shipping_address2")
    STATE_PROVINCE_SHIPPING_DROPDOWN = (By.CSS_SELECTOR, "#order_shipping_state")
    GENERIC_STATE_PROVINCE_SHIPPING_OPTION = \
        (By.XPATH, "//select[@id='order_shipping_state']//option[text()='- Select State or Province -']")
    # FALTA ZIP CODE
    # FALTA EL DROPDOWN DE COUNTRY
    GENERIC_COUNTRY_SHIPPING_OPTION = (By.XPATH,
                                       "//select[@id='order_shipping_country']//option[text()='United States']")
    PHONE_SHIPPING_INPUT = (By.CSS_SELECTOR, "#order_shipping_phone")
    PHONE_EXT_SHIPPING_INPUT = (By.CSS_SELECTOR, "#order_shipping_phone2")

    SHIPPING_METHOD_TITLE = (By.CSS_SELECTOR, "//th[text()='Shipping Method']")
    SHIPPING_METHOD_DROPDOWN = (By.CSS_SELECTOR, "#shipping_method")
    GENERIC_SHIPPING_METHOD_OPTION = (By.XPATH, "//select[@id='shipping_method']//option[text()='$-- none --$']")

