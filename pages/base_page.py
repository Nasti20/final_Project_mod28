from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver: webdriver.Chrome, timeout=5):
        self.driver = driver
        self.url = None
        self.driver.implicitly_wait(timeout)

    def open(self):
        self.driver.get(self.url)
        return self

    def url_should_have(self, url: str):
        assert WebDriverWait(self.driver, 5).until(EC.url_to_be(url)), \
            f'Неверный URL адрес страницы ожидаемый: {url}, фактический: {self.driver.current_url}'

    def title(self):
        return self.driver.find_element(By.CSS_SELECTOR, "h1.card-container__title")

    def should_have_title(self, text):
        assert self.title().text == text, 'Не корректная страница'
