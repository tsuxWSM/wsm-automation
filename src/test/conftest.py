import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from ..main.data_model.customer import Customer
from ..main.wsm_admin.test_data.customer_data_provider import CustomerDataProvider
from ..main.wsm_admin.pages.customer_edit_page import CustomerEditPage
from ..main.wsm_admin.pages.customers_page import CustomersPage
from ..main.utils.ui.admin_nav_helper import AdminNavigationHelper


@pytest.fixture(name="create_customer")
def create_customer():
    """Factory Fixture: Test Customer creation"""

    def _create_customer(driver: WebDriver, test_customer: Customer, base_url: str):
        """Creates a customer based on Customer Object information
        :param driver - WebDriver from Test Class
        :param test_customer - Defines test customer to be created (Customer type required)
        :param base_url - Site's base URL for which customer is expected to be created
        """
        customer_data = CustomerDataProvider()

        driver.get(base_url + "/admin")

        navigate = AdminNavigationHelper(driver)
        navigate.from_sign_in_to_add_customer()

        page = CustomerEditPage(driver)

        # Check only Active and Affirm Allowed flags are enable
        assert page.active_user_true.is_checkbox_on() and page.affirm_true.is_checkbox_on()

        assert page.invoice_false.is_checkbox_on() \
            and page.tax_exempt_false.is_checkbox_on() \
            and page.block_free_shipping_false.is_checkbox_on()

        page.create_new_user(test_customer)

        landing_page = CustomersPage(driver)

        if landing_page.get_notification_message_element().get_text() == customer_data.created_user_message:
            return True
        else:
            return False

    return _create_customer


@pytest.fixture(name="delete_customer")
def delete_customer():
    """Factory Fixture: Test Customer deletion"""

    def _delete_customer(driver: WebDriver, test_customer: Customer, base_url: str):
        """Deleted a customer that's been used for test purposes
        :param driver - WebDriver from Test Class
        :param test_customer - test customer to be deleted (Customer type required)
        :param base_url - Site's base URL for which customer is expected to be deleted
        """
        customer_data = CustomerDataProvider()

        driver.get(base_url + "/admin")
        navigate = AdminNavigationHelper(driver)

        navigate.from_dashboard_to_customers()
        customers_page = CustomersPage(driver)
        # Move below
        customers_page.search_customer(test_customer.email)
        customers_page.delete_icon.click()

        driver.switch_to.alert.accept()

        landing_page = CustomersPage(driver)
        if landing_page.get_notification_message_element().get_text() == customer_data.deleted_user_message:
            return True
        else:
            return False

    return _delete_customer
