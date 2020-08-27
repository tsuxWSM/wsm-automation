import pytest
from ...main.wsm_admin.pages.customer_edit_page import CustomerEditPage
from ...main.wsm_admin.pages.customers_page import CustomersPage
from ...main.wsm_admin.test_data.customer_data_provider import CustomerDataProvider
from ...main.utils.ui.admin_nav_helper import AdminNavigationHelper

_test_customer = CustomerDataProvider().customer_inactive


@pytest.mark.usefixtures("webdriver")
@pytest.mark.incremental
class CreateCustomerAdminTestSuite:
    """NOTE: Only Working for CVL for now"""

    def setup_class(self):
        self.test_data = CustomerDataProvider()

    def test_create_customer(self):
        navigate = AdminNavigationHelper(self.driver)
        navigate.from_sign_in_to_add_customer()
        page = CustomerEditPage(self.driver)
        data = self.test_data

        assert page.active_user_true.is_checkbox_on()

        # Checks default Off value for following flag based fields
        assert page.invoice_false.is_checkbox_on() \
            and page.tax_exempt_false.is_checkbox_on() \
            and page.block_free_shipping_false.is_checkbox_on()

        # Check only Affirm is enable
        assert page.affirm_true.is_checkbox_on()

        page.create_new_user(_test_customer)

        # Check for user successfully create notification message
        landing_page = CustomersPage(self.driver)
        assert landing_page.get_notification_message_element().get_text() == data.created_user_message

    def test_edit_customer(self):
        page = CustomersPage(self.driver)
        page.search_customer(_test_customer.email)
        page.edit_icon.click()

        landing_page = CustomerEditPage(self.driver)

        landing_page.active_user_true.click()

        landing_page.save_button.click()

    def test_delete_customer(self):
        page = CustomersPage(self.driver)
        page.search_customer(_test_customer.email)
        page.delete_icon.click()

        self.driver.switch_to.alert.accept()

        landing_page = CustomersPage(self.driver)

        landing_page.search_customer(_test_customer.email)

        assert landing_page.is_partial_text_present(self.test_data.no_results_message)
        assert landing_page.is_text_present(self.test_data.clear_search_message)
