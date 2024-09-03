
from selenium.webdriver.common.by import By


# class PageLocatorsHome:
class HomeLocatorsV2:
    ADD_TO_CART = (By.CSS_SELECTOR, 'a.woocommerce-LoopProduct-link')
    PRODUCT = (By.CSS_SELECTOR, 'ul.products li.product')
    BTN_ADD_TO_CART = (By.CSS_SELECTOR, 'a.add_to_cart_button')

