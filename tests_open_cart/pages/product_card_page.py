from tests_open_cart.pages.base_page import BasePage
from tests_open_cart.tests.constant import Consts


class ProductCardPage(BasePage):

    def __init__(self, driver, base_url=Consts.PRODUCT_CARD_PAGE):
        super().__init__(driver)
        self.driver = driver
        self.base_url = base_url
