from selenium.webdriver.common.by import By


class CheckoutLocators:
    """Locator for Extreme Metal Products Checkout Page"""

    ACCOUNT_SECTION_TITLE = (By.XPATH, "//span[text()='Account Selection']")

    # Guest Form
    CHECKOUT_AS_GUEST_RADIO = (By.XPATH, "//span[text()='Checkout as Guest']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#wsm_form_guest_email")
    SUBSCRIBE_CHECKBOX = (By.CSS_SELECTOR, "#wsm_form_subscribe_guest")

    # Sign Up Form
    CREATE_NEW_ACCOUNT_RADIO = (By.XPATH, "//span[text()='Create New Account']")
    REGISTER_EMAIL_INPUT = (By.CSS_SELECTOR, "#wsm_form_register_email")
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "#wsm_form_register_firstname")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "#wsm_form_register_lastname")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#wsm_form_register_password1")
    CONFIRM_PASSWORD_INPUT = (By.CSS_SELECTOR, "#wsm_form_register_password2")
    GUEST_SUBSCRIBE_CHECKBOX = \
        (By.XPATH, "//label[text()='Please inform me of product information, updates, and specials.']")
    REGISTER_NEW_ACCOUNT_INPUT = (By.CSS_SELECTOR, "#wsm_form_register_button")

    # Login Form
    LOG_INTO_YOUR_ACCOUNT_RADIO = (By.XPATH, "//span[text()='Log into Your Account']")
    LOG_EMAIL_INPUT = (By.CSS_SELECTOR, "#wsm_form_login_email")
    LOG_PASSWORD_INPUT = (By.CSS_SELECTOR, "#wsm_form_login_password")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//div[@id='wsm_account_accordion_content_login']//a[text()='Forgot Password?']")
    LOGIN_INPUT = (By.CSS_SELECTOR, "#wsm_form_login_button")

    # Address Information Section
    ADDRESS_INFORMATION_TITLE = (By.XPATH, "//span[text()='Address Information']")
    # TODO: Next locator only applies for some sites
    BILLING_AND_SHIPPING_ADDRESS_TITLE = (By.CSS_SELECTOR, "#wsm_checkout_address_billing_header")
    COMPANY_INPUT = (By.CSS_SELECTOR, "#wsm_form_billing_company")
    FIRST_NAME_ADDRESS_INPUT = (By.CSS_SELECTOR, "#wsm_form_billing_firstname")
    LAST_NAME_ADDRESS_INPUT = (By.CSS_SELECTOR, "#wsm_form_billing_lastname")
    COUNTRY_DROPDOWN = (By.CSS_SELECTOR, "#wsm_form_billing_country")
    STREET_INPUT = (By.CSS_SELECTOR, "#wsm_form_billing_address")
    SUITE_NO_INPUT = (By.CSS_SELECTOR, "#wsm_form_billing_address2")
    CITY_INPUT = (By.CSS_SELECTOR, "#wsm_form_billing_city")
    STATE_DROPDOWN = (By.CSS_SELECTOR, "#wsm_form_billing_state")
    ZIP_INPUT = (By.CSS_SELECTOR, "#wsm_form_billing_zip")
    PHONE_INPUT = (By.CSS_SELECTOR, "#wsm_form_billing_phone")
    EXTENSION_INPUT = (By.CSS_SELECTOR, "#wsm_form_billing_extension")

    SEPARATE_SHIPPING_ADDRESS_CHECKBOX = (By.CSS_SELECTOR, "input[value='separate']")

    # Separate Shipping Section
    SHIPPING_COMPANY_INPUT = (By.CSS_SELECTOR, "#wsm_form_shipping_company")
    SHIPPING_FIRST_NAME_INPUT = (By.CSS_SELECTOR, "#wsm_form_shipping_firstname")
    SHIPPING_LAST_NAME_INPUT = (By.CSS_SELECTOR, "#wsm_form_shipping_lastname")
    SHIPPING_COUNTRY_DROPDOWN = (By.CSS_SELECTOR, "#wsm_form_shipping_country")
    SHIPPING_STREET_INPUT = (By.CSS_SELECTOR, "#wsm_form_shipping_address")
    SHIPPING_SUITE_NO_INPUT = (By.CSS_SELECTOR, "#wsm_form_shipping_address2")
    SHIPPING_CITY_INPUT = (By.CSS_SELECTOR, "#wsm_form_shipping_city")
    SHIPPING_STATE_DROPDOWN = (By.CSS_SELECTOR, "#wsm_form_shipping_state")
    SHIPPING_ZIP_INPUT = (By.CSS_SELECTOR, "#wsm_form_shipping_zip")
    SHIPPING_PHONE_INPUT = (By.CSS_SELECTOR, "#wsm_form_shipping_phone")
    SHIPPING_EXTENSION_INPUT = (By.CSS_SELECTOR, "#wsm_form_shipping_extension")

    # Payment Section
    PAYMENT_INFORMATION_TITLE = (By.XPATH, "//span[text()='Payment Information']")
    CARD_RADIO = (By.XPATH, "//span[text()='Pay Securely Using My Credit or Debit Card']")
    CARD_NUMBER_INPUT = (By.CSS_SELECTOR, "#wsm_form_credit_number")
    NAME_ON_CARD_INPUT = (By.CSS_SELECTOR, "#wsm_form_credit_name")
    MONTH_DROPDOWN = (By.CSS_SELECTOR, "#wsm_form_credit_expire_month")
    GENERIC_MONTH_OPTION = (By.XPATH, "")
    YEAR_DROPDOWN = (By.CSS_SELECTOR, "#wsm_form_card_date_year")
    GENERIC_YEAR_OPTION = (By.XPATH, "")
    CVV_INPUT = (By.CSS_SELECTOR, "#wsm_form_credit_cid")
    WHERE_IS_THIS_LINK = (By.CSS_SELECTOR, "#wsm_form_credit_cid_hint")

    # For invoice
    CHECKOUT_LABEL = (By.CSS_SELECTOR, ".wsm_checkout_label")
    CHECKOUT_INFO = (By.CSS_SELECTOR, "p.wsm_checkout_pm_info")
    CHECKOUT_PM_LOGO = (By.CSS_SELECTOR, "p.wsm_checkout_pm_logo")

    # Order Checkout Section
    ORDER_CHECKOUT_TITLE = (By.XPATH, "//span[text()='Order Checkout']")
    ORDER_COMMENTS_INPUT = (By.CSS_SELECTOR, "#wsm_form_question_413")

    # Checkout Questions (invoice)
    VEHICLE_VERIFICATION_FIELD = (By.CSS_SELECTOR, "#wsm_form_question_353")
    SPECIAL_INSTRUCTIONS_FIELD = (By.CSS_SELECTOR, "#wsm_form_question_356")

    SHIPPING_OPTIONS_BOX = (By.CSS_SELECTOR, "#wsm_form_shipping_method")

    # Order Totals Section
    SUBTOTAL_FIELD = (By.CSS_SELECTOR, "#wsmjs-checkout-subtotal-amount")
    SHIPPING_FIELD = (By.CSS_SELECTOR, "#wsmjs-checkout-shipping-amount")
    TOTAL_FIELD = (By.CSS_SELECTOR, "#wsmjs-checkout-total-amount")

    GENERIC_OPTION = (By.XPATH, "//select//option[text()='OPTION$']")

    SUBMIT_ORDER_BUTTON = (By.CSS_SELECTOR, "input.wsm_interface_btn_checkout_submit")
