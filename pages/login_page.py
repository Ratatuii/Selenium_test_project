from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url_str = self.browser.current_url
        fl = False
        if url_str.find("login") > 0:
            fl = True
        assert fl, '"login" не найден в url'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_INPUT), 'Проблема с поиском поля ввода логина'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.PASSWORD_INPUT), 'Проблема с поиском поля ввода пароля'
