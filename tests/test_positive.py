import time

from pages.log_in_page import LogInPage

class TestPositiveSwagLabs:
    def test_buy_on_web_site(self, driver):
        start_and_log_in_page = LogInPage(driver=driver, url='https://www.saucedemo.com/')
        start_and_log_in_page.open()

        def test_log_in_on_site():
            start_and_log_in_page.log_in()
            
        def test_go_to_card():
            start_and_log_in_page.in_catalog_go_to_card()
        
        def test_add_card_to_cart():
            start_and_log_in_page.add_card_and_go_to_cart()

        test_log_in_on_site()
        test_go_to_card()
        test_add_card_to_cart()
