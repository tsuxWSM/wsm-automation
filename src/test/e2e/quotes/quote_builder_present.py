import pytest
import time
from ....main.utils.ui.admin_nav_helper import AdminNavigationHelper
from ....main.wsm_admin.pages.quote_builder_page import TestOption, QuoteStatus


@pytest.mark.usefixtures("webdriver")
class PresentElementQuoteAdminTestSuite:

    def prestep_navigate_quote(self):
        navigate = AdminNavigationHelper(self.driver)

        navigate.from_sign_in_to_dashboard()
        page = navigate.from_dashboard_to_quote_builder()

        assert page is not None

        page.advanced_search_button_click()
        page.select_test_option(TestOption.NO)
        page.select_test_option(TestOption.YES)
        page.select_test_option(TestOption.ANY)

        page.check_status(QuoteStatus.CANCELED)
        page.check_status(QuoteStatus.FRAUD)
        page.check_status(QuoteStatus.HELD)
        page.check_status(QuoteStatus.NEW)
        page.check_status(QuoteStatus.RETURN)
        page.check_status(QuoteStatus.BACKORDER)
        page.check_status(QuoteStatus.COMPLETE)
        page.check_status(QuoteStatus.DRAFT_OPEN)
        page.check_status(QuoteStatus.DELETED)
        page.check_status(QuoteStatus.EXPIRED)
        page.check_status(QuoteStatus.PENDING)
        page.check_status(QuoteStatus.PROCESSING)
        page.check_status(QuoteStatus.READY_TO_SHIP)
        page.check_status(QuoteStatus.SHIPPED)
        page.check_status(QuoteStatus.BUILDING)

        time.sleep(3)
