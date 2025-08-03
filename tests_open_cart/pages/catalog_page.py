from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests_open_cart.pages.base_page import BasePage
from tests_open_cart.tests.constant import Consts


class Catalog(BasePage):

    def __init__(self, driver, base_url=Consts.CATALOG_PAGE):
        super().__init__(driver)
        self.driver = driver
        self.base_url = base_url

    def check_title(self, text_of_title, time=10):
        return WebDriverWait(self.driver, time).until(EC.title_is(text_of_title),
                message=f"Can't find title{text_of_title}")
