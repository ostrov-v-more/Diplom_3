import allure

from constants import constants
from page_objects.header_page import HeaderPage
from page_objects.profile_page import ProfilePage




class TestProfilePage:

    @allure.title("Переход в раздел 'История заказов'")
    def test_go_user_orders(self, driver, login_new_user, user_order):
        expected_order_number = "#0" + user_order
        HeaderPage(driver).click_profile_button(driver.name)
        profile_page = ProfilePage(driver)
        profile_page.click_user_order_button()
        order_number = profile_page.get_order_number()
        assert expected_order_number == order_number

    @allure.title("Выход из аккаунта")
    def test_logout_user(self, driver, login_new_user):
        HeaderPage(driver).click_profile_button(driver.name)
        profile_page = ProfilePage(driver)
        profile_page.click_exit()
        assert profile_page.current_url() == constants.LOGIN_URL
