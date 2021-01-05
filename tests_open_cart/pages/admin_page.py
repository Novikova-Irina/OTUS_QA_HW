import allure
from selenium.webdriver.common.by import By
from .base_page import BasePage
from ..tests.constant import Consts


class AdminLoginPage(BasePage):
    username = (By.ID, 'input-username')
    password = (By.ID, 'input-password')
    submit_button = (By.CSS_SELECTOR, 'button')
    logout = (By.CSS_SELECTOR, '#header > div > ul > li:nth-child(2) > a')

    @allure.step("Запускаю страницу браузера {driver}")
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.base_url = Consts.ADMIN_PAGE

    @allure.step("Ввожу имя {name}")
    def _set_username_(self, name):
        self.find_element(locator=self.username).clear()
        self.find_element(locator=self.username).send_keys(name)

    @allure.step("Ввожу пароль {password}")
    def _set_password_(self, password):
        self.find_element(locator=self.password).clear()
        self.find_element(locator=self.password).send_keys(password)

    @allure.step("Ввожу логин {username} и пароль {password} и кликаю submit_button")
    def login(self, username, password):
        self._set_username_(username)
        self._set_password_(password)
        self.find_element(locator=self.submit_button).click()

    @allure.step("Logout")
    def _logout(self):
        self.find_element(locator=self.logout).click()

    @allure.step("Переход на страницу PRODUCT_CATALOG_PAGE")
    def go_to_product_card_page(self):
        return self.driver.get(Consts.CATALOG_PAGE)
