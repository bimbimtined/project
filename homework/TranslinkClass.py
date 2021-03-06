
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#   This class will contain all the methods to execute the homework


class Translink:
    # Home Page
    url = "https://www.translink.ca/"
    nextbusbtn = (By.XPATH, "//button[@id='next-bus']")
    busroutestopnbrsearch = (By.XPATH, "//input[@id='NextBusSearchTerm']")
    findmynextbusbtn = (By.XPATH, "//button[contains(text(),'Find my next bus')]")
    addfavicon = (By.XPATH, "//button[contains(.,'Add Fav')]")
    nametxtbox = (By.XPATH, "//textarea[@name='newFavourite']")
    addtofavoritesbtn = (By.XPATH, "//button[normalize-space()='Add to favourites']")
    myfavsicon = (By.XPATH, "//a[contains(.,'My Favs')]")
    translinkautohomeworklink = (By.XPATH, "//a[contains(text(),'Translink Auto Homework')]")
    # iframemain = (By.XPATH, "/html[1]/body[1]/main[1]/div[4]/div[1]")
    iframemain = (By.XPATH, "/html[1]/body[1]/main[1]/div[4]/section[3]/iframe[1]")
    commercialbrodwaytxt = (By.XPATH, "//div[@id='MainContent_PanelStops']/div[@class='txtRouteTitle'")

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

    def test_check_translink_homework_link(self, Text1):
        # validate ???Translink Auto Homework??? link
        if Text1 == 'Translink Auto Homework':
            try:
                txt1 = self.driver.find_element(*self.translinkautohomeworklink)
            except:
                return False

        if Text1 == txt1.text:
            return True
        else:
            return False

    def test_click_translink_homework_link(self):
        # click on Translink Auto Homework link
        self.driver.find_element(*self.translinkautohomeworklink).click()
        time.sleep(5)

    def test_switchttoiframe(self):
        frame1 = self.driver.find_element(*self.iframemain)
        self.driver.switch_to.frame(frame1)
        time.sleep(5)

    def test_check_99_commercial_broadway(self, Text2):
        # validate ???99 to Comm???l-Bdway Stn/ Boundary (B-Line)??? is displayed on page
        if Text2 == '99 to Comm???l-Bdway Stn/ Boundary (B-Line)':
            try:
                txt2 = self.driver.find_element(*self.commercialbrodwaytxt)
            except:
                return False

        if Text2 == txt2.text:
            return True
        else:
            return False