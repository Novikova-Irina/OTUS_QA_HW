import pytest
from selenium import webdriver
from .pages.admin_page import AdminLoginPage
from .pages.base_page import BasePage
from .pages.catalog_page import Catalog
from .pages.login_page import LoginPage
from .pages.product_card_page import ProductCardPage


def pytest_addoption(parser):
    """
    Ключи для запуска браузера
    --browser: chrome/firefox - браузер для тестирования
    """
    parser.addoption('--browser', action='store', default='chrome')


@pytest.fixture()
def browser(request):
    """
    Инициализация веб драйвера в зависимости от ключа "--browser"
    :return: объект класса webdriver
    """
    browser = request.config.getoption('--browser')
    if browser == 'firefox':
        driver = webdriver.Firefox()
    elif browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'IE':
        driver = webdriver.Ie()
    else:
        raise Exception("Incorrect browser name")
    driver.maximize_window()
    yield driver
    driver.quit()
    return


@pytest.fixture()
def base_page(browser):
    page = BasePage(browser)
    page.go_to()
    return page


@pytest.fixture()
def admin_page(browser):
    page = AdminLoginPage(browser)
    page.go_to()
    return page


@pytest.fixture()
def catalog(browser):
    page = Catalog(browser)
    page.go_to()
    return page


@pytest.fixture()
def product_page(browser):
    page = ProductCardPage(browser)
    page.go_to()
    return page


@pytest.fixture()
def login_page(browser):
    page = LoginPage(browser)
    page.go_to()
    return page
