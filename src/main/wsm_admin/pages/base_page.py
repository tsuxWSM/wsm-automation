from selenium.webdriver.remote.webdriver import WebDriver
from .locators.search_panel import SearchPanel
from .locators.top_panel import TopPanelLocators
from ...utils.ui.base_page import GlobalBasePage
from ...utils.ui.web_element import BaseWebElement
from ...utils.ui.web_element import VisualWebElement


class BaseAdminPage(GlobalBasePage):
    """Base class to initialize all Admin Panel's Page Objects, should be called from all pages under same module"""

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

        self.logo_link = VisualWebElement(driver, TopPanelLocators.WSM_LOGO)


class AdminTopPanel(BaseAdminPage):
    """A Page Object for Top Menu and its submenus representation"""

    def __init__(self, driver):
        super().__init__(driver)

        # User Account Bar
        self.dashboard_link = VisualWebElement(driver, TopPanelLocators.DASHBOARD_LINK)
        self.my_account_link = VisualWebElement(driver, TopPanelLocators.MY_ACCOUNT_LINK)
        self.support_request_link = VisualWebElement(driver, TopPanelLocators.SUPPORT_REQUEST_LINK)
        self.logout_link = VisualWebElement(driver, TopPanelLocators.LOGOUT_LINK)

        # Notifications Bar
        self.site_bounce_dropdown = VisualWebElement(driver, TopPanelLocators.SITE_BOUNCE_MENU)
        self.new_orders_link = VisualWebElement(driver, TopPanelLocators.NEW_ORDERS_LINK)
        # TODO: Check which configuration does this sub menu presence depend on
        # self.new_reviews_link = VisualWebElement(driver, TopPanelLocators.NEW_REVIEWS_LINK)
        self.inbox_link = VisualWebElement(driver, TopPanelLocators.INBOX_LINK)
        self.outbox_link = VisualWebElement(driver, TopPanelLocators.OUTBOX_LINK)

        # Admins main Menu Bar
        self.orders = VisualWebElement(driver, TopPanelLocators.MENU_ORDERS)
        self.catalogs = VisualWebElement(driver, TopPanelLocators.MENU_CATALOGS)
        self.modules = VisualWebElement(driver, TopPanelLocators.MENU_MODULES)
        self.content = VisualWebElement(driver, TopPanelLocators.MENU_CONTENT)
        self.customers = VisualWebElement(driver, TopPanelLocators.MENU_CUSTOMERS)
        self.reports = VisualWebElement(driver, TopPanelLocators.MENU_REPORTS)
        self.data = VisualWebElement(driver, TopPanelLocators.MENU_DATA)
        self.system = VisualWebElement(driver, TopPanelLocators.MENU_SYSTEM)

        self.active_submenu = VisualWebElement(driver, TopPanelLocators.ACTIVE_SUBMENU)

        # Order submenus
        self.quote_builder = BaseWebElement(driver, TopPanelLocators.SUBMENU_QUOTE_BUILDER)
        self.add_quote = BaseWebElement(driver, TopPanelLocators.SUBMENU_ADD_QUOTE)

        # Customer submenus
        self.customers_submenu = BaseWebElement(driver, TopPanelLocators.SUBMENU_CUSTOMERS)

        # System Submenus
        self.configuration_submenu = BaseWebElement(driver, TopPanelLocators.SUBMENU_CONFIGURATION)


class SearchBar(AdminTopPanel):
    """A Page Object for Search Bar representation"""

    def __init__(self, driver):
        super().__init__(driver)

        self.search_input = VisualWebElement(driver, SearchPanel.SEARCH_INPUT)
        self.search_button = VisualWebElement(driver, SearchPanel.SEARCH_BUTTON)
        self.advanced_button = VisualWebElement(driver, SearchPanel.ADVANCED_BUTTON)
