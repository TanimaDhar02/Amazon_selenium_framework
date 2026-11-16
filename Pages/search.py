from selenium.webdriver.common.by import By
from Amazon_POM.Pages.basepage import BasePage

class SearchPage(BasePage):

    search_box = (By.ID, "twotabsearchtextbox")
    search_button = (By.ID, "nav-search-submit-button")

    def enter_product(self, product):
        self.send_keys(self.search_box, product)

    def click_search(self):
        self.click(self.search_button)
