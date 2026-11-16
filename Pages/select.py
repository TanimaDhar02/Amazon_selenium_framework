from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Amazon_POM.Pages.basepage import BasePage

class SelectPage(BasePage):

    sort_dropdown = (By.XPATH, "//span[@class='a-button-text a-declarative']")
    sort_option = (By.XPATH, "//a[contains(text(),'Price: Low to High')]")

    def choose_sort_option(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(
            EC.element_to_be_clickable(self.sort_dropdown)
        ).click()

        wait.until(
            EC.element_to_be_clickable(self.sort_option)
        ).click()