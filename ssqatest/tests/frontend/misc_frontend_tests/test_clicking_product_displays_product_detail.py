import pytest
from ssqatest.src.pages.ProductPage import ProductPage
from ssqatest.src.pages.HomePage import HomePage
import logging as logger

@pytest.mark.usefixtures("init_driver")
class TestClickingProductShowsDesc:
    """
    This is a test to ensure that when the user clicks on the product, the product description gets displayed in the details page.
    """
    @pytest.fixture(scope='class')
    def setup(self,request):
        request.cls.home = HomePage(self.driver)
        request.cls.product = ProductPage(self.driver)

    @pytest.mark.lp014
    def test_product_name_under_image(self,setup):
        # breakpoint()
        self.home.go_to_home_page()
        first_product = self.home.get_firts_product_name()
        # print(f"first product is : '{first_product}'")
        self.home.click_first_product_image()
        name = self.product.get_displayed_product_name()
        assert name == first_product, "Product details page does not show the name of the Product"
        logger.info("Test Passed! ")