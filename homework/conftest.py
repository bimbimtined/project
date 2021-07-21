from selenium.webdriver.firefox.options import Options as firfoxOptions

from selenium import webdriver
import pytest
import allure
import os

BROWSERS = {
    'firefox': webdriver.Firefox,
}


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' or rep.failed:
        mode = 'a' if os.path.exists('failures') else 'w'
        try:
            with open('failures', mode) as f:
                if 'browser' in item.fixturenames:  # assume this is fixture with webdriver
                    web_driver = item.funcargs['browser']
            allure.attach(
                web_driver.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print('Fail to take screen-shot: {}'.format(e))


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