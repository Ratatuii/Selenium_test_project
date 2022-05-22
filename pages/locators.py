from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators():
    LOGIN_INPUT = (By.NAME, 'login-username')
    PASSWORD_INPUT = (By.NAME, 'login-password')
