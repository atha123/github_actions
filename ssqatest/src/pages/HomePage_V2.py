from ssqatest.src.selenium_extended.SeleniumExtended import SeleniumExtended
from ssqatest.src.configs.MainConfigs import MainConfigs
# from ssqatest.src.pages.locators.HomePageLocators import HomePageLocators
from ssqatest.src.pages.locators.HomeLocators_V2 import HomeLocatorsV2


class HomePage(HomeLocatorsV2):
    def __init__(self,driver):
        self.driver = driver
        self.sl=SeleniumExtended(self.driver)

    def go_home(self):
        self.driver.get("http://dev.bootcamp.store.supersqa.com/")

    def click_add_to_cart_button(self):
        self.sl.wait_until_element_is_visible(self.ADD_TO_CART)
        # THIS IS NOT NEEDED FOR NOW. WORKS THOUGH

    def get_all_products(self):
        return self.sl.wait_and_get_elements(self.PRODUCT)

    def get_add_to_cart_button(self):
        return self.sl.wait_until_element_is_visible(self.BTN_ADD_TO_CART)


