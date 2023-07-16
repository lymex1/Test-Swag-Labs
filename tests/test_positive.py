import time
from pages.log_in_page import LogInPage

class TestPositiveSwagLabs:
    def test_buy_on_web_site(self, driver):
        web_site = LogInPage(driver=driver, url='https://www.saucedemo.com/')
        web_site.open()
        web_site.log_in()
        web_site.in_catalog_go_to_card()
        web_site.add_card_and_go_to_cart_from_card_details()
        result = web_site.checkout_overview()
        assert result == 'Thank you for your order!'

    def test_buy_on_catalog(self, driver):
        web_site = LogInPage(driver=driver, url='https://www.saucedemo.com/')
        web_site.open()
        web_site.log_in()
        web_site.add_card_and_go_to_cart_from_catalog()
        result = web_site.checkout_overview()
        assert result == 'Thank you for your order!'

    def test_buy_on_web_site_with_random_filter(self, driver):
        web_site = LogInPage(driver=driver, url='https://www.saucedemo.com/')
        web_site.open()
        web_site.log_in()
        web_site.choose_random_filter()
        web_site.in_catalog_go_to_card()
        web_site.add_card_and_go_to_cart_from_card_details()
        result = web_site.checkout_overview()
        assert result == 'Thank you for your order!'

    def test_buy_on_catalog_with_random_filter(self, driver):
        web_site = LogInPage(driver=driver, url='https://www.saucedemo.com/')
        web_site.open()
        web_site.log_in()
        web_site.choose_random_filter()
        web_site.add_card_and_go_to_cart_from_catalog()
        result = web_site.checkout_overview()
        assert result == 'Thank you for your order!'