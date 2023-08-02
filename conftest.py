import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--browser_name", action='store', default='chrome')


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption('browser_name')
    if browser_name == 'chrome':
        print('Start browser was started')
        options = Options()
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.implicitly_wait(5)
    else:
        raise pytest.UsageError("--browser_name should have name chrome or firefox")
    yield driver
    print('Browser was closed')
