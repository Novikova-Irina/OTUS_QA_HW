import allure
from selenium.webdriver.common.by import By


class TestCatalogPage(object):
    def test_check_title(self, catalog):
        assert catalog.driver.title == 'Desktops'

    def test_check_method_check_title(self, catalog):
        assert catalog.check_title('Desktops')

    def test_find_element_by_css(self, catalog):
        canon_eos_5d = (By.CSS_SELECTOR, '#content > div:nth-child(2) > div.col-sm-2 > img')
        with allure.step(f"Поиск элемента и клик по элементу {canon_eos_5d}"):
            catalog.find_element(locator=canon_eos_5d).click()
        assert catalog.check_title('Desktops')

    def test_find_element_by_class_name_1(self, catalog):
        assert catalog.find_element_by_class_name(name_of_class='list-group-item')

    def test_find_element_by_class_name_2(self, catalog):
        assert catalog.find_element_by_class_name(name_of_class='product-thumb')

    def test_click_list_group_item(self, catalog):
        laptop_and_notebooks = (By.CSS_SELECTOR, '#column-left > div.list-group > a:nth-child(4)')
        with allure.step(f"Поиск элемента и клик по элементу {laptop_and_notebooks}"):
            catalog.find_element(locator=laptop_and_notebooks).click()
        assert catalog.check_title('Laptops & Notebooks')

    def test_click_tablets_button_and_add_to_wishlist(self, catalog):
        tablets = (By.CSS_SELECTOR, '#menu > div.collapse.navbar-collapse.navbar-ex1-collapse > ul > li:nth-child(4) > a')
        with allure.step(f"Выбор в меню {tablets}"):
            catalog.find_element(locator=tablets).click()
        samsung_galaxy_tab = (By.CSS_SELECTOR, '[data-original-title="Add to Wish List"]')
        with allure.step(f"Поиск элемента и добавление в WishList {samsung_galaxy_tab}"):
            catalog.find_element(locator=samsung_galaxy_tab).click()
        assert catalog.check_title('Tablets')
