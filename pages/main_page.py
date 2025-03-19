import time
from selenium.webdriver.common.by import By

from base.base_class import Base
from .page_urls import PageUrls
from components.header import HeaderComponent
from components.main import MainComponent
from components.popup_cart import CartPopupComponent


class MainPageLocators:
    """Класс содержит локаторы применяемые на главной странице"""

    LOCATOR_AUTH_PHONE_FIELD = (By.NAME, "phone")
    LOCATOR_AUTH_PASS_FIELD = (By.NAME, "password")
    LOCATOR_AUTH_FORM_BUTTON = (By.CLASS_NAME, "full-width-button")
    LOCATOR_PRODUCT_FULL_NAME = (
        By.XPATH,
        "/html/body/div[1]/div[8]/div[1]/div/h1/span",
    )


class MainPage(Base):
    """Класс главной страницы"""

    def __init__(self, driver):
        super().__init__(driver)

        # Создание компонентов страницы

        self.header_component = HeaderComponent(driver)
        self.main_component = MainComponent(driver)
        self.cart_popup_component = CartPopupComponent(driver)

    # Геттеры

    def get_auth_phone_field(self):
        """Метод получения поля Phone, формы аутентификации пользователя"""
        print("Получение локатора поля ввода Phone")
        return self.get_element(20, MainPageLocators.LOCATOR_AUTH_PHONE_FIELD)

    def get_auth_pass_field(self):
        """Метод получения поля Password, формы аутентификации пользователя"""
        print("Получение локатора поля пароля")
        return self.get_element(20, MainPageLocators.LOCATOR_AUTH_PASS_FIELD)

    def get_auth_form_submit_button(self):
        """Метод получения кнопки Submit, формы аутентификации пользователя"""
        print("Получение локатора кнопки Submit формы аутентификации")
        return self.get_element(20, MainPageLocators.LOCATOR_AUTH_FORM_BUTTON)

    # Действия

    def input_phone_number(self):
        """Заполнение поля phone/email, формы аутентификации пользователя"""
        self.get_auth_phone_field().send_keys("satrey.mail@gmail.com")
        print("Ввод email адреса в форму аутентификации пользователя")

    def input_pass(self):
        """Заполнение поля password, формы аутентификации пользователя"""
        self.get_auth_pass_field().send_keys("Blizko")
        print("Ввод пароля в форму аутентификации пользователя")

    def click_auth_form_submit_button(self):
        """Клик на кнопке Submit, формы аутентификации пользователя"""
        self.get_auth_form_submit_button().submit()
        print("Клик на кнопке Submit формы аутентификации")

    # Методы

    def go_to_base_url(self):
        """Переход на главную страницу проекта"""
        self.driver.get(PageUrls.URL_BASE_PAGE)
        time.sleep(2)

    def go_to_main_menu(self):
        """Переход в главное меню проекта"""
        self.header_component.click_menu_button()
        time.sleep(2)

    def go_to_cart_from_header(self):
        """Переход в корзину через кнопку корзина в заголовке страницы"""
        self.header_component.click_cart_button()
        time.sleep(2)

    def send_search_text(self, search_text):
        """Заполнение поля поиск, в хэдере главной страницы"""
        self.header_component.input_search_text(search_text)
        time.sleep(2)
        self.header_component.click_search_button()
        time.sleep(2)

    def autentification(self):
        """Аутентификация пользователя"""
        self.header_component.click_login_button()
        self.input_phone_number()
        time.sleep(2)
        self.input_pass()
        time.sleep(2)
        self.click_auth_form_submit_button()
        time.sleep(2)

    def check_navbar_links(self):
        """Проверка ссылок навигационного меню в заголовке страницы"""
        navbar = self.header_component.get_portal_nav_list()
        for link_text in navbar:
            self.header_component.click_portal_nav_link(link_text)
            time.sleep(2)

    def go_to_navbar_category(self, category):
        """Переход по заданной категории товара, в навигационном меню"""
        navbar = self.header_component.get_portal_nav_list()
        assert category in navbar, "В меню нет такой категории"
        self.header_component.click_portal_nav_link(category)

    def select_category(self, category: str):
        """Выбор заданной категории товара в главном компоненте страницы"""
        self.main_component.click_category(category)

    def select_product(self, product: str):
        """Выбор заданного товара текущей категории в главном компоненте"""
        self.main_component.click_product(product)

    def go_to_market(self):
        """Не используется"""
        self.main_component.click_market_button()

    def go_to_cart(self):
        """Переход в корзину для оформления покупки"""
        self.main_component.click_add_to_cart_button()
        self.cart_popup_component.click_popup_cart_confirm_button()

    def go_to_back(self):
        """Возврат в магазин для продолжения покупок"""
        self.main_component.click_add_to_cart_button()
        self.cart_popup_component.click_popup_cart_back_button()

    def go_to_confirm_by(self):
        """Переход на страницу завершения оформления заказа"""
        self.main_component.click_confirm_cart_button()
