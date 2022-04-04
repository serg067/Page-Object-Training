from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button.click()

    def get_product_name(self):
        product_name_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET)
        return product_name_in_basket.text

    def get_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        return product_price.text

    def should_be_success_page(self, product_name, product_price):
        self.should_be_success_message(product_name)
        self.should_be_cost_basket(product_price)

    def should_be_success_message(self, product_name):
        access_message = self.browser.find_element(*ProductPageLocators.ADD_PRODUCT_SUCCESS_MASSAGES)
        product_name_in_success_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_SUCCESS_MESSAGES)
        assert 'был добавлен в вашу корзину' in access_message.text and product_name == product_name_in_success_message.text,\
            f"Название товара из корзины не соответствуют названию товара в сообщении.\
            product_name_in_success_message: {product_name_in_success_message.text}\n\
            product_name_in_basket: {product_name}"

    def should_be_cost_basket(self, product_price):
        basket_total_cost = self.browser.find_element(*ProductPageLocators.TOTAL_COST_BASKET_IN_SUCCESS_MESSAGES)
        assert product_price == basket_total_cost.text,\
            f"Сумма добавленных товаров не равна итоговой сумме покупки. product_price: {product_price},\
            basket_total_cost: {basket_total_cost.text}"