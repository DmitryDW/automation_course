from .locators import BasketPageLocators
from .base_page import BasePage
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def go_to_basket_page(self):
        login_link = self.browser.find_element(*BasketPageLocators.ADD_BASKET)
        login_link.click()


    def add_product_to_basket(self):
        product_name = self.browser.find_element(By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > h1")
        name = product_name.text
        basket_name = self.browser.find_element(By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')
        real_name = basket_name.text
        assert name == real_name, 'Название товара не совпадает'


    def name_and_price_from_basket(self):
        book_name = self.browser.find_element(By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')
        name_on_alert = book_name.text
        book_name_added = self.browser.find_element(By.CSS_SELECTOR, '#content_inner > article > div.row > div.col-sm-6.product_main > h1')
        real_name = book_name_added.text
        basket_price = self.browser.find_element(By.CSS_SELECTOR, '#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong')
        real_price_basket = basket_price.text
        book_price = self.browser.find_element(By.CSS_SELECTOR, '#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color')
        real_book_price = book_price.text
        assert name_on_alert == real_name
        assert real_price_basket == real_book_price





