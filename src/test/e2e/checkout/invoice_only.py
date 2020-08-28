import pytest
from ....main.web_shop.pages.coverlay.home_page import HomePage
from ....main.web_shop.pages.coverlay.login_popup import LoginPopup
from ....main.web_shop.pages.coverlay.product_details_page import ProductDetailsPage
from ....main.wsm_admin.test_data.customer_data_provider import CustomerDataProvider
from ....main.web_shop.test_data.home_data_provider import HomeDataProvider
from ....main.web_shop.test_data.product_data_provider import ProductDetailsDataProvider
from ....main.web_shop.pages.page_factory import PageBuilder

_test_customer = CustomerDataProvider().customer_invoice_only
_test_product = ProductDetailsDataProvider().kit_10_5151C


@pytest.mark.usefixtures("webdriver")
@pytest.mark.incremental
class InvoiceOnlyCheckoutTestSuite:

    def setup_class(self):
        self.customer_data = CustomerDataProvider()
        self.home_data = HomeDataProvider()

    def prestep_customer_creation(self, create_customer):
        assert create_customer(self.driver, _test_customer, self.base_url)
        self.driver.get(self.base_url)

        customer = _test_customer

        page = HomePage(self.driver)
        page.account_button.click()

        page = LoginPopup(self.driver)
        page.customer_login(customer)

    def test_add_product_to_cart(self):
        data = self.home_data
        product = _test_product
        landing_page = HomePage(self.driver)

        assert landing_page.get_notification_message_element().get_text() == data.user_logged_in_message

        self.driver.get(self.base_url + product.direct_location)

        page = ProductDetailsPage(self.driver, product, _test_customer)

        assert page.is_text_present(product.title)
        page.add_to_cart_button.click()

    def test_navigate_to_cart(self):
        build_page = PageBuilder(self.site).get_factory()
        landing_page = build_page.cart(self.driver)

        assert landing_page.is_partial_text_present("My Cart")
        assert landing_page.is_text_present(_test_product.title)

        landing_page.scroll_up_to_element(landing_page.proceed_to_checkout_button)

        landing_page.proceed_to_checkout_button.click()

    def test_checkout_order_invoice(self):
        build_page = PageBuilder(self.site).get_factory()
        landing_page = build_page.checkout(self.driver, invoice_only=True, signed_user=True)
        landing_page.is_partial_text_present(_test_product.title)

    def teardown_suite(self, delete_customer):
        delete_customer(self.driver, _test_customer, self.base_url)
