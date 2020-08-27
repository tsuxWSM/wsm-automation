from selenium.webdriver.remote.webdriver import WebDriver
from ....utils.ui.base_page import GlobalBasePage
from ....utils.ui.web_element import VisualWebElement
from .locators.top_panel import TopPanelLocators
from .locators.search_panel import SearchPanelLocators


class TopPanelSection(GlobalBasePage):
    """Page Object for Top Panel Section"""

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

        self.menu_polaris = VisualWebElement(driver, TopPanelLocators.MENU_POLARIS)
        self.menu_arctic_cart = VisualWebElement(driver, TopPanelLocators.MENU_ARCTIC_CART)
        self.menu_can_am = VisualWebElement(driver, TopPanelLocators.MENU_CAN_AM)
        self.menu_cf_moto = VisualWebElement(driver, TopPanelLocators.MENU_CF_MOTO)
        self.menu_honda = VisualWebElement(driver, TopPanelLocators.MENU_HONDA)
        self.menu_john_deere = VisualWebElement(driver, TopPanelLocators.MENU_JOHN_DEERE)
        self.menu_kawasaki = VisualWebElement(driver, TopPanelLocators.MENU_KAWASAKI)
        self.menu_kubota = VisualWebElement(driver, TopPanelLocators.MENU_KUBOTA)
        self.menu_mahindra = VisualWebElement(driver, TopPanelLocators.MENU_KUBOTA)
        self.menu_yamaha = VisualWebElement(driver, TopPanelLocators.MENU_KUBOTA)


class SearchPanelSection(TopPanelSection):
    """Page Object for Search Panel Section"""

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

        self.logo_link = VisualWebElement(driver, SearchPanelLocators.LOGO_LINK)
        self.bar_search_input = VisualWebElement(driver, SearchPanelLocators.BAR_SEARCH_INPUT)
        self.call_us_link = VisualWebElement(driver, SearchPanelLocators.CALL_US_LINK)
        self.dealer_locator_link = VisualWebElement(driver, SearchPanelLocators.DEALER_LOCATOR_LINK)
