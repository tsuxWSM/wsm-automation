from .base_page import AdminTopPanel
from ...utils.ui.web_element import BaseWebElement
from .locators.dashboard import DashboardLocators


class DashboardPage(AdminTopPanel):
    """A Page Object for Admin's Dashboard Page"""

    def __init__(self, driver):
        super().__init__(driver)

        self.dashboard_submenu = BaseWebElement(driver, DashboardLocators.ACTIVE_DASHBOARD)
        self.tech_license_submenu = BaseWebElement(driver, DashboardLocators.ACTIVE_TECH_LICENSE)

        self.tabbed_panel = BaseWebElement(driver, DashboardLocators.VISIBLE_TABBED_PANEL)
