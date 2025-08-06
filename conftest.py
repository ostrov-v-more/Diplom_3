import time

import pytest
from selenium import webdriver
from constants.constants import BASE_URL, LOGIN_URL, REGISTER_URL
from constants.ingredients import Buns, Fillings, Souse
import allure

from page_objects.login_page import LoginPage
from page_objects.main_page import MainPage


@pytest.fixture()
def start_page():
    return BASE_URL


@pytest.fixture()
def ingredients_list():
    return [Buns.bun_1, Fillings.filling_1, Souse.souse_1]


@pytest.fixture(params=[
    "Chrome",
    "Firefox"
])
def driver(request, start_page):
    with allure.step(f"Открываем браузер {request.param}"):
        if request.param == "Chrome":
            driver = webdriver.Chrome()
        elif request.param == "Firefox":
            driver = webdriver.Firefox()
        driver.get(start_page)
        driver.maximize_window()
        yield driver
    with allure.step(f"Закрываем браузер {request.param}"):
        driver.quit()


@pytest.fixture()
def login_new_user(driver):
    driver.get(REGISTER_URL)
    login_page = LoginPage(driver)
    user_data = login_page.register_new_user()
    time.sleep(1)  # лаг для бд
    login_page.login_user(user_data["email"], user_data["password"])
    if MainPage(driver).check_visible_button_login(): # не всегда после ввода данных происходит логин
        driver.get(LOGIN_URL)
        login_page.login_user(user_data["email"], user_data["password"])
    return user_data


@pytest.fixture()
def user_order(driver, login_new_user, ingredients_list):
    driver.get(BASE_URL)
    main_page = MainPage(driver)
    order_number = main_page.create_burger(ingredients_list)
    return order_number
