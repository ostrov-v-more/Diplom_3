import time

import allure

from locators.login_page_locators import LoginLocators
from page_objects.base_page import BasePage
from locators.profile_page_locators import ProfileLocators



class ProfilePage(BasePage):

    def get_name(self):
        return self.get_element_value(ProfileLocators.NAME)

    def get_login(self):
        return self.get_element_value(ProfileLocators.EMAIL)

    def click_user_order_button(self):
        self.click_button(ProfileLocators.ORDER_BUTTON)

    def click_exit(self):
        self.click_button(ProfileLocators.LOGOUT_BUTTON)
        self.find_visible_element(LoginLocators.LOGIN_BUTTON)

    def get_order_number(self):
        element = self.find_visible_element(ProfileLocators.ORDER_NUMBER)
        return element.text

    @allure.step("Проверяем данные в профиле")
    def assert_profile_info(self, name, email):
        return all([self.get_name() == name, self.get_login() == email])
