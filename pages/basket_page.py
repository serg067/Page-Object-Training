from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def go_to_basket_page(self):
        link = self.browser.find_element(*BasketPageLocators.BASKET)
        link.click()

    def check_basket_is_empty(self):
        empty_message = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE)
        if " Ваша корзина пуста " in empty_message.text:
            return True
        else:
            return False
