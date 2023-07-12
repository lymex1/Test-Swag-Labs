import time

from pages.log_in_page import LogInPage

class TestPositiveSwagLabs:
    def test_positive_bought(self, driver):
        start_and_log_in_page = LogInPage(driver=driver, url='https://www.saucedemo.com/')
        start_and_log_in_page.open()
        start_and_log_in_page.log_in()
