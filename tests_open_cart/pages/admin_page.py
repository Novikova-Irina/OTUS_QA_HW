from selenium.webdriver.common.by import By
from .base_page import BasePage
from ..tests.constant import Consts


class AdminLoginPage(BasePage):
    username = (By.ID, 'input-username')
    password = (By.ID, 'input-password')
    submit_button = (By.CSS_SELECTOR, 'button')
    logout = (By.CSS_SELECTOR, '#header > div > ul > li:nth-child(2) > a')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.base_url = Consts.ADMIN_PAGE

    def _set_username_(self, name):
        self.find_element(locator=self.username).clear()
        self.find_element(locator=self.username).send_keys(name)

    def _set_password_(self, password):
        self.find_element(locator=self.password).clear()
        self.find_element(locator=self.password).send_keys(password)

    def login(self, username, password):
        self._set_username_(username)
        self._set_password_(password)
        self.find_element(locator=self.submit_button).click()

    def _logout(self):
        self.find_element(locator=self.logout).click()

    def go_to_product_card_page(self):
        return self.driver.get(Consts.CATALOG_PAGE)
