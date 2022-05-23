from .base_page import BasePage
from .locators import ProductPageLocators
import pytest


class ProductPage(BasePage):

    def add_item_to_basket_and_click(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()

    @pytest.mark.xfail
    def check_price_and_title_book(self):
        self.check_book()
        self.check_price()

    def check_book(self):
        book = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        buy_book = self.browser.find_element(*ProductPageLocators.BUY_BOOK).text
        assert book == buy_book, f'Что-то не так с названиями.. На странице книги: {book} Купили: {buy_book}'

    def check_price(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        buy_book_price = self.browser.find_element(*ProductPageLocators.BUY_BOOK_PRICE).text
        assert book_price == buy_book_price, f'Что-то не так с ценой.. Было: {book_price}, стало: {buy_book_price}'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), 'Ошибка, сообщение есть!'

    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), 'Ошибка, сообщение не исчезает!'
