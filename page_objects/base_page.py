import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.common import TimeoutException
from locators.login_page_locators import LoginLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.time = 15
        self.wait = WebDriverWait(self.driver, self.time)

    @allure.step("Находим видимый элемент")
    def find_visible_element(self, locator):
        element = self.wait.until(expected_conditions.visibility_of_element_located(locator))
        return element

    @allure.step("Находим элемент")
    def find_invisibility_element(self, locator):
        element = self.wait.until(expected_conditions.invisibility_of_element_located(locator))
        return element

    @allure.title("Получаем значение поля")
    def get_element_value(self, locator):
        element_value = self.find_visible_element(locator)
        return element_value.get_attribute("value")

    @allure.step("Находим все элементы")
    def find_all_elements(self, locator):
        elements = self.wait.until(expected_conditions.presence_of_all_elements_located(locator))
        return elements

    @allure.step("Скроллим до нужного элемента")
    def scroll_to_element(self, element):
        self.driver.execute_script("window.scrollTo(0, arguments[0].offsetTop);", element)

    @allure.step("Кликаем на элемент")
    def click_element(self, locator):
        element = self.find_visible_element(locator)
        self.scroll_to_element(element)
        try:
            element.click()
        except:
            print("!!!except_click_element")
            self.driver.execute_script("arguments[0].dispatchEvent(new MouseEvent('click', { bubbles: true }));", element)

    @allure.step("Кликаем на кликабельный элемент")
    def click_button(self, locator):
        element = self.wait.until(expected_conditions.element_to_be_clickable(locator))
        try:
            self.scroll_to_element(element)
            element.click()
        except:
            self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Пробуем еще кликнуть")
    def other_click_button(self, locator):
        self.wait_for_invisibility(LoginLocators.OVERLAY)
        element = self.wait.until(expected_conditions.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].dispatchEvent(new MouseEvent('click', { bubbles: true }));", element)

    @allure.step("Заполняем инпут")
    def add_text_to_element(self, locator, text):
        element = self.find_visible_element(locator)
        element.send_keys(text)

    @allure.step("Перетаскиваем элемент")
    def drag_and_drop(self, locator_from, locator_to):
        from_element = self.find_visible_element(locator_from)
        self.scroll_to_element(locator_from)
        to_element = self.find_visible_element(locator_to)
        self.scroll_to_element(locator_from)
        if self.driver.name == "chrome":
            action = ActionChains(self.driver)
            action.drag_and_drop(from_element, to_element).perform()
        if self.driver.name == 'firefox':
            self.driver.execute_script(
                """
                var source = arguments[0];
                var target = arguments[1];
                var evt = document.createEvent("DragEvent");
                evt.initMouseEvent("dragstart", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                source.dispatchEvent(evt);
                evt = document.createEvent("DragEvent");
                evt.initMouseEvent("dragenter", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                target.dispatchEvent(evt);
                evt = document.createEvent("DragEvent");
                evt.initMouseEvent("dragover", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                target.dispatchEvent(evt);
                evt = document.createEvent("DragEvent");
                evt.initMouseEvent("drop", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                target.dispatchEvent(evt);
                evt = document.createEvent("DragEvent");
                evt.initMouseEvent("dragend", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                source.dispatchEvent(evt);
                """,
                from_element,
                to_element
            )

    @allure.step("Ждем исчезновения элемента")
    def wait_for_invisibility(self, locator):
        try:
            self.wait.until_not(expected_conditions.invisibility_of_element_located(locator))
        except TimeoutException:
            pass

    def current_url(self):
        return self.driver.current_url

    def wait_until_text_is_visible(self, locator, element_text):
        try:
            self.wait.until_not(expected_conditions.text_to_be_present_in_element(locator, element_text))
        except TimeoutException:
            pass

