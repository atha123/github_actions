import pytest
from ssqatest.src.pages.HomePage_V2 import HomePage
from ssqatest.src.pages.Header import Header

@pytest.mark.usefixtures("init_driver")
class TestHeaderLabels:
    """
    This is a test to ensure that the header labels show up correctly.
    """
    @pytest.fixture(scope='class')
    def setup(self,request):
        request.cls.home = HomePage(self.driver)
        request.cls.header  = Header(self.driver)
        yield

    @pytest.mark.lp27
    def test_header(self,setup):
        self.home.go_home()
        menu_labels = self.header.get_all_menu_item_text()
        expected_label = ['Home','Cart','Checkout','My account','Sample Page']
        number_of_labels = len(expected_label)

        for i in range(number_of_labels):
            assert menu_labels[i] == expected_label[i], f"Actual label is: '{menu_labels[i]}' and expected label is '{expected_label[i]}'"



