from selenium.webdriver.common.by import By


class MainLocators:
    BASKET = By.XPATH, "//*[contains(@class, 'BurgerConstructor_basket__list__l9dp_')]"
    ORDER_BUTTON = By.XPATH, "//button[text() = 'Оформить заказ']"
    ORDER_NUMBER = (By.XPATH, "//*[contains(@class, 'Modal_modal__title')]")
    CLOSE_POP_UP_BUTTON = By.XPATH, "//*[contains(@class, 'Modal_modal__contentBox')]/following::*[contains(@class, 'Modal_modal__close')][1]"
    POP_UP_WINDOW = By.XPATH, "//div[contains(@class, 'Modal_modal__contentBox__sCy8X')]"
    BURGER_ASSEMBLER = By.XPATH, "//h1[text() = 'Соберите бургер']"
    ORDER_FEED = By.XPATH, "//h1[text() = 'Лента заказов']"
    INGREDIENT_DETAILS = By.XPATH, "//h2[text() = 'Детали ингредиента']"
    BUTTON_LOGIN = By.XPATH, "//button[text() = 'Войти в аккаунт']"


    @staticmethod
    def ingredient(ingredient_id):
        return By.XPATH, f".//*[contains(@href, 'ingredient/{ingredient_id}')]"

    @staticmethod
    def ingredient_counter(ingredient_id):
        return By.XPATH, f".//*[contains(@href, 'ingredient/{ingredient_id}')]//p[contains(@class, 'counter_counter__num__3nue1')]"
