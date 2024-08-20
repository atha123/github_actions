import  pytest
import time
import logging as logger
from ssqatest.src.selenium_extended import SeleniumExtended
from ssqatest.src.pages.HomePage import HomePage
@pytest.mark.usefixtures("init_driver")
class TestAddCart:
    """
        This is a test to ensure that when a user clicks on 'Add to Cart', the 'View cart' button gets displayed
    """
    # create page objects
    @pytest.fixture(scope= 'class')
    def setup(self, request):
        request.cls.homepage = HomePage(self.driver)
        yield

    @pytest.mark.lp012
    def test_add_button_displays_view_button(self,setup):
        self.homepage.go_to_home_page()
        self.homepage.click_first_add_to_cart_button()
        view_btn = self.homepage.get_view_button_first_product()

        assert view_btn, f"'View cart' button does not show when the 'Add to cart' is clicked"
        time.sleep(5)






