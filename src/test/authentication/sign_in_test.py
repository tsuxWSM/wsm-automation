import pytest
from ...main.wsm_admin.test_data.authentication_data_provider import AdminAuthenticationDataProvider
from ...main.wsm_admin.pages.dashboard_page import DashboardPage
from ...main.wsm_admin.pages.forgot_password_page import ForgotPasswordAdminPage
from ...main.wsm_admin.pages.sign_in_page import SignInAdminPage
from ...main.wsm_admin.pages.tech_license_page import TechLicensePage, Lash


@pytest.mark.usefixtures("webdriver")
@pytest.mark.incremental
class SignInAdminTestSuite:

    def setup_class(self):
        self.test_data = AdminAuthenticationDataProvider()

    def test_sign_in(self):
        page = SignInAdminPage(self.driver)
        data = self.test_data

        page.sign_in(data.username, data.password)

        landing_page = DashboardPage(self.driver)
        assert landing_page is not None

    def test_sign_out(self):
        page = DashboardPage(self.driver)
        data = self.test_data

        page.logout_link.click()

        landing_page = SignInAdminPage(self.driver)
        assert landing_page.login_title.get_text() == data.login_title_string

    def test_navigate_back_by_return(self):
        page = SignInAdminPage(self.driver)
        page.forgot_pw_link.click()
        data = self.test_data

        landing_page = ForgotPasswordAdminPage(self.driver)

        assert landing_page.title_header.get_text() == data.forgot_password_title_string
        assert landing_page.email_label.get_text() == data.email_label_string
        landing_page.return_link.click()

        back_landing_page = SignInAdminPage(self.driver)

        assert back_landing_page.login_title.get_text() == data.login_title_string

    def test_navigate_back_by_logo(self):
        page = SignInAdminPage(self.driver)
        page.forgot_pw_link.click()
        data = self.test_data

        landing_page = ForgotPasswordAdminPage(self.driver)

        assert landing_page.title_header.get_text() == data.forgot_password_title_string
        assert landing_page.email_label.get_text() == data.email_label_string
        landing_page.logo_link.click()

        back_landing_page = SignInAdminPage(self.driver)

        assert back_landing_page.login_title.get_text() == data.login_title_string

    def test_tech_license_navigation_from_login(self):
        page = SignInAdminPage(self.driver)
        page.forgot_pw_link.click()
        data = self.test_data

        landing_page = ForgotPasswordAdminPage(self.driver)

        landing_page.dashboard_menu.hover()
        landing_page.tech_license_submenu.click()

        back_landing_page = SignInAdminPage(self.driver)

        assert back_landing_page.login_title.get_text() == data.login_title_string

        back_landing_page.sign_in(data.username, data.password)

        login_landing_page = TechLicensePage(self.driver)

        assert login_landing_page.summary_title.get_text() == Lash.SUMMARY.value
