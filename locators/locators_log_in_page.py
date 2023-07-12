from selenium.webdriver.common.by import By

class LogInPageLocators:

    USER_NAME = (By.XPATH, "//div[@class='login_credentials']")
    PASSWORD = (By.CLASS_NAME, "login_password")
    USER_NAME_INPUT = (By.CSS_SELECTOR, '#user-name')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '#password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '#login-button')