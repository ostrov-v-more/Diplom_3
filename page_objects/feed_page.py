import allure


from locators.header_page_locators import HeaderLocators
from locators.login_page_locators import LoginLocators
from locators.feed_locators import FeedLocators
from page_objects.base_page import BasePage


class FeedPage(BasePage):

    @allure.step("Кликаем на первый заказ")
    def click_order(self):
        self.click_element(FeedLocators.ORDER_ITEM)

    @allure.step("проверяем отображение окна")
    def order_feed_modal_is_visible(self):
        return self.find_visible_element(FeedLocators.ORDER_POPUP).is_displayed()

    def find_orders_number(self, ):
        orders_number = self.find_all_elements(FeedLocators.ORDER_NUMBER)
        order_number = [order_number.text for order_number in orders_number]
        return order_number

    def check_order_in_work(self):
        orders_number = self.find_visible_element(FeedLocators.ORDER_IN_WORK)
        return orders_number.text

    def find_order_counts(self):
        counts = self.find_all_elements(FeedLocators.ORDERS_COUNTS)
        all_orders, day_order = [count.text for count in counts]
        return all_orders, day_order
