from pages.base_page import BasePage
from selenium.webdriver.common.by import By

from pages.personal_account_page import PersonalAccountPage
from pages.register_page import RegisterPage
from pages.restore_password_page import RestorePage


class AuthByPasswordPage(BasePage):

    def number_tab(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#t-btn-tab-phone")

    def email_tab(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#t-btn-tab-mail")

    def login_tab(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#t-btn-tab-login")

    def login_ls(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#t-btn-tab-ls")

    def register_link(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#kc-register")

    def restore_link(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#forgot_password")

    def login_field(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#username")

    def password_field(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#password")

    def login_btn(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#kc-login")

    def error_msg(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#form-error-message")

    def show_password_btn(self):
        return self.driver.find_element(By.XPATH, "(//div[@class='rt-input__action'])[2]")

    def click_on_register_page(self) -> RegisterPage:
        self.register_link().click()
        return RegisterPage(self.driver)

    def click_on_restore_page(self) -> RestorePage:
        self.restore_link().click()
        return RestorePage(self.driver)

    def fill_login_form(self, login: str, password: str, is_valid=True) -> PersonalAccountPage:
        self.login_field().send_keys(login)
        self.password_field().send_keys(password)
        self.login_btn().click()
        if is_valid:
            return PersonalAccountPage(self.driver)
        return self
