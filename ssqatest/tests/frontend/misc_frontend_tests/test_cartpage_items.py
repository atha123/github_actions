import time

import pytest
from ssqatest.src.pages.HomePage_V2 import HomePage
from ssqatest.src.pages.ProductPage import ProductPage
from ssqatest.src.pages.CartPage import CartPage
from ssqatest.src.pages.Header import Header
from ssqatest.src.pages.CheckoutPage import CheckoutPage

@pytest.mark.usefixtures("init_driver")
class Testcartpagefields:
    """
    This is a test to verify the error message in the checkout page when the user enters invalid zipcode.
    """
    @pytest.fixture(scope='class')
    def setup(self,request):
        request.cls.home = HomePage(self.driver)
        request.cls.product  = ProductPage(self.driver)
        request.cls.header  = Header(self.driver)
        request.cls.cart  = CartPage(self.driver)
        request.cls.checkout  = CheckoutPage(self.driver)
        yield

    # @pytest.fixture(scope='class')
    @pytest.mark.lp26
    def test_set_up(self,setup):
        """
        Test to perform the following steps
        1. Launch the test site.
        2. Look for the product "belt" in the search bar.
        3. Go to the product details page.
        4. Click on Add to cart button
        5. Repeat the above product "sunglasses"
        """


        self.home.go_home()
        self.header.input_int_search_field("belt")
        self.header.press_enter_on_search_field()
        self.product.click_add_to_cart_button()
        self.header.input_int_search_field("sunglasses")
        self.header.press_enter_on_search_field()
        self.product.click_add_to_cart_button_sunglasses()
        self.cart.go_to_cart_page()
        items = self.cart.get_all_product_names_in_cart()


        #Assert that the first item in the Cart page is 'belt' and the second one is 'sunglasses'
        assert items[0] == 'Belt', 'First item should have been belt'
        assert items[1] == 'Sunglasses', 'Second item should have been Sunglasses'

        # Comprehensive test




