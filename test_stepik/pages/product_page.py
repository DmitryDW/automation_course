from .locators import BasketPageLocators
from .base_page import BasePage


class ProductPage(BasePage):
    def go_to_basket_page(self):
        login_link = self.browser.find_element(*BasketPageLocators.ADD_BASKET)
        login_link.click()


    def add_product_to_basket(self):
        product_name = self.browser.find_element(*BasketPageLocators.BOOK_NAME)
        name = product_name.text
        basket_name = self.browser.find_element(*BasketPageLocators.BOOK_NAME_ON_BASKET)
        real_name = basket_name.text
        assert name == real_name


    def name_and_price_from_basket(self):
        book_name = self.browser.find_element(*BasketPageLocators.BOOK_NAME)
        name_on_alert = book_name.text
        book_name_added = self.browser.find_element(*BasketPageLocators.ADDED_BOOK)
        real_name = book_name_added.text
        basket_price = self.browser.find_element(*BasketPageLocators.BASKET_PRICE)
        real_price_basket = basket_price.text
        book_price = self.browser.find_element(*BasketPageLocators.BOOK_ON_BASKET_PRICE)
        real_book_price = book_price.text
        assert name_on_alert == real_name
        assert real_price_basket == real_book_price


    def should_not_be_success_message(self):
        assert self.is_not_element_present(*BasketPageLocators.BOOK_NAME), \
        "   Success message is presented, but should not be"


    def test_guest_cant_see_success_message(self):
        assert self.is_not_element_present(*BasketPageLocators.ADDED_BOOK), \
            "   Success message is presented, but should not be"





