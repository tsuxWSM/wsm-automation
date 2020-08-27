from selenium.webdriver.common.by import By


class TopPanelLocators:
    """Locator for Extreme Metal Products Top Panel"""

    MENU_POLARIS = (By.CSS_SELECTOR, "#widget_fnd_cat_menu > li > a[title='Polaris']")
    MENU_ARCTIC_CART = (By.CSS_SELECTOR, "#widget_fnd_cat_menu > li > a[title='Arctic Cat']")
    MENU_CAN_AM = (By.CSS_SELECTOR, "#widget_fnd_cat_menu > li > a[title='Can-Am']")
    MENU_CF_MOTO = (By.CSS_SELECTOR, "#widget_fnd_cat_menu > li > a[title='CF Moto']")
    MENU_HONDA = (By.CSS_SELECTOR, "#widget_fnd_cat_menu > li > a[title='Honda']")
    MENU_JOHN_DEERE = (By.CSS_SELECTOR, "#widget_fnd_cat_menu > li > a[title='John Deere']")
    MENU_KAWASAKI = (By.CSS_SELECTOR, "#widget_fnd_cat_menu > li > a[title='Kawasaki']")
    MENU_KUBOTA = (By.CSS_SELECTOR, "#widget_fnd_cat_menu > li > a[title='Kubota']")
    MENU_MAHINDRA = (By.CSS_SELECTOR, "#widget_fnd_cat_menu > li > a[title='Mahindra']")
    MENU_YAMAHA = (By.CSS_SELECTOR, "#widget_fnd_cat_menu > li > a[title='Yamaha']")

    SUBMENU_GENERIC = (By.CSS_SELECTOR, "a[title='$SUBMENU$']")