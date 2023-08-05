from selenium.webdriver.common.by import By
from random import randint

class CatalogLocators:
    FILTER = (By.CLASS_NAME, 'product_sort_container')
    FILTER_OPTION = (By.XPATH, f"//select[@class='product_sort_container']//option[{randint(1,4)}]")
    NAME_FROM_CARD = (By.CLASS_NAME, 'inventory_details_name')
    CARD = (By.ID, f'item_{randint(0,5)}_title_link')
    CART = (By.ID, 'shopping_cart_container')

