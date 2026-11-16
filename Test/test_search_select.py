from time import sleep
from Amazon_POM.Pages.search import SearchPage
from Amazon_POM.Pages.select import SelectPage

def test_search_select(setup_and_teardown):
    driver = setup_and_teardown

    driver.get("https://www.amazon.in/")
    sleep(3)

    search_page = SearchPage(driver)

    search_page.enter_product("Mobile")
    search_page.click_search()

    sleep(3)

    print("Current URL:", driver.current_url)
    print("Page Title:", driver.title)

    select_page = SelectPage(driver)

    select_page.choose_sort_option()

    sleep(3)