from selenium.webdriver.firefox.options import Options as firfoxOptions
from selenium.webdriver.chrome.options import Options as chromeOptions
from selenium import webdriver
import pytest

BROWSERS = {
    'firefox': webdriver.Firefox,
    # 'chrome': webdriver.Chrome,
}


@pytest.fixture(scope='session', params=BROWSERS.keys())
def browser(request):
    global driver
    if request.param == 'firefox':
        options = firfoxOptions()
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-extensions")
        options.add_argument("--proxy-server='direct://'")
        options.add_argument("--proxy-bypass-list=*")
        options.add_argument("--start-maximized")
        # options.add_argument("--headless")
        driver = BROWSERS[request.param](executable_path="C:/Drivers/Firefox/geckodriver", options=options)
        request.addfinalizer(lambda *args: driver.quit())
        return driver

    # else:
    #     options = chromeOptions()
    #     options.add_argument("--window-size=1920,1080")
    #     options.add_argument("--disable-extensions")
    #     options.add_argument("--proxy-server='direct://'")
    #     options.add_argument("--proxy-bypass-list=*")
    #     options.add_argument("--start-maximized")
    #     # options.add_argument("--headless")
    #     driver = BROWSERS[request.param](executable_path="C:/Drivers/chromedriver_win32_90/chromedriver", options=options)
    #     request.addfinalizer(lambda *args: driver.quit())
    #     return driver