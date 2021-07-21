import allure
from homework.TranslinkClass import Translink

@allure.suite('Login')
@allure.title('Launch the browser and check if browser navigates to the landing page')
def test_openNewBrowser(browser):
    global translink
    translink = Translink(browser)
    translink.load_browser()
    assert translink.test_initial_page() == True, "Page is wrong"