from ...data_model.product import Product


class ProductDetailsDataProvider:
    """Test Products Data and String Providers"""

    def __init__(self):
        """Initialize ProductDetails page data provider with a few test Products"""
        self.kit_18_714C = Product("18-714C-NTL", "Coverlay 18-714C-NTL Interior Accessories Kit", 255.52,
                                   direct_location="/i-23897318-coverlay-18-714c-ntl-interior-accessories-kit.html#"
                                                   "!year%3D2014%7C%7Cmake%3DCADILLAC%7C%7Cmodel%3DESCALADE")
        self.kit_10_5151C = Product("10-515IC-BLK", "Coverlay 10-515IC-BLK Instrument Panel Cover", 131.77,
                                    direct_location="/i-23897946-coverlay-10-515ic-blk-instrument-panel-cover.html#"
                                                    "!year%3D2012%7C%7Cmake%3DNISSAN%7C%7Cmodel%3DTITAN")

    @staticmethod
    def get_affirm_link_message_string():
        return "Affirm"
