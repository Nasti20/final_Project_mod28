from pages.auth_by_password_page import AuthByPasswordPage
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class AuthByCodePages(BasePage):
    BASE_URL = 'https://lk.rt.ru/'

    def __init__(self, browser, timeout=5):
        super().__init__(browser, timeout)
        self.url = self.BASE_URL

    def enter_with_password_btn(self):
        return self.driver.find_element(By.CSS_SELECTOR, "button[name='standard_auth_btn']")

    def click_on_enter_with_password_btn(self) -> AuthByPasswordPage:
        self.enter_with_password_btn().click()
        return AuthByPasswordPage(self.driver)

