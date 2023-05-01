import time

from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = ' http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.solve_quiz_and_get_code()
    time.sleep(2)
    page.add_product_to_basket()
    page.name_and_price_from_basket()




