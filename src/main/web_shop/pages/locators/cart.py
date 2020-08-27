from selenium.webdriver.common.by import By


class CartLocators:
    """A class for Cart Page locators"""

    # Notifications/Messages
    GREEN_MESSAGE = "li.wsm_message"

    # Cart Details Table
    GENERIC_ITEM_NAME = \
        (By.XPATH, ".wsm_cart_item_info_wrapper a[title='$ITEM_NAME$']")
    GENERIC_DELETE_ITEM_LINK = (By.XPATH,
                                "//a[text()='$ITEM_NAME$']/ancestor::div[@class='wsm_cart_item_info_wrapper']"
                                "//a[@title='Delete this item from the cart']")
    GENERIC_UPDATE_BUTTON = (By.XPATH,
                             "//a[text()='Coverlay 18-714C-NTL Interior Accessories Kit']"
                             "/ancestor::div[@class='wsm_cart_item_info_wrapper']//button[text()='Update Qty']")
    GENERIC_PRICE_FIELD = (By.XPATH,
                           "//a[text()='$ITEM_NAME$']/ancestor::div[@class='wsm_cart_item_info_wrapper']"
                           "//div[@class='wsm_cart_item_price']"
                           "//span[contains(@class, 'wsm_cart_item_value_price')]")
    GENERIC_TOTAL_FIELD = (By.XPATH,
                           "//a[text()='$ITEM_NAME$']/ancestor::div[@class='wsm_cart_item_info_wrapper']"
                           "//div[@class='wsm_cart_item_total']//span[contains(@class, 'wsm_cart_item_value_price')]")

    # Cart Totals
    CART_SUBTOTAL = (By.CSS_SELECTOR, ".wsm_cart_total_row_subtotal .wsm_cart_total_amount")
    CART_TOTAL = (By.CSS_SELECTOR, ".wsm_cart_total_row_total .wsm_cart_total_amount")

    # User Action Section
    GENERIC_SAVE_QUOTE_BUTTON = \
        (By.XPATH, "//section[@id='wsm_cart_review_total']//button[contains(text(), 'Save Quote #$QUOTE_NUMBER$')]")
    CREATE_QUOTE_BUTTON = (By.XPATH, "//section[@id='wsm_cart_review_total']//button[contains(text(), 'Create Quote')]")
    PROCEED_TO_CHECKOUT_BUTTON = \
        (By.XPATH, "//section[@id='wsm_cart_review_total']//button[contains(text(), 'Proceed to Checkout')]")
    EXIT_QUOTE_LINK = (By.XPATH, "//a[text()='EXIT QUOTE']")
