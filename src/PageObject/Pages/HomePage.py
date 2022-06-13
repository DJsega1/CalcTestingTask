from selenium.webdriver.common.by import By
from ..locators import HomePageLocator  # NOQA


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.SEARCH_BAR = driver.find_element(By.XPATH, HomePageLocator.SEARCH_BAR)
        self.BUTTON_SUBMIT = driver.find_element(By.XPATH, HomePageLocator.BUTTON_SUBMIT)
