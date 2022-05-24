from .pages.product_page import ProductPage
import pytest
from .pages.main_page import MainPage
from selenium.webdriver.support.wait import WebDriverWait
from .pages.login_page import LoginPage
import faker
import time
from .pages.basket_page import BasketPage

links_list = ["https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
              "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
              "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
              "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
              "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
              "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
              "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
              pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                           marks=pytest.mark.xfail),
              "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
              "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]


@pytest.mark.need_review
@pytest.mark.parametrize('links', links_list, )
def test_guest_can_add_to_basket(browser, links):
    page = ProductPage(browser, links)
    page.open()
    page.add_item_to_basket_and_click()
    page.solve_quiz_and_get_code()
    page.check_price_and_title_book()


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_basket_and_click()
    page.should_not_be_success_message()


@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_basket_and_click()
    page.should_dissapear_of_success_message()


@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.check_not_basket_item()
    basket_page.check_basket_empty()


class TestUserAddToBasketFromProductPage:


    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        f = faker.Faker()
        email = f.email()
        link = 'https://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
        self.browser = browser
        self.page = LoginPage(browser, link)
        self.page.open()
        self.page.register_new_user(email, 'nvr3u9nr3v9')
        self.page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
        page = ProductPage(self.browser, link)
        page.open()
        page.go_to_basket()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_to_basket(self, browser):
        link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
        page = ProductPage(self.browser, link)
        page.open()
        page.add_item_to_basket_and_click()
        page.check_price_and_title_book()
