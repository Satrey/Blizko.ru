from pages.main_page import MainPage
from pages.page_urls import PageUrls


def test_smoke(driver):
    mp = MainPage(driver)
    mp.go_to_base_url()
    mp.go_to_navbar_category("Техника")
    mp.assert_url(PageUrls.URL_TEHNIKA_PAGE)
    mp.select_category("Компьютеры")
    mp.select_category("Ноутбуки и комплектующие")
    mp.select_category("Ноутбуки")


# def test_buy_product(driver):
#     mp = MainPage(driver)
#     # Переход на главную страницу
#     mp.go_to_base_url()
#     # Аутентификация пользователя
#     mp.autentification()
#     mp.go_to_navbar_category("Одежда")
#     mp.go_to_cart()
