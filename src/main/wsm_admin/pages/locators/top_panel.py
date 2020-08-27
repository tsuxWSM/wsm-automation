from selenium.webdriver.common.by import By


class TopPanelLocators:
    """A class for Admin's Top Panel section locators"""

    WSM_LOGO = (By.CSS_SELECTOR, "#wsma_logo")

    # User Account Panel
    DASHBOARD_LINK = (By.CSS_SELECTOR, ".top_dashboard a[title='My Dashboard']")
    MY_ACCOUNT_LINK = (By.CSS_SELECTOR, "a[title='My Account']")
    SUPPORT_REQUEST_LINK = (By.CSS_SELECTOR, "a[title='Report Bug']")
    LOGOUT_LINK = (By.CSS_SELECTOR, "a[title='Logout']")

    # Right Top Panel
    SITE_BOUNCE_MENU = (By.CSS_SELECTOR, ".wsm_quick_bounce_menu")
    NEW_ORDERS_LINK = (By.CSS_SELECTOR, ".wsma_menu_horz a[title='See All New Orders']")
    NEW_REVIEWS_LINK = (By.CSS_SELECTOR, ".wsma_menu_horz a[title='See New Reviews']")
    INBOX_LINK = (By.CSS_SELECTOR, ".wsma_menu_horz a[title='List all new inquiries']")
    OUTBOX_LINK = (By.CSS_SELECTOR, ".wsma_menu_horz a[title='List all open inquiries']")

    # Admins main Menu sections
    MENU_ORDERS = (By.CSS_SELECTOR, "#MenuBar1 a[title='My Orders']")
    MENU_CATALOGS = (By.CSS_SELECTOR, "#MenuBar1 a[title='Store Catalog")
    MENU_MODULES = (By.CSS_SELECTOR, "#MenuBar1 a[title^='WSM Content']")
    MENU_CONTENT = (By.CSS_SELECTOR, "#MenuBar1 a[title^='Content']")
    MENU_CUSTOMERS = (By.CSS_SELECTOR, "#MenuBar1 a[title^='Customer']")
    MENU_REPORTS = (By.CSS_SELECTOR, "#MenuBar1 a[title^='Site Reports']")
    MENU_DATA = (By.CSS_SELECTOR, "#MenuBar1 a[title='Data']")
    MENU_SYSTEM = (By.CSS_SELECTOR, "#MenuBar1 a[title^='System Settings']")

    # Active Submenu
    ACTIVE_SUBMENU = (By.CSS_SELECTOR, "#wsma_sub_menu")

    # Dashboard Submenu Sections
    SUBMENU_TECH_LICENSE = (By.CSS_SELECTOR, "#MenuBar1 a[title='Tech License']")
    SUBMENU_DASHBOARD = (By.CSS_SELECTOR, "#MenuBar1 a[title='WSM News']")

    # Order Submenu Sections
    SUBMENU_QUOTE_BUILDER = (By.CSS_SELECTOR, "#MenuBar1 a[title='See Quotes (Beta)']")
    SUBMENU_ADD_QUOTE = (By.CSS_SELECTOR, "#MenuBar1 a[title='Add Quote (Beta)']")

    # Customer Submenu Sections
    SUBMENU_CUSTOMERS = (By.CSS_SELECTOR, "#MenuBar1 a[title='See All Customers']")

    # System Submenu Sections
    SUBMENU_CONFIGURATION = (By.CSS_SELECTOR, "#MenuBar1 a[title='Site / Store Configuration']")
