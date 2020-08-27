from selenium.webdriver.common.by import By


class DashboardLocators:
    """A class for Dashboard page locators"""
    VISIBLE_TABBED_PANEL = (By.CSS_SELECTOR, ".TabbedPanelsContentVisible .chartjs-render-monitor")

    # Active Submenus
    ACTIVE_DASHBOARD = (By.CSS_SELECTOR, "#wsma_sub_menu a[title='WSM News']")
    ACTIVE_TECH_LICENSE = (By.CSS_SELECTOR, "#wsma_sub_menu a[title='Tech License']")
