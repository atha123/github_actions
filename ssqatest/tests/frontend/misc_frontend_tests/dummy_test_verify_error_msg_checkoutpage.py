import time

import pytest
from ssqatest.src.pages.HomePage_V2 import HomePage
from ssqatest.src.pages.ProductPage import ProductPage
from ssqatest.src.pages.CartPage import CartPage
from ssqatest.src.pages.Header import Header
from ssqatest.src.pages.CheckoutPage import CheckoutPage

@pytest.mark.usefixtures("init_driver")
class Testbusinessflow:
    """
    This is a test to verify the error message in the checkout page when the user enters alhpabets for zipcode.
    """
    @pytest.fixture(scope='class')
    def setup(self,request):
        request.cls.home = HomePage(self.driver)
        request.cls.product  = ProductPage(self.driver)
        request.cls.header  = Header(self.driver)
        request.cls.cart  = CartPage(self.driver)
        request.cls.checkout  = CheckoutPage(self.driver)
        yield


    def test_add_product_to_cart(self,setup):
        """
        Test to perform the following steps
        1. Launch the test site.
        2. Look for the product "belt" in the search bar.
        3. Go to the product details page.
        4. Click on Add to cart button

        """
        self.home.go_home()
        self.header.input_int_search_field("belt")
        self.header.press_enter_on_search_field()
        name= self.product.get_displayed_product_name()
        self.product.click_add_to_cart_button()
        time.sleep(10)

    @pytest.mark.lp23
    def test_checkout_errors(self,setup,test_add_product_to_cart):
        self.checkout.go_to_checkout_page()



# breakpoint()


