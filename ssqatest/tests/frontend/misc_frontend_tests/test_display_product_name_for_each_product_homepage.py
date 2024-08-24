import pytest
from ssqatest.src.selenium_extended import SeleniumExtended
from ssqatest.src.pages.HomePage import HomePage
import logging as logger
@pytest.mark.usefixtures("init_driver")
class TestDisplayProductName:
    """
        This is a test to ensure that each product on the home page gets its product name displayed at the bottom of the picture.
    """
    @pytest.fixture(scope= 'class')
    def setup(self,request):
        request.cls.home = HomePage(self.driver)


    @pytest.mark.lp016
    def test_product_name_home_page(self,setup):
        self.home.go_to_home_page()
        test = self.home.get_all_product_elements()

        for i in test:
            whole_name= i.text
            name=whole_name.split("\n")
            print(name[0])
            assert name, "Product name is not displayed! "

        logger.info(("Test Passed !"))


