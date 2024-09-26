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

    @pytest.mark.lp22
    def test_end_to_end(self,setup):
        self.home.go_home()
        self.header.input_int_search_field("belt")
        self.header.press_enter_on_search_field()
        name= self.product.get_displayed_product_name()
        self.product.click_add_to_cart_button()
        message = self.product.get_confirm_msg_on_product_add_to_cart().text

        print(message)
