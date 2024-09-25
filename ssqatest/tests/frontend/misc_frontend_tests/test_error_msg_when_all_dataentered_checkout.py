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
    This is a test to verify the error message in the checkout page when the user enters all correct data but still there is a error
    message because the payment method is not set up
    """
    @pytest.fixture(scope='class')
    def setup(self,request):
        request.cls.home = HomePage(self.driver)
        request.cls.product  = ProductPage(self.driver)
        request.cls.header  = Header(self.driver)
        request.cls.cart  = CartPage(self.driver)
        request.cls.checkout  = CheckoutPage(self.driver)
        yield

    @pytest.mark.lp25
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
        self.product.click_add_to_cart_button()
        self.checkout.go_to_checkout_page()


        #Enter test data
        self.checkout.input_billing_first_name("Joe")
        self.checkout.input_billing_last_name("Smith")
        self.checkout.input_billing_street_address_1("Main St")
        self.checkout.input_billing_city("New York")
        self.checkout.input_billing_zip("12345")
        self.checkout.input_billing_phone_number("0000000000")
        self.checkout.input_billing_email("abc@gmail.com")
        self.checkout.click_place_order()
        time.sleep(5)
        actual_msgs = self.checkout.get_checkout_error_msgs()

        assert actual_msgs == 'Invalid payment method.', f"Expected message was:'Invalid payment method.'. Actual is: '{actual_msgs}' "
