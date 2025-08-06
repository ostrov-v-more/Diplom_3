from selenium.webdriver.common.by import By


class HeaderLocators:
    PROFILE_BUTTON = By.XPATH, "//p[text()='Личный Кабинет']"
    CONSTRUCTOR_BUTTON = By.XPATH, "//p[text()='Конструктор']"
    ORDER_BUTTON = By.XPATH, "//p[text()='Лента Заказов']"
