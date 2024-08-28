import pytest
from ssqatest.src.pages.HomePage import HomePage
import logging as logger

@pytest.mark.usefixtures("init_driver")
class TestProductName:
    """
    This is a test to ensure that the the product name shows up under the product image.
    """

    # Creating page objects
    @pytest.fixture(scope='class')
    def setup(self,request):
        request.cls.homepage = HomePage(self.driver)
        yield

    @pytest.mark.lp013
    def test_product_desc(self,setup):
        self.homepage.go_to_home_page()
        first_product = self.homepage.get_product_name()
        assert first_product.is_displayed(), f"Product name displayed is not 'Album'. Actual displayed is: '{first_product}'"

        logger.info("Test Passed !")



