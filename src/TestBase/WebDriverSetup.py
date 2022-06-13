from selenium import webdriver


class WebDriverSetup:

    def setup(self):
        self.options = webdriver.ChromeOptions()  # NOQA
        self.options.add_argument('log-level=3')  # 0 - INFO; 1 - WARNINGS; 2 - ERRORS; 3 - FATALS.
        self.driver = webdriver.Chrome(options=self.options)  # NOQA
        self.driver.set_page_load_timeout(30)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.close()
        self.driver.quit()
