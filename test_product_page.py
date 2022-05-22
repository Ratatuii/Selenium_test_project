from .pages.product_page import ProductPage


def test_guest_can_add_to_basket(browser):
    link = "https://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    # link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.solve_quiz_and_get_code()
    page.check_price_and_title_book()


