from ....main.utils.data_handlers import DateTimeHandler
from ...data_model.customer import Customer
from ...data_model.product import Product


class QuoteDataProvider:
    """Test Data and Strings Providers for Quote Builder and Add Quote"""

    def __init__(self):
        self.user = Customer("Tsune", "Maldonado", "tsune@webshopmanager.com", "tsux75", 1231, "06/03/1990")
        self.regular_product = Product("11360655", "Coverlay 10-282-BLK Dash Cover", 123.23,
                                       "/i-11360655-coverlay-10-282-blk-dash-cover.html")
        self.virtual_product = Product("1212", "Virtual Item", 21.99)

        self.expiration_date = DateTimeHandler.get_future_date_usa_format()
        self.expired_date = DateTimeHandler.get_past_date_usa_format()
