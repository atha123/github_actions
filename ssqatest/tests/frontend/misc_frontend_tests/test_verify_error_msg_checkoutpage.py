import pytest
from ssqatest.src.pages.HomePage_V2 import HomePage
from ssqatest.src.pages.ProductPage import ProductPage
from ssqatest.src.pages.CartPage import CartPage
from ssqatest.src.pages.Header import Header
from ssqatest.src.pages.CheckoutPage import CheckoutPage

@pytest.mark.usefixtures("init_driver")
class Testbusinessflow:
    """
    This is a test to verify the error messages in the checkout page when the user does not enter any Billing details
    """
    @pytest.fixture(scope='class')
    def setup(self,request):
        request.cls.home = HomePage(self.driver)
        request.cls.product  = ProductPage(self.driver)
        request.cls.header  = Header(self.driver)
        request.cls.cart  = CartPage(self.driver)
        request.cls.checkout  = CheckoutPage(self.driver)
        yield

    @pytest.mark.lp24
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
        self.checkout.click_place_order()
        actual_msgs = self.checkout.get_checkout_error_msgs()
        expected_msgs_list = ['Billing First name is a required field.','Billing Last name is a required field.','Billing Street address is a required field.','Billing Town / City is a required field.','Billing ZIP Code is a required field.','Billing Phone is a required field.','Billing Email address is a required field.','Invalid payment method.']

        actual_msgs_list = actual_msgs.split("\n")
        print(actual_msgs_list)
        length= len(actual_msgs_list)

        #Assert that the number of error messages displayed when only zipcode is entered is 7.
        assert len(actual_msgs_list) == 8, f"Number of error messages should be 7. Actual is: {len(actual_msgs_list)}"

        # Assert the error message strings
        for i in range(length):
            print(f"Error message {i}: '{actual_msgs_list[i]}' is present.")
            assert expected_msgs_list[i] == actual_msgs_list[i], "Error"








