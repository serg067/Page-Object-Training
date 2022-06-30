from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.locators import BasketPageLocators
from .pages.locators import ProductPageLocators
import time

import pytest

link1 = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
link2 = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link1)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.need_review
@pytest.mark.parametrize('link',
                         [*range(7), pytest.param(7, marks=pytest.mark.xfail(reason="сломан, согласно заданию")), *range(8, 10)])
def test_guest_can_add_product_to_basket(browser, link):
    link = f"{link1}?promo=offer{link}"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_success_page(page.get_product_name(), page.get_product_price())


@pytest.mark.xfail(reason="специально добавлена сломанная проверка")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link1)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


@pytest.mark.xfail(reason="специально добавлена сломанная проверка")
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link1)
    page.open()
    page.add_to_basket()
    page.should_success_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link2)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link2)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link2)
    page.open()
    page = BasketPage(browser, link2)
    page.go_to_basket_page()
    page.is_not_element_present(*ProductPageLocators.PRODUCT_NAME_IN_BASKET)
    page.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE)
    page.check_basket_is_empty()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        page = LoginPage(browser)
        page.open()
        email = str(time.time()) + "@mail.ru"
        password = 'passwordpass'
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link1)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link1)
        page.open()
        page.add_to_basket()
        page.should_be_success_page(page.get_product_name(), page.get_product_price())
