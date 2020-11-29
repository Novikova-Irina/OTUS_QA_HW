from selenium.webdriver.common.by import By
from tests_open_cart.tests.constant import Consts


class TestProductCard(object):

    def test_find_element_by_css_and_click(self, product_page):
        samsung_galaxy_tab_10_1 = (
            By.CSS_SELECTOR, '#content > div > div.col-sm-8 > ul.thumbnails > li:nth-child(1) > a')
        click_element = product_page.find_element(locator=samsung_galaxy_tab_10_1)
        click_element.click()
        assert product_page.driver.title == 'Samsung Galaxy Tab 10.1'

    def test_check_title(self, product_page):
        assert product_page.driver.title == 'Samsung Galaxy Tab 10.1'

    def test_find_element_by_css(self, product_page):
        assert product_page.find_element(locator=(By.CSS_SELECTOR, '#button-cart'))

    def test_go_to_base_page(self, product_page):
        product_page.go_to()  # метод из class BasePage
        assert product_page.check_url(Consts.BASE_URL)

    def test_find_element_by_css_click_go_to(self, product_page):
        software_button = product_page.find_element(locator=(
            By.CSS_SELECTOR, '#menu > div.collapse.navbar-collapse.navbar-ex1-collapse > ul > li:nth-child(5) > a'))
        software_button.click()
        assert product_page.driver.title == 'Software'
