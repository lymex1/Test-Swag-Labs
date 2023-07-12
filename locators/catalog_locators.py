from selenium.webdriver.common.by import By
from random import randint

class CatalogLocators:
    NAME = (By.CLASS_NAME, 'inventory_details_name')
    CARD = (By.ID, f'item_{randint(0,5)}_title_link')
    CART = (By.CSS_SELECTOR, '#shopping_cart_container')

