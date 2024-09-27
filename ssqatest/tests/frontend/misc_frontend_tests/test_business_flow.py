import pytest
from ssqatest.src.pages.HomePage_V2 import HomePage
from ssqatest.src.pages.ProductPage import ProductPage
from ssqatest.src.pages.CartPage import CartPage
from ssqatest.src.pages.Header import Header

@pytest.mark.usefixtures("init_driver")
class Testbusinessflow:
    """
    This is a test to ensure that the end to end business flow works well.
    """
    @pytest.fixture(scope='class')
    def setup(self,request):
        request.cls.home = HomePage(self.driver)
        request.cls.product  = ProductPage(self.driver)
        request.cls.header  = Header(self.driver)
        request.cls.cart  = CartPage(self.driver)
        yield

    @pytest.mark.lp21
    def test_end_to_end(self,setup):
        self.home.go_home()
        self.header.input_int_search_field("belt")
        self.header.press_enter_on_search_field()
        name= self.product.get_displayed_product_name()
        self.product.click_add_to_cart_button()
        self.cart.go_to_cart_page()
        self.cart.click_remove_item_button()
        # breakpoint()
        message = self.cart.get_success_message()
        list_message = message.split("\n")  #The result of this is that the 2 confirmation lines in the UI will be put in a list as 2 elements.


        # Assert the first confirmation string
        actual_first_message = list_message[0]
        expected_first_message = '“Belt” removed. Undo?'
        assert actual_first_message == expected_first_message, f"First message is Incorrect! Expected:'{expected_first_message}'. Actual:'{actual_first_message}'"

        # Assert the second confirmation string.
        assert list_message[1] == "Your cart is currently empty.", f"Second message is Incorrect!. Expected:'Your cart is currently empty.'. Actual:'{list_message[1]}'"








