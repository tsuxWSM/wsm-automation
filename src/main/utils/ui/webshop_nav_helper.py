from ....main.wsm_admin.test_data.authentication_data_provider import AdminAuthenticationDataProvider


class WebShopNavigationHelper:

    def __init__(self, driver):
        self.driver = driver
        self.auth_data = AdminAuthenticationDataProvider()
