class Customer:
    """Customer model class for test data management"""

    def __init__(self, user_name: str, last_name: str, email: str, password: str, account_number: int, birth_date: str,
                 is_active=True, affirm_allowed=True, invoice_only=False, tax_exempt=False, block_free_shipping=False):
        self.email = email
        self.password = password
        self.name = user_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.account_number = str(account_number)

        # default customer price group
        self.price_group = "none"

        # Customer Flag Initial status
        self.active = is_active
        self.affirm_allowed = affirm_allowed
        self.invoice_only = invoice_only
        self.tax_exempt = tax_exempt
        self.block_free_shipping = block_free_shipping
