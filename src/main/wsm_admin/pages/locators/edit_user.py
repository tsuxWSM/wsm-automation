from selenium.webdriver.common.by import By


class EditUsePage:

    FORM_TITLE = (By.CSS_SELECTOR, ".title th")
    USER_NAME_INPUT = (By.CSS_SELECTOR, "#login")
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "#first_name")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "#last_name")
    TITLE_DROPDOWN = (By.CSS_SELECTOR, "select#title")
    INITIAL_INPUT = (By.CSS_SELECTOR, "#initial")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#email")
    STATUS_DROPDOWN = (By.CSS_SELECTOR, "select#status")
    PERMISSIONS_TABLE = (By.CSS_SELECTOR, "#permissions table")

    # TODO: Check on id codes persistance (like Auto Shop -> 455 Truck Accesories -> 1524)
    PERMISSION_CHECKBOX = (By.CSS_SELECTOR, "access_$ACCESS_CODE$")
    PERMISSION_DROPDOWN = (By.CSS_SELECTOR, "permission_$PERMISSION_CODE$")
    PERMISSION_CHECKBOX_2 = \
        (By.XPATH, "//label[contains (text(), '$PERMISSION$')]/parent::td/preceding-sibling::td/input")
    PERMISSION_DROPDOWN_2 = \
        (By.CSS_SELECTOR, "//label[contains (text(), '$PERMISSION$')]/parent::td/following-sibling::td/select")

    ADMIN_DROPDOWN = (By.CSS_SELECTOR, "#admin")
    SEND_MAIL_CHECKBOX = (By.CSS_SELECTOR, "input#sendemail")
    SAVE_BUTTON = (By.CSS_SELECTOR, "input#action")
