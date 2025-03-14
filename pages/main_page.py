import time
from selenium.webdriver.common.by import By

from base.base_class import Base
from .page_urls import PageUrls
from components.header import HeaderComponent


class MainPageLocators:
    """Класс содержит локаторы применяемые на главной странице"""

    LOCATOR_AUTH_PHONE_FIELD = (By.NAME, "phone")
    LOCATOR_AUTH_PASS_FIELD = (By.NAME, "password")
    LOCATOR_AUTH_FORM_BUTTON = (By.CLASS_NAME, "full-width-button")


class MainPage(Base):
    """Класс главной страницы"""

    def __init__(self, driver):
        super().__init__(driver)

        self.header_component = HeaderComponent(driver)

    # Геттеры

    def get_auth_phone_field(self):
        print("Получение локатора поля ввода Phone")
        return self.get_element(20, MainPageLocators.LOCATOR_AUTH_PHONE_FIELD)

    def get_auth_pass_field(self):
        print("Получение локатора поля пароля")
        return self.get_element(20, MainPageLocators.LOCATOR_AUTH_PASS_FIELD)

    def get_auth_form_submit_button(self):
        print("Получение локатора кнопки Submit формы аутентификации")
        return self.get_element(20, MainPageLocators.LOCATOR_AUTH_FORM_BUTTON)

    # Действия

    def input_phone_number(self):
        self.get_auth_phone_field().send_keys("satrey.mail@gmail.com")
        print("Ввод email адреса в форму аутентификации пользователя")

    def input_pass(self):
        self.get_auth_pass_field().send_keys("Blizko")
        print("Ввод пароля в форму аутентификации пользователя")

    def click_auth_form_submit_button(self):
        self.get_auth_form_submit_button().submit()
        print("Клик на кнопке Submit формы аутентификации")

    # Методы

    def go_to_base_url(self):
        self.driver.get(PageUrls.URL_BASE_PAGE)
        time.sleep(2)

    def go_to_main_menu(self):
        self.header_component.click_menu_button()
        time.sleep(2)

    def go_to_cart(self):
        self.header_component.click_cart_button()
        time.sleep(2)

    def send_search_text(self, search_text):
        self.header_component.input_search_text(search_text)
        self.header_component.click_search_button()
        time.sleep(2)

    def autentification(self):
        self.header_component.click_login_button()
        time.sleep(2)
        self.input_phone_number()
        time.sleep(2)
        self.input_pass()
        self.click_auth_form_submit_button()
        time.sleep(2)

    def check_navbar_links(self):
        navbar = self.header_component.get_portal_nav_list()
        for link_text in navbar:
            self.header_component.click_portal_nav_link(link_text)
            time.sleep(2)

    def go_to_navbar_category(self, category):
        navbar = self.header_component.get_portal_nav_list()
        assert category in navbar, "В меню нет такой категории"
        self.header_component.click_portal_nav_link(category)
        time.sleep(2)
