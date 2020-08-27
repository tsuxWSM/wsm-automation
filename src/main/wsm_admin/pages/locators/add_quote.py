from selenium.webdriver.common.by import By


class AddQuoteLocators:
    """A class for Add Quote page locators"""

    # Active Submenus
    ACTIVE_QUOTE_BUILDER = (By.CSS_SELECTOR, "#wsma_sub_menu a[title='See Quotes (Beta)']")
    ACTIVE_ADD_QUOTE = (By.CSS_SELECTOR, "#wsma_sub_menu a[title='Add Quote (Beta)']")

    # Orders (Add Quote Beta) menu
    GENERIC_SUBMENU = (By.XPATH, "//div[@id='wsma_sub_menu']//a[text()='$SUBMENU_TITLES$']")
    ADD_QUOTE_TITLE = (By.XPATH, "//th[text()='Add Quote']")
    EDIT_QUOTE_TITLE = (By.XPATH, "//th[starts-with(text(), 'Quote #')]")

    # Created Quote Actions
    LOAD_TO_CART_LINK = (By.XPATH, "//a[text()='Load quote --> cart']")
    COPY_LINK_BUTTON = (By.CSS_SELECTOR, "button#draft-to-edit-btn")
    # TODO: Error design detected in several elements at this page, and this led us to end up with weak locators like:
    PRINTER_ICON = (By.CSS_SELECTOR, "a img[src$='printer.png']")

    # Customer Information Section
    CUSTOMER_INFORMATION_TITLE = (By.XPATH, "//th[text()='Customer Information']")
    CUSTOMER_INPUT = (By.CSS_SELECTOR, "#order_name")
    EMAIL_ADDRESS_INPUT = (By.CSS_SELECTOR, "#order_email")
    ACCOUNT_NUMBER_INPUT = (By.CSS_SELECTOR, "#order_account_number")
    QUOTE_STATUS_DROPDOWN = (By.CSS_SELECTOR, "#order_status")
    MEMO_INPUT = (By.CSS_SELECTOR, "#order_memo")
    EXPIRES_INPUT = (By.CSS_SELECTOR, "#draft_expiration_date")  # Not at Add Order
    CALENDAR_ICON = (By.XPATH, "//img[@style='border: medium none;']")  # Not at Add Order
    CALENDAR_POPUP = (By.CSS_SELECTOR, "div#ui-datepicker-div")

    # Address Information Section
    ADDRESS_INFORMATION_TITLE = (By.XPATH, "//th[text()='Address Information']")
    BILLING_ADDRESS_LINK = (By.CSS_SELECTOR, "#billing_address_add")  # Not at Add Order
    SHIPPING_ADDRESS_LINK = (By.CSS_SELECTOR, "#shipping_address_add")
    SHIPPING_METHOD_DROPDOWN = (By.CSS_SELECTOR, "#shipping_method")
    GENERIC_SHIPPING_OPTION = (By.XPATH, "//select[@id='shipping_method']//option[text()='$SHIPPING_METHOD$']")
    HELP_ICON_TOTAL_AMOUNT_DUE = (By.XPATH, "//td[@id='wsma-order-total-due']/preceding-sibling::td//img")
    TOTAL_AMOUNT_DUE = (By.CSS_SELECTOR, "#wsma-order-total-due")  # Total Amount Field

    # Payment Information Section
    BILLING_ADDRESS_TITLE = (By.CSS_SELECTOR, "#billing_address_add")
    PAYMENT_INFORMATION_TITLE = (By.CSS_SELECTOR, "")
    ORDER_PAYMENT_DROPDOWN = (By.CSS_SELECTOR, "#order-payment-add-type")
    GENERIC_PAYMENT_OPTION = (By.XPATH, "//option[@value='$PAYMENT_METHOD$']")
    ADD_PAYMENT_BUTTON = (By.XPATH, "//button[text()='Add Payment']")

    # Quote Information Section
    QUOTE_INFORMATION_TITLE = (By.XPATH, "//th[text()='Quote Information']")
    GENERIC_ITEM_NAME_INPUT = (By.CSS_SELECTOR, "#order_item_new$ITEM$_name")  # Item Name generic field per position
    ITEM_STATUS_DROPDOWN = (By.CSS_SELECTOR, "#order_item_new$ITEM$_status")  # Status generic field per position

    QUANTITY_INPUT = (By.CSS_SELECTOR, "#order_item_new$ITEM$_quantity")  # Quantity generic field per position
    UNIT_PRICE_INPUT = (By.CSS_SELECTOR, "#order_item_new$ITEM$_price")  # Unit Price generic field per position
    TOTAL_PRICE = (By.CSS_SELECTOR, "#order_item_new$ITEM$_total")  # Total Price generic field per position

    SKU_INPUT = (By.CSS_SELECTOR, "#order_item_new$ITEM$_sku")
    ADD_CUSTOM_ITEM_BUTTON = (By.XPATH, "//button[text()='Add Custom Item']")
    ADD_ITEM_BUTTON = (By.XPATH, "//button[text()='Add Item']")
    REMOVE_ITEM_ICONS = (By.XPATH, "//img[@title='Remove Item']")
    FIRST_RESULT_ITEM = (By.CSS_SELECTOR, "div.jqac-menu ul li span")
    GENERIC_SEARCH_RESULT_ITEM = (By.CSS_SELECTOR, "span.jqac-link[name='$RESULT$']")

    # Discounts Section
    DISCOUNTS_TITLE = (By.CSS_SELECTOR, "#draft-discount-title-th")
    HELP_ICON_PROMOTIONS_CODE = (By.CSS_SELECTOR, "#draft-promotion .helpPopupControl img")
    USE_MARKDOWNS_BUTTON = (By.XPATH, "//button[text()='Use markdowns']")  # Add Markdown button
    USE_PROMOTION_BUTTON = (By.XPATH, "//button[text()='Use promotion']")  # Add Promotion button

    # Subtotals and Total Section
    SUBTOTAL = (By.CSS_SELECTOR, "#order_subtotal")  # Subtotal field
    SHIPPING_INPUT = (By.CSS_SELECTOR, "#order_shipping")  # Shipping field
    HANDLING_INPUT = (By.CSS_SELECTOR, "#order_handling")  # Handling field
    SALES_TAX_INPUT = (By.CSS_SELECTOR, "#order_tax")  # Sales Tax field
    DISCOUNTS = (By.CSS_SELECTOR, "#order_discount")  # Discounts field
    GRAND_TOTAL = (By.CSS_SELECTOR, "#order_total")  # Total field
    HELP_ICON_CALCULATOR = (By.XPATH, "//a[@id='order-tax-calculator-open']/preceding-sibling::div/img")

    # Calculator
    TAX_OPEN_CALCULATOR_LINK = (By.CSS_SELECTOR, "#order-tax-calculator-open")
    TAX_RATE_INPUT = (By.CSS_SELECTOR, "#order-tax-rate")
    TAX_SHIPPING_INPUT = (By.CSS_SELECTOR, "#order-tax-shipping")
    BEFORE_PROMOTIONS_INPUT = (By.CSS_SELECTOR, "#order-tax-before-promotions")
    CALCULATE_BUTTON = (By.XPATH, "//button[text()='Calculate']")

    # At Add Order But Not at Add Quote
    ADD_TRACKING_NUMBER_BUTTON = (By.CSS_SELECTOR, "button#tracking_add")

    # User Comment Section
    COMMENTS_TITLE = (By.CSS_SELECTOR, "#order_discount")
    HELP_ICON_COMMENTS = (By.XPATH, "//textarea[@id='order_comment']/preceding-sibling::div/img")
    FORM_COMMENT_TEXTAREA = (By.CSS_SELECTOR, "#order_comment")
    SEND_EMAIL_BCC_INPUT = (By.XPATH, "//input[@name='form[send_email_bcc]']")

    # Submit and Nav Buttons
    CREATE_QUOTE_BUTTON = (By.CSS_SELECTOR, "#wsma-order-save-button")
    RETURN_LINK = (By.XPATH, "//a[@title='Return']")
    TOP_LINK = (By.XPATH, "//a[@title='Jump to Top']")
