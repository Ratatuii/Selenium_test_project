from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, '.basket-mini .btn-default')


class LoginPageLocators:
    LOGIN_INPUT = (By.NAME, 'login-username')
    PASSWORD_INPUT = (By.NAME, 'login-password')


class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, '.basket-items')
    BASKET_EMPTY = (By.CSS_SELECTOR, '#content_inner > p')


class MainPageLocators:
    pass


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    BOOK_NAME = (By.CSS_SELECTOR, '.product_main h1')
    BUY_BOOK = (By.CSS_SELECTOR, '.alertinner strong')
    BOOK_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    BUY_BOOK_PRICE = (By.CSS_SELECTOR, '.alert-info .alertinner strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
