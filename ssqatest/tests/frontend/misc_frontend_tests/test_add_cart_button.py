import time
import pytest
from ssqatest.src.pages.HomePage import HomePage
from ssqatest.src.pages.Header import Header
import logging as logger
import allure


@allure.tag("Cart","Integration_test_phase" )
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Latha Pai")
@allure.testcase("Jira Story ticket: TMS-456")

@pytest.mark.usefixtures('init_driver')
class TestAddCart:
    """
        This is a test to verify that when a user clicks on the 'Add to cart button', the cart gets incremented.

    """
    @pytest.fixture(scope='class')
    def setup(self,request):
        request.cls.home = HomePage(self.driver)
        request.cls.header = Header(self.driver)

    @pytest.mark.lp015
    @allure.title("TMS-456- Verify the number of items in the cart is incremented when a product is added to the cart.")
    def test_add_to_cart_counter(self,setup):
        """
            This test is to check that when a user clicks on the 'Add to Cart' button, the number of items in the cart is incremented.
        Steps-
       1. Launch the home page.
       2. Verify the count for items is zero.
       3. Add the first item to the cart.
       4. Using an Assert statement, verify that the number of items in the cart now shows 1.

        """
        self.home.go_to_home_page()
        count_before= self.header.get_cart_item_count()
        print(f"Count of items before clicking 'Add to cart' is : {count_before}")
        self.home.click_first_add_to_cart_button()
        self.header.wait_until_cart_item_count(1)
        count_after = self.header.get_cart_item_count()
        print(f"Count of items after clicking 'Add to cart' is : {count_after}")

        assert int(count_after) == int(count_before)+1, "failed"
        logger.info("Test Passed!!")


