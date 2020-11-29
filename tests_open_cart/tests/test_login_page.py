from selenium.webdriver.common.by import By


class TestSuite(object):

    def test_try_login(self, login_page):
        login_page.login('demo', 'demo')
        assert login_page.driver.title == 'Account Login'

    def test_new_customer(self, login_page):
        login_page.register_account()
        assert login_page.driver.title == 'Register Account'

    def test_negative_login(self, login_page):
        login_page.login('t', 'r')
        assert login_page.driver.title != 'Dashboard'

    def test_find_element_by_class_name(self, login_page):
        assert login_page.find_element_by_class_name(name_of_class='breadcrumb')

    def test_find_element_by_css(self, login_page):
        assert login_page.find_element(locator=(By.CSS_SELECTOR, '#column-right > div > a:nth-child(6)'))
