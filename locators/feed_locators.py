from selenium.webdriver.common.by import By


class FeedLocators:
    ORDER_ITEM = By.XPATH, "//li[contains(@class, 'OrderHistory_listItem__2x95r mb-6')]"
    ORDER_POPUP = By.XPATH, "//p[text()='Cостав']"
    ORDER_NUMBER = By.XPATH, "//p[@class='text text_type_digits-default']"
    ORDER_IN_WORK = By.XPATH, "//ul[@class='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']//li[@class='text text_type_digits-default mb-2']"
    ORDERS_COUNTS = (By.XPATH, "//p[contains(@class, 'OrderFeed_number__2MbrQ')]")
