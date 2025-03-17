import time

from selenium.webdriver.common.by import By
from base.base_class import Base


class MainComponentLocators:
    """Класс содержащий локаторы используемые на основном компаненте страницы"""

    LOCATOR_PRODUCTS_LIST = (By.CLASS_NAME, "centered-")
    LOCATOR_PRODUCT_ITEM = (By.CLASS_NAME, "")


class MainComponent(Base):
    """Класс основного компанента страницы"""

    def get_products_category_list(self):
        print("Получение навигационного меню портала")
        elements = self.get_elements(20, MainComponentLocators.LOCATOR_PRODUCTS_LIST)
        return elements

    def get_category(self, category):
        categories = self.get_products_category_list()
        for i, item in enumerate(categories, start=1):
            if category in item.text:
                print(f"Выбрана категория {item.text}")
                return item

    def click_category(self, category):
        print("Клик по ссылке категории товара")
        self.get_category(category).click()
