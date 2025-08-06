import allure
from page_objects.base_page import BasePage
from locators.main_page_locators import MainLocators


class MainPage(BasePage):

    def click_button_order(self):
        self.click_button(MainLocators.ORDER_BUTTON)

    def close_pop_up_order(self):
        if self.find_visible_element(MainLocators.POP_UP_WINDOW):
            self.click_button(MainLocators.CLOSE_POP_UP_BUTTON)

    @allure.step("Выбираем ингредиент")
    def click_ingredient(self, ingredient):
        ingredient_locator = MainLocators.ingredient(ingredient)
        self.click_element(ingredient_locator)

    @allure.step("Проверяем отображение деталей")
    def check_visible_ingredient_details(self):
        return self.find_visible_element(MainLocators.INGREDIENT_DETAILS)


    @allure.step("Проверяем отображение деталей")
    def check_invisible_ingredient_details(self):
        return self.find_invisibility_element(MainLocators.INGREDIENT_DETAILS)

    @allure.step('Получаем значение счетчика ингредиентов')
    def get_counter_ingredients(self, ingredient):
        counter_locator = MainLocators.ingredient_counter(ingredient)
        element = self.find_visible_element(counter_locator)
        return element.text

    @allure.step('Перетаскиваем ингредиент в корзину')
    def drag_and_drop_ingredient_in_basket(self, ingredient: str):
        with allure.step(f"Добавляем ингредиент с id: {ingredient}"):
            ingredient_locator = MainLocators.ingredient(ingredient)
            self.drag_and_drop(locator_from=ingredient_locator, locator_to=MainLocators.BASKET)

    def get_order_number(self):
        order_number = "9999"
        self.wait_until_text_is_visible(MainLocators.ORDER_NUMBER, order_number)
        while order_number == "9999":
            order_number = self.find_visible_element(MainLocators.ORDER_NUMBER).text
        return order_number

    @allure.step("Заказываем бургер")
    def create_burger(self, ingredients_list):
        for ingredient in ingredients_list:
            self.drag_and_drop_ingredient_in_basket(ingredient)
        self.click_button_order()
        order_number = self.get_order_number()
        self.close_pop_up_order()
        return order_number

    @allure.step("Проверяем видимость заголовка страницы Конструктор")
    def check_visible_constructor_text(self):
        element = self.find_visible_element(MainLocators.BURGER_ASSEMBLER)
        return element.is_displayed()

    @allure.step("Проверяем видимость заголовка страницы Лента Заказов")
    def check_visible_feed_text(self):
        element = self.find_visible_element(MainLocators.ORDER_FEED)
        return element.is_displayed()

    def check_visible_button_login(self):
        try:
            element = self.find_visible_element(MainLocators.BUTTON_LOGIN)
            return element.is_displayed()
        except:
            return False
