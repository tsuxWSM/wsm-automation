from ....main.wsm_admin.pages.customers_page import CustomersPage
from ....main.wsm_admin.pages.customer_edit_page import CustomerEditPage
from ....main.wsm_admin.pages.dashboard_page import DashboardPage
from ....main.wsm_admin.pages.sign_in_page import SignInAdminPage
from ....main.wsm_admin.pages.add_quote_page import AddQuotePage
from ....main.wsm_admin.pages.quote_builder_page import QuoteBuilderPage
from ....main.wsm_admin.pages.configuration_page import SiteInformationPanel
from ....main.wsm_admin.test_data.authentication_data_provider import AdminAuthenticationDataProvider


class AdminNavigationHelper:

    def __init__(self, driver):
        self.advanced_button = None
        self.driver = driver
        self.auth_data = AdminAuthenticationDataProvider()

    def from_sign_in_to_dashboard(self):
        init_page = SignInAdminPage(self.driver)
        data = self.auth_data

        init_page.sign_in(data.username, data.password)

        return DashboardPage(self.driver)

    def from_dashboard_to_system_configuration(self):
        init_page = DashboardPage(self.driver)
        init_page.system.hover()
        init_page.configuration_submenu.click()

        return SiteInformationPanel(self.driver)

    def from_sign_in_to_system_configuration(self):
        self.from_sign_in_to_dashboard()

        return self.from_dashboard_to_system_configuration()

    def from_dashboard_to_customers(self):
        init_page = DashboardPage(self.driver)
        init_page.customers.hover()
        init_page.customers_submenu.click()

        return CustomersPage(self.driver)

    def from_dashboard_to_add_quote(self):
        init_page = DashboardPage(self.driver)
        init_page.orders.hover()
        init_page.add_quote.click()

        return AddQuotePage(self.driver)

    def from_dashboard_to_quote_builder(self):
        init_page = DashboardPage(self.driver)
        init_page.orders.hover()
        init_page.quote_builder.click()

        return QuoteBuilderPage(self.driver)

    def from_customer_to_add_customer(self):
        init_page = CustomersPage(self.driver)

        init_page.add_customer_button_top.click()

        return CustomerEditPage(self.driver)

    def from_sign_in_to_customers(self):
        self.from_sign_in_to_dashboard()

        return self.from_dashboard_to_customers()

    def from_sign_in_to_add_customer(self):
        self.from_sign_in_to_dashboard()
        self.from_dashboard_to_customers()

        return self.from_customer_to_add_customer()

    def from_sign_in_to_add_quote(self):
        self.from_sign_in_to_dashboard()

        return self.from_dashboard_to_add_quote()
