from selenium.webdriver.common.by import By

class CheckOutLocators:
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, '#checkout')
    FIRST_NAME = (By.CSS_SELECTOR, '#first-name')
    LAST_NAME = (By.CSS_SELECTOR, '#last-name')
    POSTAL_CODE = (By.CSS_SELECTOR, '#postal-code')
    CONTINUE_BUTTON = (By.CSS_SELECTOR, '#continue')
    FINISH_BUTTON = (By.CSS_SELECTOR, '#finish')
    COMPLETE_TEXT = (By.CLASS_NAME, 'complete-header')
