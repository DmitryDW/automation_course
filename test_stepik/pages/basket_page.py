from .base_page import BasePage
from .locators import BasePageLocators


class BasketPage(BasePage):

    def search_empty_basket(self):
        assert self.is_element_present(*BasePageLocators.BASKET_EMPTY), "Login link is not presented"
