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



class VopayPages:
    outerUrl = "https://vopay-testing.com/iframe/new/outer.html"
    iframelink = (By.XPATH, "//body/center[1]/iframe[1]")
    iframelinkinner = (By.XPATH, "/html[1]/body[1]/center[1]/iframe[1]")
    loadmore = (By.XPATH, "//button[@id='load-more']")
    banklist = (By.XPATH, "//div[@class='bankList__Item ']")

    # Home Page
    linkYourBankTxt = (By.XPATH,"//div[@class='bankListCenterItems bankListCenterItemsNOt']//div[@class='bankHeader__container']//h1[@class='bankList__Header'][contains(text(),'Link your bank')]")
    searchBankPlaceHolder = (By.XPATH, "//input[@id='search-bar']")

    # Search Bank
    vopayBank = (By.XPATH, "//div[@class='bankList__Items ']//div[@id='1884']")
    continueBtn = (By.XPATH, "//button[@id='procced-bank']")

    # Connect your account
    securelyConnectTxt = (By.XPATH,"//div[contains(@class,'bankListCenterItems')]//h1[@class='bankFlow__title bankflow__sepearator'][contains(text(),'Securely connect your account')]")
    changeBank = (By.XPATH, "//a[@id='change-bank']")
    myBankOnline = (By.XPATH, "//span[contains(text(),'Connect my bank online')]")
    myBankManually = (By.XPATH, "//span[contains(text(),'Connect my bank manually')]")

    # My Bank Online
    userNameTxtBox = (By.XPATH, "//input[@id='username']")
    passwordTxtBox = (By.XPATH, "//input[@id='password']")
    termsOfUseTxt = (By.XPATH, "//div[@id='bankFlow']//label[2]")
    termsOfUseLink = (By.XPATH, "//a[@id='TermsofUseButtonLogin']")
    termsOfUseCrossBtn = (By.XPATH, "//span[@class='icon-cross cross']")
    termsOfUseChecked = (By.XPATH, "//div[@id='ember453']//p[@class='tersofuse__condition']")
    continueButton = (By.XPATH, "//button[@id='AutoLogin']")
    bankFlowSubtitleUserPassIncorrect = (By.XPATH, "//p[contains(text(),'Your username or password are incorrect. Please tr')]")
    bankFlowSubtitleSecReasons = (By.XPATH, "//p[contains(text(),'For security reasons your account may be locked af')]")
    retryLogin = (By.XPATH, "//button[@id='AutoRetryLogin']")

    # My Bank Online - Verify Identity
    bankFlowSubtitleSeparatorTxt = (By.XPATH, "//h1[contains(text(),'What is the color of sky? Answer: blue')]")
    bankFlowSubtitleIdentityTxt = (By.XPATH, "//h2[contains(text(),'Verify your identity')]")
    continueBankBtn = (By.CSS_SELECTOR, "div[id='ember516'] button[class='bank__Button ']")
    answerTxtBox = (By.XPATH, "//input[@id='anwser-question']")
    bankFlowSubtitleProvideAnswerTxt = (By.XPATH, "//p[contains(text(),'Please provide the answer along with the user toke')]")
    retryQuestion = (By.XPATH, "//button[@id='AutoRetryQuestion']")
    bankFlowSubtitleStillThereTxt = (By.XPATH, "//h1[@class='bankFlow__subTitle bankflow__sepearator'][normalize-space()='Are you still there?']")
    sessionExpireBtn = (By.XPATH, "//button[@id='SessionExpireContinue2']")

    # My Bank Online - Select an Account
    selectAccountTxt = (By.XPATH, "//h1[contains(text(),'Please select an account')]")
    chequingCADMasked = (By.XPATH, "//span[contains(.,'Chequing (***9999)')]")
    chequingCADBal = (By.XPATH, "//span[contains(.,'$50,000.00 CAD')]")
    chequingUSDMasked = (By.XPATH, "//span[contains(.,'Chequing (***9988)')]")
    chequingUSDBal = (By.XPATH, "//span[contains(.,'$5,000.00 USD')]")
    chequingCADBtn = (By.XPATH, "//label[@for='bankId-0']//span[@class='circle']")
    chequingUSDBtn = (By.XPATH, "//label[@for='bankId-1']//span[@class='circle']")
    submitAccountBtn = (By.XPATH, "//button[@id='AutoSubmitAccount']")
    tokenprint = (By.XPATH, "//div[@class='token-container']/div[1]/div[1]")

    # Manual Banking
    vopayLogo = (By.XPATH, "//form[@id='manualBaninkInfo']//img")
    institutionNbrTxt = (By.CSS_SELECTOR, "p[class='bankflow__description bankflow__description--InstitutionNumber']")
    transitNbrTxtBox = (By.ID, "transit-number")
    accountNbrTxtBox = (By.ID, "account-number")
    accountNbrErrorMsg = (By.XPATH, "//li[contains(text(),'This value is too short. It should have 7 characters or more.')]")
    accountNbrValueReqErrorMsg = (By.XPATH, "//li[contains(text(),'This value is required.')]")
    manualTermsOfUseTxt = (By.ID, "TermsofUseButtonManualLogin")
    manualContinueBtn = (By.ID, 'ManualAccountInfoSubmit')

    # Manual Banking - Account Type
    accountTypeTxt = (By.XPATH, "//h1[contains(text(),'Select your Account Type')]")
    personalAccountBtn = (By.XPATH, "//span[contains(text(),'Personal Account')]")
    businessAccountBtn = (By.XPATH, "//span[contains(text(),'Business Account')]")
    accountTypeBtn = (By.ID, "SelectAccountType")
    invalidEmailErrorMsg = (By.XPATH, "//li[contains(text(),'This value should be a valid email.')]")
    manualPersonalBtn = (By.ID, "ManualPersonalComplete")

    # Manual Banking - Account Type - Personal Account
    firstNameTxtBox = (By.ID, "first-name-personal")
    lastNameTxtBox = (By.ID, "last-name-personal")
    emailTxtBox = (By.ID, "email-personal")
    phoneTxtBox = (By.ID, "phone-personal")
    addMyAddressTxt = (By.ID, "ManualPersonalAddAddress")
    addressDdl = (By.XPATH, "//input[@id='address']")
    cityTxtBox = (By.ID, "city")
    provinceTxtBox = (By.ID, "ProvinceText")
    postalCodeTxtBox = (By.ID, "postalcode")
    cancelRemoveBtn = (By.ID, "ManualRemoveAddress")
    addAddressBtn = (By.ID, "manualAddAddress")

    # Manual Banking - Account Type - Business Account
    companyNameTxtBox = (By.XPATH, "//input[@id='company-name-business']")
    firstNameBusinessTxtBox = (By.XPATH, "//input[@id='first-name-business']")
    lastNameBusinessTxtBox = (By.XPATH, "//input[@id='last-name-business']")
    phoneBusinessTxtBox = (By.XPATH, "//input[@id='phone-business']")
    addMyAddressBusinessTxt = (By.XPATH, "//a[@id='ManualBusinessAddAddress']")
    cancelRemoveBusinessBtn = (By.CSS_SELECTOR, "#ManualRemoveAddress")
    addAddressBusinessBtn = (By.XPATH, "//button[@id='manualAddAddress']")

    def __init__(self, driver):
        self.driver = driver

    # Load the iframe in a new page Inner Redirect
    # Launch outer url
    def test_browser_load_outer(self):
        self.driver.get(self.outerUrl)
        self.driver.implicitly_wait(150)

    # Change the user to the outer Iframe
    @allure.description('Switch to iframe')
    def test_switchttoiframe(self):
        frame = self.driver.find_element(*self.iframelink)
        self.driver.switch_to.frame(frame)

    @allure.description('Click on LoadMore button')
    def test_loadMore(self):
        time.sleep(3)
        load = self.driver.find_element(*self.loadmore)

        try:
            for x in range(0, 6):
                display = self.driver.find_element(*self.loadmore).is_displayed()
                if display == True:
                    load.click()
        except:
            return False

    @allure.step('Show all counts of bank')
    def test_showall_banklist(self):
        time.sleep(2)
        list = self.driver.find_elements(*self.banklist)
        bank = len(list)
        print(bank)

    @allure.step('Check Link your bank')
    def test_link_your_bank(self, LinkYourBank):
        if LinkYourBank == 'Link your bank':
            try:
                link_bank = self.driver.find_element(*self.linkYourBankTxt)
            except:
                return False

        if LinkYourBank == link_bank.text:
            return True
        else:
            return False

    @allure.step('Check the placeholder of Search Bar')
    def test_place_holder_searchbar(self):
        print(self.driver.find_element(*self.searchBankPlaceHolder).get_attribute("placeholder"))

    @allure.step('Search a bank')
    def test_search_bank(self):
        # Search vopay
        self.driver.find_element(*self.searchBankPlaceHolder).send_keys('vopay')
        time.sleep(5)

        # select a bank
        self.driver.find_element(*self.vopayBank).click()
        time.sleep(5)

        # Click Continue
        self.driver.find_element(*self.continueBtn).click()
        time.sleep(5)

    def test_connect_my_bank_online(self):
        # Click Connect my bank online
        onlinebank = self.driver.find_element(*self.myBankOnline)
        onlinebank.click()
        time.sleep(5)
        return onlinebank

    def test_check_terms_of_use(self):
        # Check terms of Use
        terms_msg = 'By checking this you agree to the Terms of Use.'
        if terms_msg == self.termsOfUseTxt:
            return True
        else:
            return False

    def test_connect_my_bank_online_terms_of_use(self):
        # Click Terms of Use
        self.driver.find_element(*self.termsOfUseLink).click()
        time.sleep(5)

        # Click Cross button
        self.driver.find_element(*self.termsOfUseCrossBtn).click()
        time.sleep(5)

        # Accept terms
        # Check if checkbox is enabled
        try:
            checkboxEnabled = self.driver.find_element(*self.termsOfUseChecked)
            checkbox = checkboxEnabled.is_selected()
            if checkbox == False:
                checkboxEnabled.click()
        except:
            return False

    def test_connect_my_bank_online_invalid_credentials(self):
        # Populate invalid username and password
        invaliduser = 'vopaydemo!'
        invalidpass = 'vopay1234'

        self.driver.find_element(*self.userNameTxtBox).send_keys(invaliduser)
        self.driver.find_element(*self.passwordTxtBox).send_keys(invalidpass)
        time.sleep(5)

        # Click terms of use checkbox
        self.driver.find_element(*self.termsOfUseChecked).click()

        # Click Continue
        self.driver.find_element(*self.continueButton).click()
        time.sleep(10)

        # Check the error message
        err_msg = 'Your username or password are incorrect. Please try again.'
        if err_msg == self.bankFlowSubtitleUserPassIncorrect:
            return True
        else:
            return False

    def test_connect_my_bank_online_check_bank_flow_user_pass_err(self):
        # Check the error message
        err_msg = 'Your username or password are incorrect. Please try again.'
        if err_msg == self.bankFlowSubtitleUserPassIncorrect:
            return True
        else:
            return False

    def test_connect_my_bank_online_check_bank_flow_sec_reason_err(self):
        # Check the error message
        err_msg = 'For security reasons your account may be locked after several unsuccessful attempts.'
        if err_msg == self.bankFlowSubtitleSecReasons:
            return True
        else:
            return False

    def test_connect_my_bank_online_retry_login(self):
        # Click Retry Login
        self.driver.find_element(*self.retryLogin).click()
        time.sleep(10)

    def test_connect_my_bank_online_valid_credentials(self):
        # Populate valid username and password
        validuser = 'vopaydemo'
        validpass = 'vopaydemo'

        self.driver.find_element(*self.userNameTxtBox).send_keys(validuser)
        self.driver.find_element(*self.passwordTxtBox).send_keys(validpass)
        time.sleep(5)

        # Click terms of use checkbox
        self.driver.find_element(*self.termsOfUseChecked).click()

        # Click Continue
        self.driver.find_element(*self.continueButton).click()
        time.sleep(10)

    def test_connect_my_bank_online_verify_question(self, Identity):
        if Identity == 'What is the color of sky? Answer: blue':
            try:
                identity = self.driver.find_element(*self.bankFlowSubtitleSeparatorTxt)
            except:
                return False

        if Identity == 'Verify your identity':
            try:
                identity = self.driver.find_element(*self.bankFlowSubtitleIdentityTxt)
            except:
                return False

        if Identity == identity.text:
            return True
        else:
            return False

    def test_connect_my_bank_online_verify_identity_continue(self, BankFlow):
        # Click Continue
        self.driver.find_element(*self.continueBankBtn).click()
        time.sleep(5)

        # Check the sub title
        if BankFlow == 'Please provide the answer along with the user token.':
            try:
                bankflow = self.driver.find_element(*self.bankFlowSubtitleProvideAnswerTxt)
            except:
                return False

        if BankFlow == bankflow.text:
            return True
        else:
            return False

    def test_connect_my_bank_online_verify_answer(self):
        # Click Retry Question
        self.driver.find_element(*self.retryQuestion).click()
        time.sleep(5)

        # Populate the Answer
        answer = 'blue'
        self.driver.find_element(*self.answerTxtBox).send_keys(answer)
        time.sleep(5)

        # Click Continue
        self.driver.find_element(*self.continueBankBtn).click()
        time.sleep(5)

    def test_connect_my_bank_online_check_account(self, Account):
        # Check Available Accounts
        if Account == 'Please select an account':
            try:
                accnt = self.driver.find_element(*self.selectAccountTxt)
            except:
                return False

        if Account == 'Chequing (***9999)':
            try:
                accnt = self.driver.find_element(*self.chequingCADMasked)
            except:
                return False

        if Account == '$50,000.00 CAD':
            try:
                accnt = self.driver.find_element(*self.chequingCADBal)
            except:
                return False

        if Account == 'Chequing (***9988)':
            try:
                accnt = self.driver.find_element(*self.chequingUSDMasked)
            except:
                return False

        if Account == '$5,000.00 USD':
            try:
                accnt = self.driver.find_element(*self.chequingUSDBal)
            except:
                return False

        if Account == accnt.text:
            return True
        else:
            return False

    def test_connect_my_bank_online_select_account(self):
        # Click CAD Chequing Account
        self.driver.find_element(*self.chequingCADBtn).click()
        time.sleep(5)

        # Click CAD Chequing Account
        self.driver.find_element(*self.submitAccountBtn).click()
        time.sleep(5)

    def test_outer_redirect_token(self):
        # Get Current URL
        time.sleep(15)
        get = self.driver.current_url
        print(get)
        time.sleep(3)
        self.driver.switch_to.default_content()
        time.sleep(2)

        # Print the token from the container
        getcountOR = self.driver.find_element(*self.tokenprint).text
        print(getcountOR)
        string = str(get)
        token = string.split("&")
        print(token[0])
        string1 = str(token[0])
        getCount = string1.split("=")
        get1 = str(getCount[1])
        print(get1)
        # Check if token from the container is matched from the token url
        try:
            if str(getcountOR) == str(get1):
                return True
        except:
            return False

    def test_connect_my_bank_manually(self):
        # Click Connect my bank manually
        manualbank = self.driver.find_element(*self.myBankManually)
        manualbank.click()
        time.sleep(5)
        return manualbank

    def test_vopay_logo_exists(self):
        # Check if logo exists
        logo = self.driver.find_element(*self.vopayLogo).is_displayed()
        time.sleep(10)
        return logo

    def test_transit_account_nbr_value_required(self):
        value = '1'
        # Input transit number
        self.driver.find_element(*self.transitNbrTxtBox).send_keys(value)
        time.sleep(5)

        # Input account nbr
        self.driver.find_element(*self.accountNbrTxtBox).send_keys(value)
        time.sleep(5)

        # Click terms of use checkbox
        self.driver.find_element(*self.manualTermsOfUseTxt).click()
        time.sleep(5)

        # Click terms of use cross button
        self.driver.find_element(*self.termsOfUseCrossBtn).click()
        time.sleep(5)

    def test_manual_continue_btn(self):
        # Click Continue
        self.driver.find_element(*self.manualContinueBtn).click()
        time.sleep(5)

    def test_transit_account_nbr_value_too_short_err_msg(self, ErrorMessage):
        # Check Error Message
        if ErrorMessage == 'This value is too short. It should have 7 characters or more.':
            try:
                errormsg = self.driver.find_element(*self.accountNbrErrorMsg)
            except:
                return False

        if ErrorMessage == errormsg.text:
            return True
        else:
            return False

    def test_account_nbr_clear(self):
        # Clear Account Number
        account_nbr = self.driver.find_element(*self.accountNbrTxtBox)
        account_nbr.clear()
        account_nbr.send_keys(Keys.CONTROL + "a")
        account_nbr.send_keys(Keys.DELETE)
        time.sleep(5)

    def test_transit_nbr_clear(self):
        # Clear transit Number
        account_nbr = self.driver.find_element(*self.transitNbrTxtBox)
        account_nbr.clear()
        account_nbr.send_keys(Keys.CONTROL + "a")
        account_nbr.send_keys(Keys.DELETE)
        time.sleep(5)

    def test_valid_transit_account_nbr(self):
        # Input transit number
        self.driver.find_element(*self.transitNbrTxtBox).send_keys('99999')
        time.sleep(5)

        # Input account nbr
        self.driver.find_element(*self.accountNbrTxtBox).send_keys('9999999')
        time.sleep(5)

    def test_account_type(self, Account):
        # Check Account Type
        if Account == 'Select your Account Type':
            try:
                account = self.driver.find_element(*self.accountTypeTxt)
            except:
                return False

        # Check Personal Account
        if Account == 'Personal Account':
            try:
                account = self.driver.find_element(*self.personalAccountBtn)
            except:
                return False

        # Check Business Account
        if Account == 'Business Account':
            try:
                account = self.driver.find_element(*self.businessAccountBtn)
            except:
                return False

        if Account == account.text:
            return True
        else:
            return False

    def test_select_personal_account(self):
        # Click Personal Account
        self.driver.find_element(*self.personalAccountBtn).click()
        time.sleep(5)

    def test_manual_account_type_continue_btn(self):
        # Click Continue
        self.driver.find_element(*self.accountTypeBtn).click()
        time.sleep(5)

    def test_input_invalid_email(self):
        firstname = 'Kriselle'
        lastname = 'Tined'
        invalidemail = 'test!@@@gmail.com'
        phone = '7789178888'

        # Input First Name
        self.driver.find_element(*self.firstNameTxtBox).send_keys(firstname)

        # Input Last Name
        self.driver.find_element(*self.lastNameTxtBox).send_keys(lastname)

        # Input Invalid email
        self.driver.find_element(*self.emailTxtBox).send_keys(invalidemail)

        # Input Phone
        self.driver.find_element(*self.phoneTxtBox).send_keys(phone)

    def test_manual_personal_complete_continue_btn(self):
        # Click Continue
        self.driver.find_element(*self.manualPersonalBtn).click()
        time.sleep(5)

    def test_invalid_email_err_msg(self, InvalidEmail):
        # Check Error Message
        if InvalidEmail == 'This value should be a valid email.':
            try:
                invalidemail = self.driver.find_element(*self.invalidEmailErrorMsg)
            except:
                return False

        if InvalidEmail == invalidemail.text:
            return True
        else:
            return False

    def test_invalid_email_clear(self):
        # Clear Invalid email
        invalid_email = self.driver.find_element(*self.emailTxtBox)
        invalid_email.send_keys(Keys.CONTROL + "a")
        invalid_email.send_keys(Keys.DELETE)
        time.sleep(5)

    def test_input_valid_email(self):
        validemail = 'testing@gmail.com'
        # Input valid email
        self.driver.find_element(*self.emailTxtBox).send_keys(validemail)

    def test_add_my_address(self):
        self.driver.find_element(*self.addMyAddressTxt).click()
        time.sleep(5)

    def test_google_address(self):
        # Input Address
        address = '456 Test'

        self.driver.find_element(*self.addressDdl).click()
        time.sleep(2)

        self.driver.find_element(*self.addressDdl).send_keys(address)
        time.sleep(2)

        # Select google address
        actionchains = ActionChains(self.driver)
        actionchains.send_keys(Keys.ARROW_DOWN).perform()
        time.sleep(2)
        actionchains.send_keys(Keys.ENTER)
        time.sleep(5)

        postalcode = 'V5H 1C3'
        postal = self.driver.find_element(*self.postalCodeTxtBox)
        postal.click()
        postal.clear()
        postal.send_keys(postalcode)
        time.sleep(5)

    def test_scroll_down(self):
        ActionChains(self.driver).send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(5)

    def test_add_address(self):
        self.driver.find_element(*self.addAddressBtn).click()
        time.sleep(5)

    def test_get_outer_redirect_token(self):
        # Get Current URL
        get = self.driver.current_url
        print(get)

    def test_select_business_account(self):
        # Click Business Account
        self.driver.find_element(*self.businessAccountBtn).click()
        time.sleep(5)

    def test_add_company_name(self):
        companyname = 'Amazon International'
        firstname = 'Kriselle'
        lastname = 'Tined'
        phone = '7789178888'

        # Input Company Name
        self.driver.find_element(*self.companyNameTxtBox).send_keys(companyname)

        # Input First Name
        self.driver.find_element(*self.firstNameBusinessTxtBox).send_keys(firstname)

        # Input Last Name
        self.driver.find_element(*self.lastNameBusinessTxtBox).send_keys(lastname)

        # Input Phone
        self.driver.find_element(*self.phoneBusinessTxtBox).send_keys(phone)

    def test_add_my_address_business(self):
        self.driver.find_element(*self.addMyAddressBusinessTxt).click()
        time.sleep(5)

    def test_add_my_address_cancel(self):
        self.driver.find_element(*self.cancelRemoveBusinessBtn).click()
        time.sleep(5)

    def test_google_address_business_account(self):
        # Input Address
        address = '567'

        self.driver.find_element(*self.addressDdl).click()
        time.sleep(2)

        self.driver.find_element(*self.addressDdl).send_keys(address)
        time.sleep(2)

        # Select google address
        actionchains = ActionChains(self.driver)
        actionchains.send_keys(Keys.ARROW_DOWN).perform()
        time.sleep(2)
        actionchains.send_keys(Keys.ENTER)
        time.sleep(5)

    def test_add_address_business(self):
        self.driver.find_element(*self.addAddressBusinessBtn).click()
        time.sleep(5)