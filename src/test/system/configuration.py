import pytest
from ...main.utils.ui.admin_nav_helper import AdminNavigationHelper
import time
from ...main.wsm_admin.pages.configuration_page import CurrencyCodeOption, LanguageOption, \
    OrderUpdateRedirect, ResultsPerPageInMyOrders, SubmissionLimit


@pytest.mark.usefixtures("webdriver")
class PresentElementSystemAdminTestSuite:

    def prestep_navigate_system_configuration(self):
        navigate = AdminNavigationHelper(self.driver)

        page = navigate.from_sign_in_to_system_configuration()

        assert page is not None

        page.select_currency_code_option(CurrencyCodeOption.PESO)
        page.select_currency_code_option(CurrencyCodeOption.DOLAR_CAD)
        page.select_currency_code_option(CurrencyCodeOption.DOLAR)

        page.select_language_option(LanguageOption.SPA)
        page.select_language_option(LanguageOption.ENG)

        time.sleep(4)

        landing_page = page.go_to_general()
        landing_page.select_order_update_redirect_option(OrderUpdateRedirect.REDIRECT_TO_THE_ALL_ORDERS_LIST)
        landing_page.select_results_per_page_in_my_orders_option(ResultsPerPageInMyOrders.TEN)
        landing_page.select_submission_limit_option(SubmissionLimit.FIFTEEN)

        site_page = landing_page.go_to_site_information()
        assert site_page is not None

        time.sleep(3)
