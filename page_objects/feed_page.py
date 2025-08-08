import allure

from locators.feed_locators import FeedLocators
from page_objects.base_page import BasePage


class FeedPage(BasePage):

    @allure.step("Кликаем на первый заказ")
    def click_order(self):
        self.click_element(FeedLocators.ORDER_ITEM)

    @allure.step("Проверяем отображение окна")
    def order_feed_modal_is_visible(self):
        return self.find_visible_element(FeedLocators.ORDER_POPUP).is_displayed()

    @allure.step("Сохраняем номер заказа")
    def find_orders_number(self, ):
        orders_number = self.find_all_elements(FeedLocators.ORDER_NUMBER)
        order_number = [order_number.text for order_number in orders_number]
        return order_number

    @allure.step("Находим номер заказа 'в работе'")
    def check_order_in_work(self):
        orders_number = self.find_visible_element(FeedLocators.ORDER_IN_WORK)
        return orders_number.text

    @allure.step("Находим счетчики заказов")
    def find_order_counts(self):
        counts = self.find_all_elements(FeedLocators.ORDERS_COUNTS)
        all_orders, day_order = [count.text for count in counts]
        return all_orders, day_order
