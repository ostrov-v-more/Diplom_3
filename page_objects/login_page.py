import allure
from page_objects.base_page import BasePage
from locators.login_page_locators import LoginLocators
from helpers.data_helper import DataHelper


class LoginPage(BasePage):

    @allure.step("Кликаем 'Зарегистрироваться'")
    def click_register(self):
        self.click_button(LoginLocators.REGISTER)

    @allure.step("Кликаем 'Восстановить пароль'")
    def click_recover_password(self):
        self.click_button(LoginLocators.FORGOT_PASSWORD)

    @allure.step("Вводим email")
    def set_email(self, email: str = None):
        email = email or DataHelper.generate_email()
        self.add_text_to_element(LoginLocators.EMAIL, email)
        return email

    @allure.step("Вводим имя")
    def set_name(self, name: str = None):
        name = name or DataHelper.generate_name()
        self.add_text_to_element(LoginLocators.NAME, name)
        return name

    @allure.step("Вводим пароль")
    def set_password(self, password: str = None):
        password = password or DataHelper.generate_password()
        self.add_text_to_element(LoginLocators.PASSWORD, password)
        return password

    @allure.step("Кликаем кнопку 'Восстановить'")
    def click_button_recover(self):
        self.click_button(LoginLocators.RECOVER_BUTTON)

    @allure.step("Кликаем кнопку 'Войти'")
    def click_button_enter(self):
        print("Кликаем кнопку 'Войти'")
        self.click_button(LoginLocators.LOGIN_BUTTON)

    def check_button_enter(self):
        return self.find_visible_element(LoginLocators.LOGIN_BUTTON).is_displayed()


    @allure.step("переходим на страницу 'Восстановление пароля'")
    def go_to_recovery_password_page(self):
        self.click_recover_password()
        self.set_email()
        self.click_button_recover()

    @allure.step("Проверяем видимость элементов на странице 'Восстановление пароля'")
    def check_visibility_element_recovery_page(self):
        text = self.find_visible_element(LoginLocators.TEXT_PASS_RECOVERY_H2).is_displayed()
        new_pass = self.find_visible_element(LoginLocators.NEW_PASSWORD).is_displayed()
        email_code = self.find_visible_element(LoginLocators.EMAIL_CODE).is_displayed()
        return all([text, new_pass, email_code])

    @allure.step("Вводим новый пароль")
    def set_new_password(self):
        password = DataHelper.generate_password()
        self.add_text_to_element(LoginLocators.NEW_PASSWORD, password)
        return password

    @allure.step("Кликаем иконку 'Показать пароль' и проверяем что пароль стал видимым")
    def check_see_password(self):
        self.set_new_password()
        self.click_element(LoginLocators.SEE_PASSWORD_ICON)
        element = self.find_visible_element(LoginLocators.TEXT_PASSWORD)
        return element.is_displayed()

    @allure.step("Регистрируем нового пользователя")
    def register_new_user(self, name: str = None, email: str = None, password: str = None):
        name = self.set_name(name)
        email = self.set_email(email)
        password = self.set_password(password)
        self.click_register()
        return {
            "name": name,
            "email": email,
            "password": password,
        }

    @allure.step("Логинимся пользователем")
    def login_user(self, email, password):
        self.set_email(email)
        self.set_password(password)
        self.click_button_enter()






