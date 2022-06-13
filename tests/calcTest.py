import sys

sys.path.append(sys.path[0] + "/..")  # changing path in order to avoid ImportError

from src.TestBase.WebDriverSetup import WebDriverSetup  # NOQA
from src.PageObject.Pages.CalcPage import CalcPage  # NOQA
from src.PageObject.Pages.HomePage import HomePage  # NOQA


class TestCalcPage(WebDriverSetup):
    def test_main(self):
        self.driver.get("https://google.com")

        assert self.driver.title == "Google"

        home_page = HomePage(self.driver)
        home_page.SEARCH_BAR.send_keys("Калькулятор")
        home_page.BUTTON_SUBMIT.click()

        assert self.driver.title == "Калькулятор - Поиск в Google"

        calc_page = CalcPage(self.driver)

        queue = [calc_page.BUTTONS_NUM[0],  # buttons queue
                 calc_page.BUTTONS_OPER[1],
                 calc_page.BUTTONS_NUM[1],
                 calc_page.BUTTONS_OPER[2],
                 calc_page.BUTTONS_NUM[2],
                 calc_page.BUTTONS_OPER[3],
                 calc_page.BUTTONS_NUM[0],
                 calc_page.BUTTON_EQUAL]

        for button in queue:
            button.click()

        memory = calc_page.MEMORY_FIELD.text
        result = calc_page.RESULT_FIELD.text

        assert memory == "1 × 2 - 3 + 1 ="
        assert result == '0'
