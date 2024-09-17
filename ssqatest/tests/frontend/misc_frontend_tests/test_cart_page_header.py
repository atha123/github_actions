from ssqatest.src.pages.HomePage import HomePage
from ssqatest.src.pages.CartPage import CartPage
from ssqatest.src.pages.Header import Header
import pytest

@pytest.mark.usefixtures("init_driver")
class TestCartHeader:
    """
    This is a test a test to check the labels in the cart page after an item is added to the cart.
    """

    @pytest.fixture(scope='class')
    def setup(self,request):
        request.cls.home = HomePage(self.driver)
        request.cls.cart = CartPage(self.driver)
        request.cls.header = Header(self.driver)
        yield


    @pytest.mark.lp20
    def test_labels_cart_page(self,setup):
        """
        This is a test to ensure that
        1. All the 6 labels are visible.
        2. The correct labels/data is displayed in the Cart Page when an item is added.
        Args:
            setup:

        Returns:

        """
        self.home.go_to_home_page()
        self.home.click_first_add_to_cart_button()
        self.header.wait_until_cart_item_count(1)
        self.cart.go_to_cart_page()

        headers = self.cart.get_cart_column_header()

        # Assert that there are 5 labels
        assert len(headers) == 6, "Number of headers in UI is incorrect"

        #Assert that the labels are correct
        expected = ['Remove item','Thumbnail image','Product','Price','Quantity','Subtotal']
        l = len(expected)

        for i in range(l):
            assert headers[i].text == expected[i], "The column names do not match the expected names."






