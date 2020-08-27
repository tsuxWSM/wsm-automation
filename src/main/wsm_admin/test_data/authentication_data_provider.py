from ...data_model.customer import Customer


class AdminAuthenticationDataProvider:
    """Test Data and String Providers for Sign In"""

    def __init__(self):
        # Test Data
        self.username = "tsune"
        self.password = "drg75F0x29"
        self.email = "tsune@webshopmanager.com"
        self.wrong_password = "wr0n9_p4$$w0rd"
        self.invalid_email = "tsune_129"
        self.non_existent_email = "tsune@gmail.com"

        # String Providers
        self.invalid_creds_error_message_string = "Incorrect username or password."
        self.login_title_string = "Login to WSM"
        self.forgot_password_title_string = "Forgot Password"
        self.email_label_string = "Login or email address:"
        self.email_notification_message = "If you entered a valid login or email address, you will receive an email " \
                                          "with a link to reset your password within the next 10 minutes."


class WebShopAuthenticationDataProvider:

    def __init__(self):
        self.user_tsune = Customer("Tsune", "Maldonado", "tsune@webshopmager.com", "tsux75", 1231, "06/03/1990")
        self.user_eric = Customer("Eric", "Lawler", "eric@webshopmanager.com", "erd77", 1232, "10/26/1987")
        self.user_eduardo = Customer("Eduardo", "Maldonado", "rec.tsune@gmail.com", "tsux77", 1729, "01/25/1999")
