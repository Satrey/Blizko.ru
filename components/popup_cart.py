import time

from selenium.webdriver.common.by import By
from base.base_class import Base


class CartPopupComponentLocators:
    """Класс содержащий локаторы используемые на основном компаненте страницы"""

    LOCATOR_POPUP_CART_CONFIRM_BUTTON = (
        By.XPATH,
        '//a[contains(text(), "Перейти к оформлению")]',
    )  # (By.LINK_TEXT, "Перейти к оформлению")
    LOCATOR_POPUP_CART_BACK_BUTTON = (
        By.XPATH,
        "//span[contains(text(), 'Вернуться к покупкам')]",
    )


class CartPopupComponent(Base):
    """Класс всплывающего окна корзины"""

    # Геттеры

    def get_popup_cart_confirm_button(self):
        print("Получение кнопки подтверждения заказа")
        return self.get_element(
            30, CartPopupComponentLocators.LOCATOR_POPUP_CART_CONFIRM_BUTTON
        )

    def get_popup_cart_back_button(self):
        print("Получение кнопки возврата в магазин")
        return self.get_element(
            30, CartPopupComponentLocators.LOCATOR_POPUP_CART_BACK_BUTTON
        )

    # Действия

    def click_popup_cart_confirm_button(self):
        self.get_popup_cart_confirm_button().click()
        print("Клик по кнопке подтверждения заказа")

    def click_popup_cart_back_button(self):
        self.get_popup_cart_back_button().click()
        print("Клик по кнопке возвратав магазин")
