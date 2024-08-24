import pytest
from ssqatest.src.pages.HomePage import HomePage
import logging as logger

@pytest.mark.usefixtures("init_driver")
class TestDisplayPrice:
    """
        This is to ensure that the price is displayed for all items.
    """

    @pytest.fixture(scope = 'class')
    def setup(self,request):
        request.cls.home = HomePage(self.driver)


    @pytest.mark.lp018
    def test_display_price(self,setup):
        self.home.go_to_home_page()
        products = self.home.get_all_product_elements()


        for i in products:
            whole_name = i.text
            name = whole_name.split("\n")
            price= self.home.get_product_price()
            assert price.is_displayed(), "Price missing"

        logger.info('Test Passed!')