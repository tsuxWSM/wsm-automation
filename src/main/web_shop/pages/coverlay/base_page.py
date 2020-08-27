from enum import Enum
from selenium.webdriver.remote.webdriver import WebDriver
from ....utils.ui.base_page import GlobalBasePage
from ....utils.ui.web_element import VisualWebElement
from .locators.top_panel import TopPanelLocators
from .locators.search_panel import SearchPanelLocators


class BaseShopPage(GlobalBasePage):
    """Base class to initialize all Web Shop's Page Objects, should be called from all pages under same module"""

    def __init__(self, driver: WebDriver):
        super().__init__(driver)


class MainNavigatorItems(Enum):
    COMBO_KITS = "Combo Kits"
    KICK_PANELS = "Kick Panels"
    DASH_COVERS = "Dash Covers"
    DOOR_PANELS = "Door Panels"
    ARM_RESTS = "Arm Rests"
    DOOR_PANEL_INSERTS = "Door Panel Inserts"
    INSTRUMENT_PANEL_COVERS = "Instrument Panel Covers"


class TopPanelSection(BaseShopPage):
    """Page Object for Top Panel Section"""

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

        self.account_button = VisualWebElement(driver, TopPanelLocators.ACCOUNT_BUTTON)
        self.cart_button = VisualWebElement(driver, TopPanelLocators.CART_BUTTON)
        self.cart_content = VisualWebElement(driver, TopPanelLocators.CART_CONTENT_NUMBER)
        self.call_number_link = VisualWebElement(driver, TopPanelLocators.CALL_NUMBER_LINK)
        self.search_input = VisualWebElement(driver, TopPanelLocators.SEARCH_INPUT)
        self.search_button = VisualWebElement(driver, TopPanelLocators.SEARCH_BUTTON)

    def click_main_nav_item_link(self, item_title: MainNavigatorItems):
        var_template = "$ITEM_TITLE$"
        locator = TopPanelLocators.GENERIC_MAIN_ITEM_LINK[0], \
            TopPanelLocators.GENERIC_MAIN_ITEM_LINK[1].replace(var_template, item_title)
        VisualWebElement(self.driver, locator).click()


class SearchPanelSection(TopPanelLocators):
    """Page Object for Search Panel Section"""

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

        self.logo_link = VisualWebElement(driver, SearchPanelLocators.LOGO_LINK)
        self.bar_search_input = VisualWebElement(driver, SearchPanelLocators.BAR_SEARCH_INPUT)
        self.search_button = VisualWebElement(driver, SearchPanelLocators.SEARCH_BUTTON)
        self.call_us_link = VisualWebElement(driver, SearchPanelLocators.CALL_US_LINK)
        self.chat_link = VisualWebElement(driver, SearchPanelLocators.CHAT_LINK)
