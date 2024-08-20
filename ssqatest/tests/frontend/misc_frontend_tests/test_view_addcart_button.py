import  pytest
import logging as logger
from ssqatest.src.selenium_extended import SeleniumExtended
from ssqatest.src.pages.HomePage import HomePage

@pytest.mark.usefixtures("init_driver")
@pytest.mark.lp012
class TestAddCart:
    """
        This is a test to ensure that when a user clicks on 'Add to Cart', the 'View cart' button is also displayed
    """
    # create page objects
    @pytest.fixture(scope= 'class')
    def setup(self, request):
        request.cls.homepage = HomePage(self.driver)
        yield

    def test_add_button_displays_view_button(self):
        self.homepage.go_to_home_page()
        self.homepage.click_first_add_to_cart_button()





