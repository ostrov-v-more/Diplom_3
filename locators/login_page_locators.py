from selenium.webdriver.common.by import By


class LoginLocators:
    EMAIL = By.XPATH, "//label[contains(text(), 'Email')]/following-sibling::input"
    NAME = By.XPATH, "//label[contains(text(), 'Имя')]/following-sibling::input"
    PASSWORD = By.XPATH, "//input[@type='password' and @name='Пароль']"
    LOGIN_BUTTON = By.XPATH, "//button[text()='Войти']"
    FORGOT_PASSWORD = By.XPATH, "//*[text()='Восстановить пароль']"
    RECOVER_BUTTON = By.XPATH, "//*[text()='Восстановить']"
    REGISTER = By.XPATH, "//*[text()='Зарегистрироваться']"
    TEXT_PASS_RECOVERY_H2 = By.XPATH, "//div//h2[text()='Восстановление пароля']"
    EMAIL_CODE = By.XPATH, "//*[contains(@class, 'input') and text()='Введите код из письма']"
    NEW_PASSWORD = By.XPATH, "//input[@type='password' and @name='Введите новый пароль']"
    SEE_PASSWORD_ICON = By.XPATH, "//div[@class='input__icon input__icon-action']"
    TEXT_PASSWORD = By.XPATH, "//input[@type='text' and (@name='Введите новый пароль' or @name='Пароль')]"
    OVERLAY = By.XPATH, "//*[contains(@class, 'Modal_modal_overlay__')]"