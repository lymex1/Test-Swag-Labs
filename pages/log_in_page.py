from locators.locators_log_in_page import LogInPageLocators as login_locators
from locators.catalog_locators import CatalogLocators as catalog_locators
from locators.checkout_locators import CheckOutLocators as checkout_locators
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LogInPage(BasePage):
    def log_in(self):
        user_name = self.element_is_visibale(login_locators.USER_NAME).text
        user_name = user_name.split('\n')
        password = self.element_is_visibale(login_locators.PASSWORD).text
        password = password.split('\n')
        self.element_is_visibale(login_locators.USER_NAME_INPUT).send_keys(user_name[1])
        self.element_is_visibale(login_locators.PASSWORD_INPUT).send_keys(password[1])
        self.element_is_visibale(login_locators.LOGIN_BUTTON).click()

    def choose_random_filter(self):
        self.element_is_visibale(catalog_locators.FILTER).click()
        self.element_is_visibale(catalog_locators.FILTER_OPTION).click()

    def in_catalog_go_to_card(self):
        self.element_is_visibale(catalog_locators.CARD).click()

    def add_card_and_go_to_cart_from_catalog(self):
        NAME_FROM_CATALOG = self.element_is_visibale(catalog_locators.CARD).text
        NAME_FROM_CATALOG = NAME_FROM_CATALOG.split(' ')
        NAME_FROM_CATALOG = '-'.join(NAME_FROM_CATALOG)
        self.element_is_visibale((By.CSS_SELECTOR, f'#add-to-cart-{NAME_FROM_CATALOG.lower()}')).click()
        self.element_is_visibale(catalog_locators.CART).click()

    def add_card_and_go_to_cart_from_card_details(self):
        NAME_FROM_CARD = self.element_is_visibale(catalog_locators.NAME_FROM_CARD).text
        NAME_FROM_CARD = NAME_FROM_CARD.split(' ')
        NAME_FROM_CARD = '-'.join(NAME_FROM_CARD)
        self.element_is_visibale((By.CSS_SELECTOR, f'#add-to-cart-{NAME_FROM_CARD.lower()}')).click()
        self.element_is_visibale(catalog_locators.CART).click()

    def checkout_overview(self):

        """This function end process and buy product"""
        self.element_is_visibale(checkout_locators.CHECKOUT_BUTTON).click()
        self.element_is_visibale(checkout_locators.FIRST_NAME).send_keys('Egor')
        self.element_is_visibale(checkout_locators.LAST_NAME).send_keys('Karinkin')
        self.element_is_visibale(checkout_locators.POSTAL_CODE).send_keys('123')
        self.element_is_visibale(checkout_locators.CONTINUE_BUTTON).click()
        self.element_is_visibale(checkout_locators.FINISH_BUTTON).click()
        finish_text = self.element_is_visibale(checkout_locators.COMPLETE_TEXT).text

        return finish_text




