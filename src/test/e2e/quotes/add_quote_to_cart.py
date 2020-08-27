import pytest
import time
from ....main.data_model.quote import Quote
from ....main.wsm_admin.test_data.quote_data_provider import QuoteDataProvider
from ....main.web_shop.pages.cart_page import CartPage
from ....main.utils.ui.admin_nav_helper import AdminNavigationHelper
from ....main.wsm_admin.pages.add_quote_page import AddQuotePage


@pytest.mark.usefixtures("webdriver")
class LoadQuoteToCartAdminTestSuite:

    def setup_class(self):
        self.test_data = QuoteDataProvider()

    def prestep_navigate(self):
        navigate = AdminNavigationHelper(self.driver)

        navigate.from_sign_in_to_add_quote()

    # @pytest.mark.xfail
    def test_create_quote_expired_date(self):
        test_data = self.test_data
        page = AddQuotePage(self.driver)

        page.customer_input.__set__(test_data.user.name)
        page.email_address_input.__set__(test_data.user.email)

        # sets expired Quote
        # page.expires_input.__set__(self.test_data.expired_date)
        page.expires_input.__set__(test_data.expiration_date)

        page.scroll_down()

        page.search_item(test_data.regular_product)

        page.add_custom_item()
        page.fill_item_title(test_data.virtual_product.title, 1)
        page.fill_item_sku(test_data.virtual_product.sku, 1)
        page.set_item_price(test_data.virtual_product.price, 1)

        page.shipping_input.manually_clear()
        page.shipping_input.__set__("12.00")

        page.create_quote_action()

        assert page.is_text_present("Load quote --> cart")

    def test_load_to_cart(self):
        test_data = self.test_data
        page = AddQuotePage(self.driver, True)

        quote = Quote(page.get_quote_number_from_title(), [test_data.regular_product, test_data.virtual_product],
                      total_amount_due=page.total_amount_due.get_amount(),
                      shipping_price=page.shipping_input.get_input_value(),
                      total=page.grand_total.get_amount())

        page.enable_quote_actions()

        page.load_to_cart_link.click()

        landing_page = CartPage(self.driver, quote, user_lands_from_admin=True)
        assert landing_page is not None

        time.sleep(12)
        # page.create_quote_button.click()
