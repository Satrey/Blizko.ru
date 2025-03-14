from selenium.webdriver.common.by import By
from base.base_class import Base


class HeaderComponentLocators:
    """Класс содержит локаторы используемые для поиска элементов в компоненте заголовка"""

    # Локаторы

    LOCATOR_AUTH_BUTTON = (By.XPATH, '//*[@id="open-auth-popup"]')
    LOCATOR_MENU_BUTTON = (By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/button")
    LOCATOR_PUR_BUTTON = (By.XPATH, '//ul[@class="header-navigation-links"]/li[0]')
    LOCATOR_FAVORITE_BUTTON = (By.XPATH, '//ul[@class="header-navigation-links"]/li[1]')
    LOCATOR_CART_BUTTON = (By.XPATH, '//ul[@class="header-navigation-links"]/li[3]')
    LOCATOR_SEARCH_FIELD = (By.XPATH, '//input[@name="q"]')
    LOCATOR_SEARSH_BUTTON = (By.XPATH, "//button[@class='header-search-form__submit']")
    LOCATOR_NAVBAR_LIST = (
        By.XPATH,
        "//*[@class='portal-nav']/ul[@class='pn-list']/li[@class='pn-item']",
    )


class HeaderComponent(Base):
    """Класс компонента шапки страницы"""

    # Геттеры

    def get_login_button(self):
        print("Получение локатора кнопки Войти")
        return self.get_element(20, HeaderComponentLocators.LOCATOR_AUTH_BUTTON)

    def get_menu_button(self):
        print("Получение локатора кнопки Меню")
        return self.get_element(20, HeaderComponentLocators.LOCATOR_MENU_BUTTON)

    def get_cart_button(self):
        print("Получение локатора кнопки Корзины")
        return self.get_element(20, HeaderComponentLocators.LOCATOR_CART_BUTTON)

    def get_puchases_button(self):
        print("Получение локатора кнопки Покупки")
        return self.get_element(20, HeaderComponentLocators.LOCATOR_PURCHASES_BUTTON)

    def get_favorite_button(self):
        print("Получение локатора кнопки Избранное")
        return self.get_element(20, HeaderComponentLocators.LOCATOR_FAVORITE_BUTTON)

    def get_search_field(self):
        print("Получение локатора поля Search")
        return self.get_element(20, HeaderComponentLocators.LOCATOR_SEARCH_FIELD)

    def get_searh_button(self):
        print("Получение локатора кнопки Search")
        return self.get_element(20, HeaderComponentLocators.LOCATOR_SEARSH_BUTTON)

    def get_portal_nav_list(self):
        print("Получение навигационного меню портала")
        elements = self.get_elements(20, HeaderComponentLocators.LOCATOR_NAVBAR_LIST)
        elements_list = []
        for item in elements:
            elements_list.append(item.text)
        print(elements_list)
        return elements_list

    # Действия в компоненте

    def click_login_button(self):
        self.get_login_button().click()
        print("Клик на кнопке Login")

    def click_menu_button(self):
        self.get_menu_button().click()
        print("Клик на кнопке Menu")

    def click_cart_button(self):
        self.get_cart_button().click()
        print("Клик на кнопке Корзины")

    def click_search_button(self):
        self.get_searh_button().submit()
        print("Клик на кнопке Поиск")

    def input_search_text(self, search_text):
        self.get_search_field().send_keys(search_text)
        print("Ввод текста в поле поиска")

    def click_portal_nav_link(self, link_text):
        self.get_element(50, (By.LINK_TEXT, link_text)).click()
        print(f"Клик на разделе меню {link_text}")
