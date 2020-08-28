from __future__ import annotations
from abc import abstractmethod
from .cart_page import CartPage
from .coverlay.cart_page import CoverlayCartPage
from .coverlay.checkout_page import CoverlayCheckoutPage
from .checkout_page import CheckoutPage
from ...data_model.quote import Quote
from .extrememetalproducts.cart_page import ExtremeMetalProductsCartPage
from .extrememetalproducts.checkout_page import ExtremeMetalProductsCheckoutPage
from ...utils.system_constants import Site


class PageFactory:

    @abstractmethod
    def cart(self, driver, product_list, quote, user_lands_from_admin) -> CartPage:
        pass

    @abstractmethod
    def checkout(self, driver, invoice_only, signed_user) -> CheckoutPage:
        pass


class CVLPageFactory(PageFactory):

    def cart(self, driver, product_list=None, quote: Quote = None, user_lands_from_admin: bool = False)\
            -> CoverlayCartPage:
        return CoverlayCartPage(driver)

    def checkout(self, driver, invoice_only: bool = False, signed_user: bool = False)\
            -> CoverlayCheckoutPage:
        return CoverlayCheckoutPage(driver=driver, invoice_only=invoice_only, signed_user=signed_user)


class EMPPageFactory(PageFactory):

    def cart(self, driver, product_list=None, quote: Quote = None, user_lands_from_admin: bool = False)\
            -> ExtremeMetalProductsCartPage:
        return ExtremeMetalProductsCartPage(driver, product_list, quote, user_lands_from_admin)

    def checkout(self, driver, invoice_only: bool = False, signed_user: bool = False)\
            -> ExtremeMetalProductsCheckoutPage:
        return ExtremeMetalProductsCheckoutPage(driver=driver)


class PageBuilder:

    def __init__(self, site: Site):
        self.site = site

    def get_factory(self) -> PageFactory:
        if self.site == Site.EMP.value:
            return EMPPageFactory()
        elif self.site == Site.CVL.value:
            return CVLPageFactory()
        else:
            raise BaseException("Not Supported Site>> Please pick a site from System Constant's Site Enum")
