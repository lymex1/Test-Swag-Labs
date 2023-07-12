import time
from random import randint
from locators.locators_log_in_page import LogInPageLocators as Locators
from pages.base_page import BasePage


class LogInPage(BasePage):

    def log_in(self):
        user_name = self.element_is_visibale(Locators.USER_NAME).text
        user_name = user_name.split('\n')
        print(user_name)
        password = self.element_is_visibale(Locators.PASSWORD).text
        password = password.split('\n')
        print(password)
        self.element_is_visibale(Locators.USER_NAME_INPUT).send_keys(user_name[1])
        self.element_is_visibale(Locators.PASSWORD_INPUT).send_keys(password[1])
        self.element_is_visibale(Locators.LOGIN_BUTTON).click()