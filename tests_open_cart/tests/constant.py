

class Consts(object):

    u"""Константы для работы с веб-браузером."""

    BASE_URL = 'https://demo.opencart.com/'
    ADMIN_SUFFIX = 'admin/'
    CATALOG_SUFFIX = '/index.php?route=product/category&path=20'
    PRODUCT_CARD_SUFFIX = '/index.php?route=product/product&path=57&product_id=49'
    LOGIN_SUFFIX = '/index.php?route=account/login'
    CART_CHECKOUT_SUFFIX = '/index.php?route=checkout/cart'
    ADMIN_PAGE = BASE_URL + ADMIN_SUFFIX
    CATALOG_PAGE = BASE_URL + CATALOG_SUFFIX
    PRODUCT_CARD_PAGE = BASE_URL + PRODUCT_CARD_SUFFIX
    LOGIN_PAGE = BASE_URL + LOGIN_SUFFIX
    CART_CHECKOUT = BASE_URL + CART_CHECKOUT_SUFFIX
