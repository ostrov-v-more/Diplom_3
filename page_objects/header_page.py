import allure
from locators.header_page_locators import HeaderLocators
from page_objects.base_page import BasePage


class HeaderPage(BasePage):

    @allure.step("Нажимаем кнопку 'Лена Заказов'")
    def click_order_button(self):
        self.click_button(HeaderLocators.ORDER_BUTTON)

    @allure.step("Нажимаем кнопку 'Личный кабинет'")
    def click_profile_button(self, driver_name):
        self.click_button(HeaderLocators.PROFILE_BUTTON)

        if driver_name == "chrome":
            self.click_button(HeaderLocators.PROFILE_BUTTON)
        if driver_name == "firefox":
            self.other_click_button(HeaderLocators.PROFILE_BUTTON)


    @allure.step("Нажимаем кнопку 'Конструктор'")
    def click_constructor_button(self):
        self.click_button(HeaderLocators.CONSTRUCTOR_BUTTON)

