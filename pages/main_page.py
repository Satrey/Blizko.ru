import time
from selenium.webdriver.common.by import By

from base.base_class import Base


class BasePageLocators:
    """Класс содержит локаторы применяемые на главной странице"""

    URL_BASE_PAGE = "https://tyumen.blizko.ru/"

    LOCATOR_AUTH_BUTTON = (By.XPATH, '//*[@id="open-auth-popup"]')
    LOCATOR_CART_BUTTON = (By.XPATH, '//ul[@class="header-navigation-links"]/li[2]')

    LOCATOR_MENU_BUTTON = (By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/button")
    LOCATOR_PUR_BUTTON = (By.XPATH, '//ul[@class="header-navigation-links"]/li[0]')
    LOCATOR_FAVORITE_BUTTON = (By.XPATH, '//ul[@class="header-navigation-links"]/li[1]')

    LOCATOR_SEARCH_FIELD = (By.XPATH, '//input[@name="q"]')
    LOCATOR_SEARSH_BUTTON = (By.CLASS_NAME, "header-search-form__submit")

    LOCATOR_AUTH_PHONE_FIELD = (By.NAME, "phone")
    LOCATOR_AUTH_FORM_BUTTON = (By.CLASS_NAME, "full-width-button")


class MainPage(Base):
    """Класс главной страницы"""

    # Геттеры

    def get_login_button(self):
        print("Получение локатора кнопки Войти")
        return self.get_element(20, BasePageLocators.LOCATOR_AUTH_BUTTON)

    def get_menu_button(self):
        print("Получение локатора кнопки Меню")
        return self.get_element(20, BasePageLocators.LOCATOR_MENU_BUTTON)

    def get_cart_button(self):
        print("Получение локатора кнопки Карзины")
        return self.get_element(20, BasePageLocators.LOCATOR_CART_BUTTON)

    def get_puchases_button(self):
        print("Получение локатора кнопки Карзины")
        return self.get_element(20, BasePageLocators.LOCATOR_PURCHASES_BUTTON)

    def get_favorite_button(self):
        print("Получение локатора кнопки Карзины")
        return self.get_element(20, BasePageLocators.LOCATOR_FAVORITE_BUTTON)

    def get_search_field(self):
        print("Получение локатора поля Search")
        return self.get_element(20, BasePageLocators.LOCATOR_SEARCH_FIELD)

    def get_searh_button(self):
        print("Получение локатора кнопки Search")
        return self.get_element(20, BasePageLocators.LOCATOR_SEARSH_BUTTON)

    def get_auth_phone_field(self):
        print("Получение локатора поля ввода Phone")
        return self.get_element(20, BasePageLocators.LOCATOR_AUTH_PHONE_FIELD)

    def get_auth_form_submit_button(self):
        print("Получение локатора кнопки Submit формы аутентификации")
        return self.get_element(20, BasePageLocators.LOCATOR_AUTH_FORM_BUTTON)

    # Действия

    def click_login_button(self):
        self.get_login_button().click()
        print("Клик на кнопке Login")

    def click_menu_button(self):
        self.get_menu_button().click()
        print("Клик на кнопке Menu")

    def click_cart_button(self):
        self.get_cart_button().click()
        print("Клик на кнопке Карзины")

    def click_search_button(self):
        self.get_searh_button().submit()
        print("Клик на кнопке Поиск")

    def input_search_text(self):
        self.get_search_field().send_keys("Компьютеры")
        print("Ввод текста в поле поиска")

    def input_phone_number(self):
        self.get_auth_phone_field().send_keys("satrey.mail@gmail.com")
        print("Ввод email адреса в форму аутентификации пользователя")

    def click_auth_phone_submit_button(self):
        self.get_auth_form_submit_button().submit()
        print("Клик на кнопке Submit формы аутентификации")

    # Методы

    def go_to_base_url(self):
        self.driver.get(BasePageLocators.URL_BASE_PAGE)
        self.driver.maximize_window()
        time.sleep(5)

    def go_to_main_menu(self):
        self.click_menu_button()
        time.sleep(10)

    def go_to_cart(self):
        self.click_cart_button()
        time.sleep(10)

    def send_search_text(self):
        self.input_search_text()
        self.click_search_button()
        time.sleep(10)

    def autentification(self):
        self.click_login_button()
        time.sleep(10)
        self.input_phone_number()
        self.click_auth_phone_submit_button()
        time.sleep(10)
