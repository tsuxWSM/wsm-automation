from selenium.webdriver.common.by import By


class TechLicense:
    """A class for Tech License page locators"""

    SUMMARY_TITLE = (By.CSS_SELECTOR, ".wsm-ib h2")

    GENERIC_SEL_LASH = (By.XPATH, "//div[@class='wsm-ib']//li[text()='$LASH_TITLE$']")
    GENERIC_LASH_LINK = (By.XPATH, "//div[@class='wsm-ib']//a[text()='$LASH_TITLE$']")
