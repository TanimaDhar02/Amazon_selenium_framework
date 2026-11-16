from selenium.webdriver.support.ui import Select
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        self.driver.find_element(*locator).click()

    def send_keys(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def select_option(self, locator, text):
        dropdown = self.driver.find_element(*locator)
        option = Select(dropdown)
        option.select_by_visible_text(text)