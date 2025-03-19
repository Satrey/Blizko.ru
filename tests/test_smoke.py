import time

from pages.main_page import MainPage
from pages.page_urls import PageUrls


def test_buy_product(driver):
    mp = MainPage(driver)
    # Переход на главную страницу
    mp.go_to_base_url()
    mp.assert_url(PageUrls.URL_BASE_PAGE)
    # Аутентификация пользователя
    mp.autentification()
    mp.go_to_navbar_category("Одежда")
    time.sleep(5)
    mp.assert_url(PageUrls.URL_ODEZHDA_PAGE)


def test_smoke(driver):
    mp = MainPage(driver)
    # Переход на главную страницу
    mp.go_to_base_url()
    mp.assert_url(PageUrls.URL_BASE_PAGE)
    # переход в категорию "Техника"
    mp.go_to_navbar_category("Техника")
    time.sleep(5)
    mp.assert_url(PageUrls.URL_TEHNIKA_CATEGORY_PAGE)
    # переход в категорию "Компьютеры"
    mp.select_category("Компьютеры")
    mp.assert_url(PageUrls.URL_COMPUTER_CATEGORY_PAGE)
    # переход в категорию "Ноутбуки и комплектующие"
    mp.select_category("Ноутбуки и комплектующие")
    mp.assert_url(PageUrls.URL_NOTEBOOK_CATEGORY_PAGE)
    # переход в категорию "Ноутбуки"
    mp.select_category("Ноутбуки")
    mp.assert_url(PageUrls.URL_NOTEBOOK_ITEM_PAGE)
    # Выбор товара по наименованию
    mp.select_product("Ноутбук ACD 15S G2, 15.6")
    # Переход на страницу товара и добавление в корзину
    mp.go_to_cart()
    # Переход к оформлению товара
    time.sleep(5)
    mp.go_to_confirm_by()
    time.sleep(15)
