from selenium.webdriver.common.by import By
from .base_page import BasePage
from ..tests.constant import Consts


class LoginPage(BasePage):
    email = (By.ID, 'input-email')
    password = (By.ID, 'input-password')
    submit_button = (By.CSS_SELECTOR, '#content > div > div:nth-child(2) > div > form > input')
    new_customer = (By.CSS_SELECTOR, '#content > div > div:nth-child(1) > div > a')

    def __init__(self, driver, base_url=Consts.LOGIN_PAGE):
        super().__init__(driver)
        self.driver = driver
        self.base_url = base_url

    def _set_email(self, email):
        self.find_element(locator=self.email).clear()
        self.find_element(locator=self.email).send_keys(email)

    def _set_password_(self, password):
        self.find_element(locator=self.password).clear()
        self.find_element(locator=self.password).send_keys(password)

    def login(self, email, password):
        self._set_email(email)
        self._set_password_(password)
        self.find_element(locator=self.submit_button).click()

    def register_account(self):
        return self.find_element(locator=self.new_customer).click()
