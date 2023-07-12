from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    """This function open website"""
    def open(self):
        self.driver.get(url=self.url)

    """Эта функция позволяет не искать элемент на 
        странице пока он не загрузиться"""
    def element_is_visibale(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
