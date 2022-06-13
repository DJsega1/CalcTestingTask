from selenium.webdriver.common.by import By
from ..locators import CalcPageLocator  # NOQA


class CalcPage:
    def __init__(self, driver):
        self.driver = driver
        self.MEMORY_FIELD = driver.find_element(By.XPATH, CalcPageLocator.MEMORY_FIELD)
        self.RESULT_FIELD = driver.find_element(By.XPATH, CalcPageLocator.RESULT_FIELD)
        self.BUTTON_EQUAL = driver.find_element(By.XPATH, CalcPageLocator.BUTTON_EQUAL)
        self.BUTTONS_NUM = list()
        self.BUTTONS_OPER = list()
        for i in range(1, 4):  # changing XPATH depending on number (check locators)
            self.BUTTONS_NUM.append(driver.find_element(By.XPATH, CalcPageLocator.BUTTON_NUM.format(i)))
        for i in range(2, 6):  # changing XPATH depending on operator (check locators)
            self.BUTTONS_OPER.append(driver.find_element(By.XPATH,
                                                         CalcPageLocator.BUTTON_OPER.format(i)))
