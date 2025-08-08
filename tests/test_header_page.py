
import allure
import pytest

from constants.constants import BASE_URL, LOGIN_ENDPOINT
from page_objects.header_page import HeaderPage
from page_objects.main_page import MainPage
from page_objects.profile_page import ProfilePage


class TestHeaderPage:

    @allure.title("Переход по клику в Личный кабинет")
    def test_go_profile_page(self, driver, login_new_user):
        email = login_new_user["email"]
        name = login_new_user["name"]
        HeaderPage(driver).click_profile_button(driver.name)
        assert ProfilePage(driver).assert_profile_info(name, email)

    @allure.title("Переход по клику в Ленту заказа")
    def test_go_order_feed(self, driver):
        HeaderPage(driver).click_order_button()
        assert MainPage(driver).check_visible_feed_text()

    @allure.title("Переход по клику в Конструктор")
    @pytest.mark.parametrize("start_page", [BASE_URL + LOGIN_ENDPOINT])
    def test_go_constructor(self, driver):
        HeaderPage(driver).click_constructor_button()
        assert MainPage(driver).check_visible_constructor_text()

