from .pages.product_page import ProductPage
import pytest


@pytest.mark.parametrize('link', [*range(7), pytest.param(7, marks=pytest.mark.xfail(reason="won't fix")), *range(8, 10)])
def test_guest_can_go_to_login_page(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_success_page(page.get_product_name(), page.get_product_price())
