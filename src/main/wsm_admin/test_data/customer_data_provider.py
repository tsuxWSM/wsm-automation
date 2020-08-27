from ...data_model.customer import Customer


class CustomerDataProvider:
    """Customer class for test data management"""

    def __init__(self):
        self.customer_default = Customer("Tsune", "Maldonado", "tsune@webshopmanager.com", "tsux75", 1231, "06/03/1990")
        self.customer_tax_exempt = Customer("Eric", "Lawler", "eric@webshopmanager.com", "erd77", 1232, "10/26/1987",
                                            tax_exempt=True)
        self.customer_invoice_only = Customer("Isaac", "Novartx", "rec.isaac@gmail.com", "tsux77", 1729, "01/25/1999",
                                              invoice_only=True)
        self.customer_block_free_shipping = Customer("Charly", "Atlas", "rec.charly@gmail.com", "tsux77", 1729,
                                                     "01/25/1999", invoice_only=True)
        self.customer_inactive = Customer("Eduardo", "Maldonado", "rec.tsune@gmail.com", "tsux77", 1729, "01/25/1999",
                                          is_active=False, affirm_allowed=False, invoice_only=True, tax_exempt=True,
                                          block_free_shipping=True)

        # String providers
        self.created_user_message = "Customer saved successfully!"
        self.deleted_user_message = "Customer has been deleted."
        self.no_results_message = "No search results found.  "
        self.clear_search_message = "clear search terms"
