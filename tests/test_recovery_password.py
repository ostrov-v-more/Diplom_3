import allure
import pytest

from constants.constants import BASE_URL, LOGIN_ENDPOINT
from page_objects.login_page import LoginPage


@pytest.fixture
def start_page():
    return BASE_URL+LOGIN_ENDPOINT


class TestRecoveryPassword:

    @allure.title("Проверяем переход на страницу восстановления пароля")
    def test_recovery_password_flow(self, driver):
        login_page = LoginPage(driver)
        login_page.go_to_recovery_password_page()
        assert login_page.check_visibility_element_recovery_page()

    @allure.title("Проверяем видимость пароля после клика на иконку 'Глазик'")
    def test_click_icon_show_password(self, driver):
        login_page = LoginPage(driver)
        login_page.go_to_recovery_password_page()
        assert login_page.check_see_password()
