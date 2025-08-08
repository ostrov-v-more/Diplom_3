from selenium.webdriver.common.by import By


class ProfileLocators:
    LOGOUT_BUTTON = By.XPATH, "//*[text()='Выход']"
    NAME = By.XPATH, "//label[contains(text(), 'Имя')]/following-sibling::input"
    EMAIL = By.XPATH, "//label[contains(text(), 'Логин')]/following-sibling::input"
    ORDER_BUTTON = By.XPATH, "//*[text()='История заказов']"
    ORDER_NUMBER = By.XPATH, "//li[contains(@class, 'OrderHistory_listItem__2x95r')]//p[@class='text text_type_digits-default']"
