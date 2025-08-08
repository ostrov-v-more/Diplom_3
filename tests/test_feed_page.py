import allure
from constants.ingredients import Buns, Fillings, Souse
from page_objects.feed_page import FeedPage
from page_objects.header_page import HeaderPage
from page_objects.main_page import MainPage


class TestFeedPage:

    @allure.title("Eсли кликнуть на заказ, откроется всплывающее окно с деталями")
    def test_open_order_details(self, driver):
        HeaderPage(driver).click_order_button()
        feed_page = FeedPage(driver)
        feed_page.click_order()
        assert feed_page.order_feed_modal_is_visible()

    @allure.title("Заказ пользователя отображается в ленте заказов")
    def test_user_order_show_in_feed(self, driver, login_new_user, user_order):
        expected_order_number = "#0" + user_order
        HeaderPage(driver).click_order_button()
        feed_page = FeedPage(driver)
        order_number = feed_page.find_orders_number()
        assert expected_order_number in order_number

    @allure.title("Заказ пользователя отображается в работе")
    def test_user_order_in_work(self, driver, login_new_user, user_order):
        expected_order_number = "0" + user_order
        HeaderPage(driver).click_order_button()
        feed_page = FeedPage(driver)
        order_number = feed_page.check_order_in_work()
        assert expected_order_number == order_number

    @allure.title("Увеличение счетчиков при заказе бургера")
    def test_up_count_order(self, driver, login_new_user):
        header_page = HeaderPage(driver)
        feed_page = FeedPage(driver)
        main_page = MainPage(driver)
        header_page.click_order_button()
        all_orders, day_orders = feed_page.find_order_counts()
        header_page.click_constructor_button()
        main_page.create_burger([Buns.bun_1, Fillings.filling_1, Souse.souse_1])
        header_page.click_order_button()
        new_all_orders, nwe_day_orders = feed_page.find_order_counts()
        assert new_all_orders > all_orders and nwe_day_orders > day_orders



