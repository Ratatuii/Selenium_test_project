from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_INPUT = (By.NAME, 'login-username')
    PASSWORD_INPUT = (By.NAME, 'login-password')


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    BOOK_NAME = (By.CSS_SELECTOR, '.product_main h1')
    BUY_BOOK = (By.CSS_SELECTOR, '.alertinner strong')
    BOOK_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    BUY_BOOK_PRICE = (By.CSS_SELECTOR, '.alert-info .alertinner strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")