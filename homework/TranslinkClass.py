import random
import time
import allure
import keyboard
from selenium import webdriver
import pytest
from selenium.webdriver import ActionChains, DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

#   This class will contain all the methods to execute the homework


class Translink:
    # Home Page
    url = "https://www.translink.ca/"
    nextbusbtn = (By.XPATH, "//button[@id='next-bus']")

    def __init__(self, driver):
        # to initialize a variable to hold reference of webdriver instance being passed to the function as a reference.
        self.driver = driver

    def load_browser(self):
        # to load a given URL in browser window
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)

    def test_initial_page(self):
        # test whether correct URL has been loaded or not
        current = self.driver.current_url
        try:
            if current == self.url:
                return True
            else:
                return False
        except:
            return False