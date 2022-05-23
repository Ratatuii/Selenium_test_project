from .pages.product_page import ProductPage
import pytest

links_list = ["https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
               pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
              "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]


@pytest.mark.parametrize('links', links_list,)
def test_guest_can_add_to_basket(browser, links):
    # link = "https://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    # link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser, links)
    page.open()
    page.go_to_login_page()
    page.solve_quiz_and_get_code()
    page.check_price_and_title_book()
