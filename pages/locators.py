from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")


class LoginPageLocators:
    LOGIN_URL = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL = (By.CSS_SELECTOR, "[name=registration-email]")
    PASSWORD1 = (By.CSS_SELECTOR, "[name=registration-password1]")
    PASSWORD2 = (By.CSS_SELECTOR, "[name=registration-password2]")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "[name = registration_submit]")
    SUCCESSFUL_REGISTRATION = (By.CSS_SELECTOR, ".alert-success")


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, "div h1")
    PRODUCT_NAME_IN_SUCCESS_MESSAGES = (By.CSS_SELECTOR, "#messages>div .alertinner strong")
    ADD_PRODUCT_SUCCESS_MASSAGES = (By.CSS_SELECTOR, "#messages>div")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    TOTAL_COST_BASKET_IN_SUCCESS_MESSAGES = (By.CSS_SELECTOR, "#messages div:nth-of-type(3) p strong")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET = (By.CSS_SELECTOR, 'span a.btn-default')
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, 'div>div>p:only-child')
    SUCCSS_MESSAGE = (By.CSS_SELECTOR, '#messages .alertinner')
