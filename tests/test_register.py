from pages.auth_by_code_page import AuthByCodePages
import pytest


class TestRegister:
    LOGIN = "rtkid_1683378325024"
    PASSWORD = "Pro33160900"


    @staticmethod
    def get_password_auth_page(browser):
        code_auth_page = AuthByCodePages(browser).open()
        pass_auth_page = code_auth_page.click_on_enter_with_password_btn()
        return pass_auth_page

    @pytest.mark.xfail(reason="Текст не соответствует ожидаемому результату")
    def test_check_tabs_names(self, browser):
        pass_auth_page = self.get_password_auth_page(browser)
        assert pass_auth_page.number_tab().text == 'Номер'
        assert pass_auth_page.email_tab().text == "Почта"
        assert pass_auth_page.login_tab().text == "Логин"
        assert pass_auth_page.login_ls().text == "Лицевой счёт"

    def test_default_active_tab(self, browser):
        pass_auth_page = self.get_password_auth_page(browser)
        assert 'rt-tab--active' in pass_auth_page.number_tab().get_attribute('class')

    def test_move_to_register_page(self, browser):
        pass_auth_page = self.get_password_auth_page(browser)
        register_page = pass_auth_page.click_on_register_page()
        register_page.should_have_title('Регистрация')

    def test_move_to_restore_page(self, browser):
        pass_auth_page = self.get_password_auth_page(browser)
        restore_page = pass_auth_page.click_on_restore_page()
        restore_page.should_have_title('Восстановление пароля')

    def test_positive_login(self, browser):
        pass_auth_page = self.get_password_auth_page(browser)
        pass_auth_page.login_tab().click()
        personal_account_page = pass_auth_page.fill_login_form(self.LOGIN, self.PASSWORD)
        personal_account_page.url_should_have("https://start.rt.ru/?tab=main")

    def test_login_with_not_existing_email(self, browser):
        pass_auth_page = self.get_password_auth_page(browser)
        pass_auth_page.email_tab().click()
        pass_auth_page.fill_login_form('test777@gamil.com', self.PASSWORD, is_valid=False)
        assert pass_auth_page.error_msg().text == 'Неверный логин или пароль'

    def test_show_password(self, browser):
        pass_auth_page = self.get_password_auth_page(browser)
        assert pass_auth_page.password_field().get_attribute('type') == 'password'
        pass_auth_page.password_field().send_keys('123456')
        pass_auth_page.show_password_btn().click()
        assert pass_auth_page.password_field().get_attribute('type') == 'text'

    @pytest.mark.parametrize('email', ('test@', 'test@gmail.'))
    def test_validate_email_field(self, browser, email):
        pass_auth_page = self.get_password_auth_page(browser)
        pass_auth_page.email_tab().click()
        pass_auth_page.fill_login_form(email, self.PASSWORD, is_valid=False)
        assert pass_auth_page.error_msg().text == 'Неверный логин или пароль'








