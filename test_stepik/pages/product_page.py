from .locators import BasketPageLocators
from .base_page import BasePage
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def go_to_basket_page(self):
        login_link = self.browser.find_element(*BasketPageLocators.ADD_BASKET)
        login_link.click()
