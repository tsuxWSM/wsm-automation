from selenium.webdriver.common.by import By


class CustomerEdit:
    """A class for Customer Edit page locators"""
    ACTIVE_USER_TRUE = (By.CSS_SELECTOR, "input#form_active")
    ACTIVE_USER_FALSE = (By.CSS_SELECTOR, "input#form_active_false")

    EMAIL_INPUT = (By.CSS_SELECTOR, "input#form_email")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input#form_password")
    ALTERNATE_ID_INPUT = (By.CSS_SELECTOR, "input#form_alternate_identifier")
    ACCOUNT_NUMBER_INPUT = (By.CSS_SELECTOR, "input#form_account_number")
    NAME_INPUT = (By.CSS_SELECTOR, "input#form_firstname")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "input#form_lastname")
    COMPANY_INPUT = (By.CSS_SELECTOR, "input#form_birthdate")
    BIRTH_DATE_INPUT = (By.CSS_SELECTOR, "input#form_company")
    ACCOUNT_STATUS_DROPDOWN = (By.CSS_SELECTOR, "select#form_customer_account_status")
    BALANCE_DUE_INPUT = (By.CSS_SELECTOR, "input#form_customer_balance_due")

    # Radio buttons
    TAX_EXEMPT_TRUE = (By.CSS_SELECTOR, "input#form_notax")
    TAX_EXEMPT_FALSE = (By.CSS_SELECTOR, "input#form_notax_false")

    INVOICE_TRUE = (By.CSS_SELECTOR, "input#form_invoicepayment")
    INVOICE_FALSE = (By.CSS_SELECTOR, "input#form_invoicepayment_false")

    AFFIRM_ALLOWED_TRUE = (By.CSS_SELECTOR, "input#form_affirm_allowed")
    AFFIRM_ALLOWED_FALSE = (By.CSS_SELECTOR, "input#form_affirm_allowed_false")

    BLOCK_FREE_SHIPPING_TRUE = (By.CSS_SELECTOR, "input#form_nofreeshipping")
    BLOCK_FREE_SHIPPING_FALSE = (By.CSS_SELECTOR, "input#form_nofreeshipping_false")

    # Price Group
    PRICE_GROUP_DROPDOWN = (By.CSS_SELECTOR, "select#form_group")

    # Access group section
    SALES_GROUP_CHECKBOX = (By.CSS_SELECTOR, "input.form_access_group")
    SELECT_ALL_BUTTON = (By.CSS_SELECTOR, "button.selectall_btn")
    CLEAR_ALL_BUTTON = (By.CSS_SELECTOR, "button.clear_btn")

    # Main Action Buttons
    ADD_CUSTOMER_BUTTON = (By.CSS_SELECTOR, "input.add_btn")
    SAVE_CUSTOMER_BUTTON = (By.CSS_SELECTOR, "input.save_btn")
    DELETE_BUTTON = (By.CSS_SELECTOR, "input.delete_btn")

