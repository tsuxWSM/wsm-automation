from enum import Enum
from .base_page import AdminTopPanel
from .locators.tech_license import TechLicense
from ...utils.ui.web_element import VisualWebElement


class Lash(Enum):
    SUMMARY = "Summary"
    SESSIONS = "Sessions"
    BANDWIDTH = "Bandwidth"
    PRODUCTS = "Products"
    HOURS = "Hours"
    SALES = "Sales"


class TechLicensePage(AdminTopPanel):
    """A Page Object for Admin's Tech License Page"""

    def __init__(self, driver):
        super().__init__(driver)

        self.active_lash_title = Lash.SUMMARY

        self.summary_title = VisualWebElement(driver, TechLicense.SUMMARY_TITLE)
        self.selected_lash = VisualWebElement(driver, self.get_selected_lash_locator_by_title(self.active_lash_title))

        self.summary_lash = None
        self.sessions_lash = VisualWebElement(driver, self.get_lash_locator_by_title(Lash.SESSIONS))
        self.bandwidth_lash = VisualWebElement(driver, self.get_lash_locator_by_title(Lash.BANDWIDTH))
        self.products_lash = VisualWebElement(driver, self.get_lash_locator_by_title(Lash.PRODUCTS))
        self.hours_lash = VisualWebElement(driver, self.get_lash_locator_by_title(Lash.HOURS))
        self.sales_lash = VisualWebElement(driver, self.get_lash_locator_by_title(Lash.SALES))

    @staticmethod
    def get_lash_locator_by_title(lash_title: Lash):
        var_template = "$LASH_TITLE$"
        return TechLicense.GENERIC_LASH_LINK[0], \
            TechLicense.GENERIC_LASH_LINK[1].replace(var_template, lash_title.value)

    @staticmethod
    def get_selected_lash_locator_by_title(lash_title: Lash):
        var_template = "$LASH_TITLE$"
        return TechLicense.GENERIC_SEL_LASH[0], TechLicense.GENERIC_SEL_LASH[1].replace(var_template, lash_title.value)

    def switch_to_lash(self, lash_title: Lash):
        """Switch to a different lash updating @select_lash attribute and creating link elment for las active lash"""
        # TODO: Implement/extend proper logic for this method
        last_active_lash_title = self.selected_lash.get_text()
        self.selected_lash = VisualWebElement(self.driver, self.get_selected_lash_locator_by_title(lash_title))

        if lash_title == Lash.SUMMARY:
            self.summary_lash = VisualWebElement(self.driver, self.get_lash_locator_by_title(last_active_lash_title))
