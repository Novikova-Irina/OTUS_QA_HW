from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests_open_cart.tests.constant import Consts


class BasePage(object):
    submit_button = (By.CSS_SELECTOR, '#search > input')

    def __init__(self, driver, base_url=Consts.BASE_URL):
        self.driver = driver
        self.base_url = base_url

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def search(self):
        return self.find_element(locator=self.submit_button)

    def go_to(self):
        return self.driver.get(self.base_url)

    def go_to_url(self, url):
        return self.driver.get(url)

    def check_url(self, url, time=10):
        return WebDriverWait(self.driver, time).until(EC.url_matches(url))

    def find_element_by_class_name(self, name_of_class, time=10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located((By.CLASS_NAME, name_of_class)))
