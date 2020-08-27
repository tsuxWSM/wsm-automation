from selenium.webdriver.common.by import By


class Customers:
    """A class for Admin's Customers page locators"""

    TOP_ADD_CUSTOMER_BUTTON = (By.CSS_SELECTOR, "#search button.add_btn")
    TOP_EXPORT_BUTTON = (By.CSS_SELECTOR, "#search button.download_export_btn")

    EDIT_ICON = (By.CSS_SELECTOR, "a img[title='Edit']")
    IMPERSONATE_ICON = (By.CSS_SELECTOR, "a img[title='Impersonate']")
    DELETE_ICON = (By.CSS_SELECTOR, "a img[title='Delete']")

    BOTTOM_ADD_CUSTOMER_BUTTON = (By.CSS_SELECTOR, "tfoot button.add_btn")
    BOTTOM_EXPORT_BUTTON = (By.CSS_SELECTOR, "tfoot button.download_export_btn")

    NOTIFICATION_MESSAGE = (By.CSS_SELECTOR, "li.wsm_message")
