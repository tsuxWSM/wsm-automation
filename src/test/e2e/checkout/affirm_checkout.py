import pytest
from ....main.utils.ui.admin_nav_helper import AdminNavigationHelper
from ....main.wsm_admin.pages.customer_edit_page import CustomerEditPage
from ....main.wsm_admin.pages.customers_page import CustomersPage
from ....main.web_shop.pages.coverlay.home_page import HomePage
from ....main.web_shop.pages.coverlay.login_popup import LoginPopup
from ....main.web_shop.pages.coverlay.product_details_page import ProductDetailsPage
from ....main.wsm_admin.test_data.customer_data_provider import CustomerDataProvider
from ....main.web_shop.test_data.home_data_provider import HomeDataProvider
from ....main.web_shop.test_data.product_data_provider import Product, ProductDetailsDataProvider


_test_customer = CustomerDataProvider().customer_default
# Test Data for Items only working with CVL site for now
_test_product_1 = ProductDetailsDataProvider().kit_18_714C
_test_product_2 = ProductDetailsDataProvider().kit_10_5151C
_cart_products = []


@pytest.mark.usefixtures("webdriver")
@pytest.mark.incremental
class AffirmAvailabilityCheckoutTestSuite:

    def setup_class(self):
        self.customer_data = CustomerDataProvider()
        self.home_data = HomeDataProvider()

    def prestep_customer_creation(self, create_customer):
        assert create_customer(self.driver, _test_customer, self.base_url)
        self.driver.get(self.base_url)

    def test_sign_in_with_recently_created_customer_affirm_allowed(self):
        customer = _test_customer
        data = self.home_data

        page = HomePage(self.driver)

        page.account_button.click()

        page = LoginPopup(self.driver)
        page.customer_login(customer)

        landing_page = HomePage(self.driver)
        assert landing_page.get_notification_message_element().get_text() == data.user_logged_in_message

    @pytest.mark.parametrize("product", [_test_product_1, pytest.param(_test_product_2, marks=pytest.mark.xfail)])
    def test_affirm_appears(self, product: Product):
        self.driver.get(self.base_url + product.direct_location)

        page = ProductDetailsPage(self.driver, product, _test_customer)

        assert page.is_text_present(product.title)

        assert page.is_text_present(ProductDetailsDataProvider().get_affirm_link_message_string()),\
            "Affirm Link is not displayed"

    def test_switch_user_affirm_not_allowed(self):
        self.driver.get(self.base_url + "/admin")

        navigate = AdminNavigationHelper(self.driver)
        customers_page = navigate.from_dashboard_to_customers()
        customers_page.search_customer(_test_customer.email)
        customers_page.edit_icon.click()

        landing_page = CustomerEditPage(self.driver)

        landing_page.affirm_false.click()
        _test_customer.affirm_allowed = False

        assert landing_page.affirm_false.is_checkbox_on()

        landing_page.save_button.click()

    def test_impersonate_customer(self):
        page = CustomersPage(self.driver)
        page.search_customer(_test_customer.email)
        page.impersonate_icon.click()

        page.switch_to_window(0)

    def test_affirm_not_shown(self):
        self.driver.get(self.base_url + _test_product_1.direct_location)

        page = ProductDetailsPage(self.driver, _test_product_1, _test_customer)

        assert page.is_text_present(_test_product_1.title)

        assert page.affirm_link is None

    def teardown_suite(self, delete_customer):
        delete_customer(self.driver, _test_customer, self.base_url)
