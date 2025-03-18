import time

from selenium.webdriver.common.by import By
from base.base_class import Base


class MainComponentLocators:
    """Класс содержащий локаторы используемые на основном компаненте страницы"""

    LOCATOR_PRODUCTS_LIST = (By.CLASS_NAME, "centered-")
    LOCATOR_PRODUCT_ITEM = (By.CLASS_NAME, "gallery-product-item")
    LOCATOR_MARKET_BUTTON = (By.XPATH, "//button[contains(text(),'Перейти в магазин')]")
    LOCATOR_ADD_TO_CART_BUTTON = (
        By.XPATH,
        "/html/body/div[1]/div[8]/div[2]/div[2]/div/div[2]/div/div/order-cart-control/button",
    )
    LOCATOR_GO_TO_CART_BUTTON = (By.LINK_TEXT, "Корзина")


class MainComponent(Base):
    """Класс основного компанента страницы"""

    # Геттеры

    def get_products_category_list(self):
        print("Получение списка категорий товаров в главной секции страницы")
        elements = self.get_elements(20, MainComponentLocators.LOCATOR_PRODUCTS_LIST)
        return elements

    def get_category(self, category):
        print(f"Выбор категории {category} из списка категорий главной страницы")
        categories = self.get_products_category_list()
        for i, item in enumerate(categories, start=1):
            if category in item.text:
                print(f"Выбрана категория {item.text}")
                return item

    def get_products_list(self):
        print("Получение списка товаров на главной странице")
        products = self.get_elements(20, MainComponentLocators.LOCATOR_PRODUCT_ITEM)
        return products

    def get_product(self, product):
        print(f"Выбор товара {product} из списка товаров главной страницы")
        products = self.get_products_list()
        for i, item in enumerate(products, start=1):
            if product in item.text:
                print(f"Выбрана товар {item.text}")
                return item

    def get_market_button(self):
        print("Получение кнопки перехода в магазин с выбранным товаром")
        return self.get_element(20, MainComponentLocators.LOCATOR_MARKET_BUTTON)

    def get_add_to_cart_button(self):
        print("Получение кнопки добавления товара в корзину")
        return self.get_element(20, MainComponentLocators.LOCATOR_ADD_TO_CART_BUTTON)

    def get_go_to_cart_button(self):
        print("Получение кнопки перехода в корзину")
        return self.get_element(20, MainComponentLocators.LOCATOR_GO_TO_CART_BUTTON)

    # Действия

    def click_category(self, category):
        print("Клик по ссылке категории товара")
        self.get_category(category).click()

    def click_product(self, product):
        print("Клик по ссылке товара")
        self.get_product(product).click()

    def click_market_button(self):
        print("Клик по кнопке перехода в магазин")
        self.get_market_button().click()

    def click_add_to_cart_button(self):
        print("Клик по кнопке добавить товар в корзину")
        self.get_add_to_cart_button().click()

    def click_go_to_cart_button(self):
        print("Клик по кнопке перейти в корзину")
        self.get_go_to_cart_button().click()
