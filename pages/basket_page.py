from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def check_basket_empty(self):
        assert self.browser.find_element(*BasketPageLocators.BASKET_EMPTY), 'Ошибка! Корзина не пуста!'

    def check_not_basket_item(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), 'Ошибка! в корзине есть товар!!'
