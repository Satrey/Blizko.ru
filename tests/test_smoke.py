import time

from pages.main_page import MainPage
from pages.page_urls import PageUrls


def test_smoke(driver):
    mp = MainPage(driver)
    mp.go_to_base_url()
    mp.go_to_navbar_category("Техника")
    time.sleep(2)
    mp.assert_url(PageUrls.URL_TEHNIKA_CATEGORY_PAGE)
    mp.select_category("Компьютеры")
    mp.assert_url(PageUrls.URL_COMPUTER_CATEGORY_PAGE)
    mp.select_category("Ноутбуки и комплектующие")
    mp.assert_url(PageUrls.URL_NOTEBOOK_CATEGORY_PAGE)
    mp.select_category("Ноутбуки")
    mp.assert_url(PageUrls.URL_NOTEBOOK_ITEM_PAGE)
    mp.select_product("Ноутбук ACD 15S G2, 15.6")
    mp.go_to_cart()
    time.sleep(5)


# def test_buy_product(driver):
#     mp = MainPage(driver)
#     # Переход на главную страницу
#     mp.go_to_base_url()
#     # Аутентификация пользователя
#     mp.autentification()
#     mp.go_to_navbar_category("Одежда")
