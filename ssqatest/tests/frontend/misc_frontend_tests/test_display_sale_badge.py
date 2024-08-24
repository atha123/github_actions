import pytest
from ssqatest.src.pages.HomePage import HomePage
import logging as logger

@pytest.mark.usefixtures("init_driver")
class TestDisplaySaleBadge:
    """
        This is to ensure that the sale badge is displayed for items on sale.
    """

    @pytest.fixture(scope = 'class')
    def setup(self,request):
        request.cls.home = HomePage(self.driver)


    @pytest.mark.lp017
    def test_sale_badge(self,setup):
        self.home.go_to_home_page()
        test = self.home.get_all_product_elements()
        # breakpoint()
        for i in test:
            whole_name = i.text
            name = whole_name.split("\n")
            if 'SALE!' in name:
                sale_badge = self.home.get_sale_badge()
                assert sale_badge, 'Sale badge is missing'

            else:
                pass

    logger.info("Test Passed!")


