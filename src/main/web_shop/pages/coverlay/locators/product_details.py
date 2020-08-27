from selenium.webdriver.common.by import By


class ProductDetailsLocators:
    """A class for Product Details page locators"""

    PRODUCT_TITLE = (By.CSS_SELECTOR, "h1.wsm-prod-title")
    PRODUCT_SKU = (By.CSS_SELECTOR, "#wsm-prod-info-container span.wsm-prod-sku")
    REVIEWS_LINK = (By.CSS_SELECTOR, "a[title='Write a Review']")
    PRODUCT_SUMMARY = (By.CSS_SELECTOR, "div p.dci-prod-sum")
    PRODUCT_IMAGE_ROTATOR_LINK = (By.CSS_SELECTOR, "#wsm-prod-rotate a")
    PRICE = (By.CSS_SELECTOR, "span.wsmjs-product-price")

    ITEM_INQUIRY_LINK = (By.CSS_SELECTOR, "button.wsm-inquiry-button")
    TELL_A_FRIEND_LINK = (By.CSS_SELECTOR, "button.wsm-tellafriend-button")

    QUANTITY_INPUT = (By.CSS_SELECTOR, "input.wsm-prod-qty-field")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.wsm-addtocart-button")

    # affirm links
    AFFIRM_LINK = (By.CSS_SELECTOR, "a.affirm-modal-trigger")
    AFFIRM_LOGO = (By.CSS_SELECTOR, "span.__affirm-logo")
