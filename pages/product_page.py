from .base_page import BasePage
from .locators import ProductPageLocators
import pytest


class ProductPage(BasePage):

    def go_to_login_page(self):
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

    # def test_guest_can_add_product_to_basket(self, link):
    #    pass

    # def test_guest_cant_see_success_message_after_adding_product_to_basket(self):
    #    assert self.is_not_element_present(*ProductPageLocators.BUY_BOOK)