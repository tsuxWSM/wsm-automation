from selenium.webdriver.common.by import By


class TopPanelLocators:
    """A class for Shop's Top Panel locators"""

    ACCOUNT_BUTTON = (By.CSS_SELECTOR, ".wsm-hdr__pre a.wsm-hdr__btn--account")
    CART_BUTTON = (By.CSS_SELECTOR, ".cart_icon_counter_wrapper")
    CART_CONTENT_NUMBER = (By.CSS_SELECTOR, ".cart_icon_counter_wrapper > .cart_counter")
    CALL_NUMBER_LINK = (By.CSS_SELECTOR, "span.wsm-hdr__phone-num")
    SEARCH_INPUT = (By.CSS_SELECTOR, "#edit-keys")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "input.ast_search_btn")

    # Navigator Main Items Link generic locator. Note: Use MainNavigatorItems
    GENERIC_MAIN_ITEM_LINK = (By.CSS_SELECTOR, ".nav-main__link[title='$SHIPPING_METHOD$']")
