from homework.TranslinkClass import Translink


def test_openNewBrowser(browser):
    global translink
    translink = Translink(browser)
    translink.load_browser()
    assert translink.test_initial_page() == True, "Page is wrong"


def test_findMyNextBus(browser):
    translink.test_nextbus_tab_widget()
    translink.test_add_fav()
    translink.test_edit_name()


def test_translinkAutoHomework(browser):
    assert translink.test_check_translink_homework_link('Translink Auto Homework') == True, "Translink Auto Homework - link not found"
    translink.test_click_translink_homework_link()
    translink.test_switchttoiframe()
