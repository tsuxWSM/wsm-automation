class Product:
    """Product model class for test data management"""

    def __init__(self, sku: str, name: str, price: float, direct_location: str = ""):
        self.sku = sku
        self.title = name
        self.price = str(price)
        self.direct_location = direct_location
