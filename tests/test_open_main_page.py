# from pages.main_page import MainPage
# from pages.page_urls import PageUrls


# def test_open_main_page(driver):
#     """Тест на открытие главной страницы"""
#     mp = MainPage(driver)
#     # Переход на главную страницу
#     mp.go_to_base_url()
#     mp.assert_url(PageUrls.URL_BASE_PAGE)


# def test_user_autentification(driver):
#     """Тест аутентификации пользователя"""
#     mp = MainPage(driver)
#     # Переход на главную страницу
#     mp.go_to_base_url()
#     # Аутентификация пользователя
#     mp.autentification()


# def test_main_menu(driver):
#     """Тест кнопки главного меню"""
#     mp = MainPage(driver)
#     # Переход на главную страницу
#     mp.go_to_base_url()
#     # Переход на страницу главного меню
#     mp.go_to_main_menu()


# def test_search_field(driver):
#     """Тест поля пользовательского поиска"""
#     mp = MainPage(driver)
#     # Переход на главную страницу
#     mp.go_to_base_url()
#     # Заполнение строки поиска
#     mp.send_search_text("Одежда")
#     mp.go_to_base_url()
#     mp.send_search_text("select title, text from users where id=10 or 1=1")


# def test_buy_product(driver):
#     mp = MainPage(driver)
#     # Переход на главную страницу
#     mp.go_to_base_url()
#     # Аутентификация пользователя
#     mp.autentification()
#     mp.go_to_navbar_category("Одежда")
#     mp.go_to_cart()


# def test_navbar(driver):
#     mp = MainPage(driver)
#     # Переход на главную страницу
#     mp.go_to_base_url()
#     # Проверка навигационного бара
#     mp.check_navbar_links()
