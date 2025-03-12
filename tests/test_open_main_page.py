from pages.main_page import MainPage

""" Тест на открытие главной страницы """


def test_open_main_page(driver):
    mp = MainPage(driver)
    # Переход на главную страницу
    mp.go_to_base_url()


""" Тест аутентификации пользователя """


def test_user_autentification(driver):
    mp = MainPage(driver)
    # Переход на главную страницу
    mp.go_to_base_url()
    # Аутентификация пользователя
    mp.autentification()


""" Тест кнопки главного меню """


def test_main_menu(driver):
    mp = MainPage(driver)
    # Переход на главную страницу
    mp.go_to_base_url()
    # Переход на страницу главного меню
    mp.go_to_main_menu()


""" Тест кнопки карзины """


def test_cart_button(driver):
    mp = MainPage(driver)
    # Переход на главную страницу
    mp.go_to_base_url()
    # Переход на страницу карзины
    mp.go_to_cart()


""" Тест поля пользовательского поиска """


def test_search_field(driver):
    mp = MainPage(driver)
    # Переход на главную страницу
    mp.go_to_base_url()
    # Заполнение строки поиска
    mp.send_search_text()


# def test_buy_product(driver):
#     mp = MainPage(driver)
#     # Переход на главную страницу
#     mp.go_to_base_url()
#     mp.autentification()
#     mp.go_to_main_menu()
#     mp.input_search_text()
#     mp.go_to_cart()
