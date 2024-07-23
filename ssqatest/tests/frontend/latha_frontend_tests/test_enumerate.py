import pytest
from ssqatest.src.pages.HomePage import HomePage
import  logging as logger

pytestmark=[pytest.mark.feregression, pytest.mark.fesmoke]
@pytest.mark.usefixtures("init_driver")

class TestDropDown():
    """
    This is a test to check that the expected strings show up in the drop down menu of the main page (top) using a for loop.

    """
    @pytest.mark.lpenu
    def test_dropdownmenu_bottom_test_strings(self):
        home= HomePage(self.driver)
        home.go_to_home_page()
        drop_down = home.get_sorting_dropdown_bottom_page()
        contents = drop_down.splitlines()
        expected_list = ['Default sorting', 'Sort by popularity', 'Sort by average rating', 'Sort by latest',
                         'Sort by price: low to high', 'Sort by price: high to low','']
        # Validation for the contents of the drop down menu

        for index,expected in enumerate(contents):
            assert expected.lstrip() == expected_list[index], "no match"
            print(f" expected '{expected.lstrip()}' = actual '{expected_list[index]}'")

