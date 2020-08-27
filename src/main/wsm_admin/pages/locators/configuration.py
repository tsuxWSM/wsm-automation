from selenium.webdriver.common.by import By


class ConfigurationLocator:
    """Page Object for Configuration page locators"""

    CONFIGURATION_TITLE = (By.XPATH, "//th[text()='Configuration']")
    SITE_INFORMATION_BUTTON = (By.CSS_SELECTOR, "#site-information-config")
    GENERAL_BUTTON = (By.CSS_SELECTOR, "#general-config")
    CATALOG_BUTTON = (By.CSS_SELECTOR, "#catalog-config")
    CART_BUTTON = (By.CSS_SELECTOR, "#cart-config")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "#checkout-config")
    SHIPPING_AND_HANDLING_BUTTON = (By.CSS_SELECTOR, "#shipping-config")
    PAYMENT_AND_PROCESSING_BUTTON = (By.CSS_SELECTOR, "#payment-config")
    IMAGES_BUTTON = (By.CSS_SELECTOR, "#images-config")
    INTEGRATION_BUTTON = (By.CSS_SELECTOR, "#integrations-config")
    AGS_BUTTON = (By.CSS_SELECTOR, "#ags-config")
    DNS_BUTTON = (By.CSS_SELECTOR, "#dns-config")
    ADVANCED_BUTTON = (By.CSS_SELECTOR, "#advanced-config")
    ADMIN_BUTTON = (By.CSS_SELECTOR, "#admin-config")
    MTL_BUTTON = (By.CSS_SELECTOR, "#mtl-config")
    RETURN_BUTTON = (By.XPATH, "//a[@title='Return']//img")
    TOP_BUTTON = (By.XPATH, "//a[@title='Jump to Top']//img")
    SAVE_CHANGES_INPUT = (By.CSS_SELECTOR, "#config_save_changes")


class SiteInformationLocators:
    """Page Object for Site Information page locators"""

    SITE_INFORMATION_TITLE = (By.XPATH,
                              "//tbody[@id='site-information-config-section']//th[text()='Site Information']")
    SITE_NAME_INPUT = (By.CSS_SELECTOR, "#config_title")
    OWNERS_NAME_INPUT = (By.CSS_SELECTOR, "#config_owner")
    COMPANY_INPUT = (By.CSS_SELECTOR, "#config_company")
    ADDRESS_ONE_INPUT = (By.CSS_SELECTOR, "#config_address1")
    ADDRESS_TWO_INPUT = (By.CSS_SELECTOR, "#config_address2")
    CITY_INPUT = (By.CSS_SELECTOR, "#config_city")
    COUNTRY_DROPDOWN = (By.CSS_SELECTOR, "#config_country")
    GENERIC_COUNTRY_OPTION = (By.XPATH, "//select[@id='config_default_country']//option[text()='$COUNTRY$']")
    STATE_PROVINCE_DROPDOWN = (By.XPATH, "//select[@id='config_state']")
    GENERIC_STATE_PROVINCE_OPTION = (By.XPATH, "//select[@id='config_state']//option[text()='STATE,PROVINCE']")
    ZIP_CODE_INPUT = (By.CSS_SELECTOR, "#config_zip")
    TOLL_FREE_INPUT = (By.CSS_SELECTOR, "#config_toll_free")
    PHONE_INPUT = (By.CSS_SELECTOR, "#config_phone")
    FAX_INPUT = (By.CSS_SELECTOR, "#config_fax")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#config_email")
    CURRENCY_CODE_DROPDOWN = (By.XPATH, "//select[@name='config[currency]']")
    GENERIC_CURRENCY_OPTION = (By.XPATH, "//select[@name='config[currency]']//option[text()='$OPTION$']")
    LANGUAGE_DROPDOWN = (By.XPATH, "//select[@name='config[language]']")
    GENERIC_LANGUAGE_OPTION = (By.XPATH, "//select[@name='config[language]']//option[text()='$LANGUAGE$']")
    LOGO_URL_INPUT = (By.CSS_SELECTOR, "#config_logo_url")
    LOGO_URL_IMG = (By.CSS_SELECTOR, "")
    FAVORITE_ICON_INPUT = (By.CSS_SELECTOR, "#config_favicon_url")
    FAVORITE_ICON_IMG = (By.CSS_SELECTOR, "")


class GeneralLocators:
    """Page Object for General page locators"""

    GENERAL_TITLE = (By.XPATH, "//th[text()='General']")
    NEWS_ARTICLES_INPUT = (By.CSS_SELECTOR, "#config_news_count")
    ALLOW_COMMENTS_CHECKBOX = (By.CSS_SELECTOR, "#config_allow_comments")
    NEWS_SUMMARY_CHARACTERS_INPUT = (By.CSS_SELECTOR, "#config_summary_characters")
    DISPLAY_NEWS_ARTICLE_THUMBNAILS_CHECKBOX = (By.CSS_SELECTOR, "#config_show_news_article_thumbnail")
    CONTACT_FORM_TEXT_TEXTAREA = (By.CSS_SELECTOR, "#config_contact_preamble")
    # TODO: TIME ZONE IT HAS TOO MANY OPTIONS.
    ORDER_UPDATE_REDIRECT_DROPDOWN = (By.CSS_SELECTOR, "select[name='config[order_update_redirect]']")
    GENERIC_ORDER_UPDATE_REDIRECT_OPTION = (By.XPATH, "//OPTION[text()='$TEXT$']")
    RESULTS_PER_PAGE_IN_MY_ORDERS_DROPDOWN = (By.CSS_SELECTOR, "select[name='config[my_orders_per_page]']")
    GENERIC_RESULTS_PER_PAGE_OPTION = (By.XPATH, "//select[@id='config_my_orders_per_page']/option[text()='$VALUE$']")
    CUSTOM_LOGIN_USERNAME_ON_RADIO = (By.CSS_SELECTOR, "#config_custom_login_username_on")
    CUSTOM_LOGIN_USERNAME_OFF_RADIO = (By.CSS_SELECTOR, "#config_custom_login_username_off")
    SAVE_COMPANY_WITH_ACCOUNT_CHECKBOX = (By.CSS_SELECTOR, "#config_save_company_with_account")

    CUSTOMER_FORM_SPAM_SETTINGS_TITLE = (By.XPATH, "//th[text()='Customer Form Spam Settings']")
    RECAPTCHA_SITE_KEY_INPUT = (By.CSS_SELECTOR, "#config_recaptcha_site_key")
    GENERATE_RECAPTCHA_SITE_KEY_LINK = (By.XPATH, "//a[text()='Generate reCAPTCHA site key']")
    GET_HELP_SETTING_UP_RECAPTCHA_LINK = (By.XPATH, "//a[text()='Get help setting up reCAPTCHA']")
    RECAPTCHA_SECRET_INPUT = (By.CSS_SELECTOR, "#config_recaptcha_secret")
    SUBMISSION_LIMIT_DROPDOWN = (By.CSS_SELECTOR, "#config_inquiry_form_limit")
    GENERIC_SUBMISSION_LIMIT_OPTION = (By.XPATH, "//select[@id='config_inquiry_form_limit']/option[text()='$LIMIT$']")
    SUBMISSION_LIMIT_INTERVAL_INPUT = (By.CSS_SELECTOR, "#config_inquiry_form_limit_interval")

    WYSIWYG_EDITOR_TITLE = (By.XPATH, "//th[text()='WYSIWYG Editor']")
    WYSIWYG_MINIMUM_RADIO = (By.CSS_SELECTOR, "#config_wysiwyg_minimum")
    WYSIWYG_MEDIUM_RADIO = (By.CSS_SELECTOR, "#config_wysiwyg_medium")
    WYSIWYG_MAXIMUM_RADIO = (By.CSS_SELECTOR, "#config_wysiwyg_maximum")

    INVOICE_PRINTING_TITLE = (By.XPATH, "//th[text()='Invoice Printing']")
    SHIPPING_FIELD_LEFT_JUSTIFICATION_RADIO = (By.CSS_SELECTOR, "#config_shipping_field_print_location.focus")
    SHIPPING_FIELD_RIGHT_JUSTIFICATION_RADIO = (By.CSS_SELECTOR,
                                                "#config_shipping_field_print_location[value='right']")
    SHIPPING_METHOD_LEFT_JUSTIFICATION_RADIO = (By.CSS_SELECTOR, "#config_shipping_method_print_location.focus")
    SHIPPING_METHOD_RIGHT_JUSTIFICATION_RADIO = (By.CSS_SELECTOR,
                                                 "#config_shipping_method_print_location[value='right']")
    ADD_WEBSITE_URL_TO_FORMS_CHECKBOX = (By.CSS_SELECTOR, "config_add_url_forms")
