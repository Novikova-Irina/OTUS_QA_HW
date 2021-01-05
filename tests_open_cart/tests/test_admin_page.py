import allure
import pytest


class TestSuite(object):

    @pytest.mark.parametrize("login, password", [
        ('demo', 'demo'),
        ('#', '?'),
        (1, 2)
    ])
    def test_success_login(self, admin_page, login, password):
        with allure.step(f"Логинится на любую комбинацию"):
            admin_page.login(login, password)
        assert admin_page.driver.title == 'Dashboard'

    def test_incorrect_login(self, admin_page):
        with allure.step(f"Логин, разлогин и проверка, что снова доступна страница с title = 'Administration'"):
            admin_page.login('test', 'test')
        with allure.step(f"Logout"):
            admin_page._logout()
        assert admin_page.driver.title == 'Administration'

    def test_go_to_product_card_page(self, admin_page):
        with allure.step(f"Проверка перехода к разделу с товарами. Появляется таблица с товарами"):
            admin_page.go_to_product_card_page()
        assert admin_page.driver.title == 'Desktops'
