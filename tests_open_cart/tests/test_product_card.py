import allure
from selenium.webdriver.common.by import By
from tests_open_cart.tests.constant import Consts


class TestProductCard(object):
    SAMSUNG_GALAXY_TAB = (By.CSS_SELECTOR, '#button-cart')

    def test_find_element_by_css_and_click(self, product_page):
        samsung_galaxy_tab_10_1 = (
            By.CSS_SELECTOR, '#content > div > div.col-sm-8 > ul.thumbnails > li:nth-child(1) > a')
        with allure.step(f"Поиск элемента и клик по элементу {samsung_galaxy_tab_10_1}"):
            product_page.find_element(locator=samsung_galaxy_tab_10_1).click()
        assert product_page.driver.title == 'Samsung Galaxy Tab 10.1'

    def test_check_title(self, product_page):
        assert product_page.driver.title == 'Samsung Galaxy Tab 10.1'

    def test_find_element_by_css(self, product_page):
        assert product_page.find_element(locator=self.SAMSUNG_GALAXY_TAB)

    def test_go_to_base_page(self, product_page):
        with allure.step(f"Переход на страницу BasePage"):
            product_page.go_to()  # метод из class BasePage
        assert product_page.check_url(Consts.BASE_URL)

    def test_find_element_by_css_click_go_to(self, product_page):
        software_button = product_page.find_element(locator=(
            By.CSS_SELECTOR, '#menu > div.collapse.navbar-collapse.navbar-ex1-collapse > ul > li:nth-child(5) > a'))
        with allure.step(f"Клик по элементу {software_button}"):
            software_button.click()
        assert product_page.driver.title == 'Software'

    def test_add_to_wishlist(self, product_page):
        """Добавление продукта 'Samsung Galaxy Tab 10.1' в WishList """
        samsung_galaxy_tab = (By.CSS_SELECTOR, '[data-original-title="Add to Wish List"]')
        with allure.step(f"Поиск элемента {samsung_galaxy_tab}"):
            click_element = product_page.find_element(locator=samsung_galaxy_tab)
        with allure.step(f"Добавление элемента в WishList"):
            click_element.click()
        assert click_element.tag_name == 'button'

    def test_add_to_cart(self, product_page):
        """Добавление продукта 'Samsung Galaxy Tab 10.1' в Корзину """
        with allure.step(f"Поиск элемента {self.SAMSUNG_GALAXY_TAB}"):
            click_element = product_page.find_element(locator=self.SAMSUNG_GALAXY_TAB)
        with allure.step(f"Добавление элемента в Корзину"):
            click_element.click()
        assert click_element.tag_name == 'button'

    def test_add_product_to_cart_and_check_cart(self, product_page):
        with allure.step(f"Поиск элемента и клик по: {self.SAMSUNG_GALAXY_TAB}"):
            product_page.find_element(locator=self.SAMSUNG_GALAXY_TAB).click()
        with allure.step(f"Переход на страницу {Consts.CART_CHECKOUT}"):
            product_page.go_to_url(Consts.CART_CHECKOUT)
        assert product_page.driver.title == 'Shopping Cart'
