import time

import pytest
from ssqatest.src.pages.HomePage_V2 import HomePage
import logging as logger

@pytest.mark.usefixtures("init_driver")
class TestDisplayAddToCart:
    """
    This is to ensure that each item has 'Add to Cart' button.
    """

    @pytest.fixture(scope = 'class')
    def setup(self,request):
        request.cls.home = HomePage(self.driver)

    @pytest.mark.lp020
    def test_viewcart(self, setup):
        self.home.go_home()
        items = self.home.get_all_products()
        for i in items:
            btn = self.home.get_add_to_cart_button()
            assert btn.is_displayed(), f"There is not button called 'Add to Cart' for item: {i}"

        logger.info("Test passed!")



