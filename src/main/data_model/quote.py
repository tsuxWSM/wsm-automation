class Quote:

    def __init__(self, quote_number: int, products: list, shipping_method: str = "", total_amount_due: float = 0.0,
                 tax: float = float, shipping_price: float = 0.0, handling_price: float = 0.0, total: float = 0.0):
        self.quote_number = str(quote_number)
        self.products = products
        self.shiping_method = shipping_method
        self.total_amount_due = total_amount_due
        self.sales_tax = tax
        self.shipping_price = shipping_price
        self.handling_price = handling_price
        self.total = total

    def get_total_amount_due_string(self):
        return str(self.total_amount_due)

    def get_sales_tax_string(self):
        return str(self.sales_tax)

    def get_shipping_price_string(self):
        return str(self.shipping_price)

    def get_handling_price_string(self):
        return str(self.handling_price)

    def get_total_price(self):
        return str(self.total)
