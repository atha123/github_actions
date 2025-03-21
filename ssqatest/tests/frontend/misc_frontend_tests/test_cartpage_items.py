import time

import pytest
from ssqatest.src.pages.HomePage_V2 import HomePage
from ssqatest.src.pages.ProductPage import ProductPage
from ssqatest.src.pages.CartPage import CartPage
from ssqatest.src.pages.Header import Header
from ssqatest.src.pages.CheckoutPage import CheckoutPage
import allure


# @allure.description("Verify the cart page has the 2 items added and the correct names show up.")
@allure.tag("Cart","Integration_test_phase" )
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Latha Pai")
@allure.issue("Defect ticket: ERP-9900")
@allure.testcase("Jira Story ticket: TMS-456")

@pytest.mark.usefixtures("init_driver")
class TestCartPageFields:
    """
    This is a test to verify the cart page has the 2 items (Belt and Sunglasses) added and the correct names show up.
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
    @allure.title("TMS-456- Verify the cart page has the 2 items added and the correct names show up")
    def test_product_names_in_cartpage(self,setup):
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