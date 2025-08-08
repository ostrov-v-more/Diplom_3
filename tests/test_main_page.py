import pytest
import allure
from constants.ingredients import Buns, Fillings, Souse
from page_objects.main_page import MainPage


class TestMainPage:

    @allure.title("Проверяем появление поп-ап окна")
    @pytest.mark.parametrize("ingredient", [Buns.bun_2, Fillings.filling_1, Souse.souse_1])
    def test_show_ingredient_details(self, driver, ingredient):
        main_page = MainPage(driver)
        main_page.click_ingredient(ingredient)
        assert main_page.check_visible_ingredient_details()

    @allure.title("Поп-ап окно закрывается при нажатии на крестик")
    def test_close_ingredient_details(self, driver):
        main_page = MainPage(driver)
        main_page.click_ingredient(Buns.bun_2)
        main_page.close_pop_up_order()
        assert main_page.check_invisible_ingredient_details()

    @allure.title("При добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента")
    def test_up_ingredient_counter(self, driver):
        ingredient = Fillings.filling_1
        main_page = MainPage(driver)
        counter_0 = main_page.get_counter_ingredients(ingredient)
        main_page.drag_and_drop_ingredient_in_basket(ingredient)
        counter_1 = main_page.get_counter_ingredients(ingredient)
        assert int(counter_0) + 1 == int(counter_1)

    @allure.title("Проверка возможности создать заказ залогининым пользователем")
    def test_create_order(self, driver, login_new_user):
        main_page = MainPage(driver)
        order_number = main_page.create_burger([Buns.bun_1, Fillings.filling_1, Souse.souse_1])
        assert order_number != "9999" and len(order_number) != 0

