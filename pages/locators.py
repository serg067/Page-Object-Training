from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")


class LoginPageLocators:
    LOGIN_URL = (By.CSS_SELECTOR, "#registration_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, "div h1")
    PRODUCT_NAME_IN_SUCCESS_MESSAGES = (By.CSS_SELECTOR, "#messages>div .alertinner strong")
    ADD_PRODUCT_SUCCESS_MASSAGES = (By.CSS_SELECTOR, "#messages>div")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    TOTAL_COST_BASKET_IN_SUCCESS_MESSAGES = (By.CSS_SELECTOR, "#messages div:nth-of-type(3) p strong")

