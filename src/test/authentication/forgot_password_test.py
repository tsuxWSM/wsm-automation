import pytest
from ...main.utils.ui.web_element import Expectation
from ...main.wsm_admin.pages.forgot_password_page import ForgotPasswordAdminPage
from ...main.wsm_admin.pages.sign_in_page import SignInAdminPage
from ...main.wsm_admin.test_data.authentication_data_provider import AdminAuthenticationDataProvider


@pytest.mark.incremental
@pytest.mark.usefixtures("webdriver")
class ForgotPasswordAdminTestSuite:

    def setup(self):
        self.test_data = AdminAuthenticationDataProvider()

    def verify_wrong_password(self):
        page = SignInAdminPage(self.driver)
        data = self.test_data

        page.sign_in(data.username, data.wrong_password)

        error_message = page.get_error_message_element()
        error_message.safety_get_element_by(Expectation.VISIBILITY)

        assert error_message.get_text() == data.invalid_creds_error_message_string

    def test_forgot_password(self):
        page = SignInAdminPage(self.driver)
        data = self.test_data

        page.forgot_pw_link.click()

        landing_page = ForgotPasswordAdminPage(self.driver)

        assert landing_page.is_text_present(data.email_label_string)

        landing_page.email_input.__set__(data.email)
        landing_page.next_button.click()

        forgot_landing_page = SignInAdminPage(self.driver)
        error_message = forgot_landing_page.get_notification_message_element()

        assert error_message.get_text() == data.email_notification_message
