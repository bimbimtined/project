import random
import time
import keyboard
from selenium import webdriver
import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains, DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import warnings

#   This class will contain all the methods to execute the homework


class Translink:
    # Home Page
    url = "https://www.translink.ca/"
    nextbusbtn = (By.XPATH, "//button[@id='next-bus']")
    busroutestopnbrsearch = (By.XPATH, "//input[@id='NextBusSearchTerm']")
    findmynextbusbtn = (By.XPATH, "//button[contains(text(),'Find my next bus')]")
    addfavicon = (By.XPATH, "//button[contains(.,'Add Fav')]")
    nametxtbox = (By.XPATH, "//textarea[@name='newFavourite']")
    addtofavoritesbtn = (By.XPATH, "//button[contains(text(),'Add to Favourites')]")
    myfavsicon = (By.XPATH, "//a[contains(.,'My Favs')]")
    translinkautohomeworklink = (By.XPATH, "//a[contains(text(),'Translink Auto Homework')]")
    iframemain = (By.XPATH, "/html[1]/body[1]/main[1]/div[3]/section[3]/iframe[1]")
    iframechild = (By.XPATH, "//iframe[contains(@title,'Next Bus')]")
    commercialbroadwaytxt = (By.XPATH, "//main[@id='content']/div[4]/section[3]/iframe")

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

    def test_nextbus_tab_widget(self):
        # click on next bus tab on widget
        self.driver.find_element(*self.nextbusbtn).click()
        time.sleep(2)

        # on the search field > enter 99
        self.driver.find_element(*self.busroutestopnbrsearch).click()
        self.driver.find_element(*self.busroutestopnbrsearch).send_keys('99')
        time.sleep(2)

        # click Find my next bus button
        self.driver.find_element(*self.findmynextbusbtn).click()
        time.sleep(2)

    def test_add_fav(self):
        # click on Add Fav icon
        self.driver.find_element(*self.addfavicon).click()
        time.sleep(5)

    def test_edit_name(self):
        # clear the name field
        name = self.driver.find_element(*self.nametxtbox)
        name.send_keys(Keys.CONTROL + "a")
        name.send_keys(Keys.DELETE)
        time.sleep(5)

        # enter 'Translink Auto Homework' in the Edit Name
        self.driver.find_element(*self.nametxtbox).send_keys('Translink Auto Homework')

        # click on 'Add to Favourites' button
        self.driver.find_element(*self.addtofavoritesbtn).click()
        time.sleep(2)

        # click on 'My Favs' icon
        self.driver.find_element(*self.myfavsicon).click()
        time.sleep(5)

    def test_check_translink_homework_link(self, Link):
        # validate “Translink Auto Homework” link
        global link
        if Link == 'Translink Auto Homework':
            try:
                link = self.driver.find_element(*self.translinkautohomeworklink)
            except:
                return False

        if Link == link.text:
            return True
        else:
            return False

    def test_click_translink_homework_link(self):
        # click on Translink Auto Homework link
        self.driver.find_element(*self.translinkautohomeworklink).click()
        time.sleep(5)

    def test_switchttoiframe(self):
        link = 'https://www.translink.ca/next-bus/results/#/text/route/99/'
        # frame1 = self.driver.find_element(*self.iframemain)
        # self.driver.switch_to.frame(frame1)
        # time.sleep(5)
        # self.driver.refresh()

        self.driver.switch_to.frame(self.driver.find_element(By.XPATH, "iframe[title='Next Bus']py"))

    def test_check_commercialbroadway(self, CommercialBroadway):
        # validate “99 Commercial-Broadway / UBC (B-Line)” text
        global ubc
        if CommercialBroadway == '99 Commercial-Broadway / UBC (B-Line)':
            try:
                ubc = self.driver.find_element(*self.commercialbroadwaytxt)
            except:
                return False

        if CommercialBroadway == ubc.text:
            return True
        else:
            return False

