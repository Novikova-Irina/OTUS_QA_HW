from selenium.webdriver.common.by import By


class TestCatalogPage(object):
    def test_check_title(self, catalog):
        assert catalog.driver.title == 'Desktops'

    def test_check_method_check_title(self, catalog):
        assert catalog.check_title('Desktops')

    def test_find_element_by_css(self, catalog):
        canon_eos_5d = (By.CSS_SELECTOR, '#content > div:nth-child(2) > div.col-sm-2 > img')
        click_element = catalog.find_element(locator=canon_eos_5d)
        click_element.click()
        # Здесь не поняла, почему я кликаю, а перехода на другую страницу нет. Что надо сделать?
        assert catalog.check_title('Desktops')

    def test_find_element_by_class_name_1(self, catalog):
        assert catalog.find_element_by_class_name(name_of_class='list-group-item')

    def test_find_element_by_class_name_2(self, catalog):
        assert catalog.find_element_by_class_name(name_of_class='product-thumb')
