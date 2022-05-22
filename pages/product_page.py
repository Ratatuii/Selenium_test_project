from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def go_to_login_page(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()

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
