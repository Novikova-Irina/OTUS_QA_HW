from selenium.webdriver.common.by import By

from tests_open_cart.tests.constant import Consts


class TestBasePage(object):
    def test_check_base_page(self, base_page):
        """Тест, который открывает основную страницу opencart (http://<ip_or_fqdn>/opencart/) и проверяет,
                что мы находимся именно на странице приложения opencart."""
        assert base_page.driver.title == 'Your Store'

    def test_check_page_by_method(self, base_page):
        """Тест, который открывает основную страницу opencart (http://<ip_or_fqdn>/opencart/) и проверяет,
                что мы находимся именно на странице приложения opencart."""
        assert base_page.check_url(Consts.BASE_URL)

    def test_base_page_find_element(self, base_page):
        """Поиск элемента по CSS_SELECTOR'у"""
        assert base_page.search()

    def test_find_element_by_css(self, base_page):
        assert base_page.find_element(locator=(By.CSS_SELECTOR, '#carousel0 > div > div:nth-child(13) > img'))

    def test_go_to_product_card_page(self, base_page):
        """Поиск элемента по class name"""
        assert base_page.find_element_by_class_name(name_of_class='swiper-pager')
