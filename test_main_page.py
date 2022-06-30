from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.locators import BasketPageLocators
from .pages.locators import ProductPageLocators


link = "http://selenium1py.pythonanywhere.com/"


class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


def test_login_page(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, link)
    page.open()
    page = BasketPage(browser, link)
    page.go_to_basket_page()
    page.is_not_element_present(*ProductPageLocators.PRODUCT_NAME_IN_BASKET)
    page.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE)
    page.check_basket_is_empty()
