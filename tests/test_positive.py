import time
from pages.log_in_page import LogInPage

class TestPositiveSwagLabs:
    def test_buy_on_web_site(self, driver):
        start_and_log_in_page = LogInPage(driver=driver, url='https://www.saucedemo.com/')
        start_and_log_in_page.open()
        start_and_log_in_page.log_in()
        start_and_log_in_page.in_catalog_go_to_card()
        start_and_log_in_page.add_card_and_go_to_cart()
        result = start_and_log_in_page.checkout_overview()
        assert result == 'Thank you for your order!'
