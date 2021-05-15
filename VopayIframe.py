import time
import allure
from Iframe.Vopaypages import VopayPages
from resources.variables import *
from selenium import webdriver

"""Vopay Iframe"""
"""Outer Html page"""

@allure.suite('Vopay Outer Iframe')
@allure.title('Launch vopay iframe outer page(Vopay Outer)')
def test_cases_VopayOuter(browser):
    global vopay
    vopay = VopayPages(browser)
    vopay.test_browser_load_outer()

@allure.suite('Vopay Outer Iframe')
@allure.title('To loadmore banks and get counts of all bank(Vopay Outer)')
def test_countbank_VopayOuter(browser):
    vopay.test_switchttoiframe()
    vopay.test_loadMore()
    vopay.test_showall_banklist()

@allure.suite('Vopay Outer Iframe')
@allure.title('Check link your bank')
def test_linkyourbank(browser):
    assert vopay.test_link_your_bank('Link your bank') == True, "Link your bank - text not found"

@allure.suite('Vopay Outer Iframe')
@allure.title('Search bank')
def test_search_bank(browser):
    vopay.test_place_holder_searchbar()
    vopay.test_search_bank()

@allure.suite('Vopay Outer Iframe')
@allure.title('Connect my bank online')
def test_my_bank_online(browser):
    vopay.test_connect_my_bank_online()
    vopay.test_check_terms_of_use()
    vopay.test_connect_my_bank_online_terms_of_use()
    vopay.test_connect_my_bank_online_invalid_credentials()
    vopay.test_connect_my_bank_online_check_bank_flow_user_pass_err()
    vopay.test_connect_my_bank_online_check_bank_flow_sec_reason_err()
    vopay.test_connect_my_bank_online_retry_login()

@allure.suite('Vopay Outer Iframe')
@allure.title('Online banking credentials')
def test_my_bank_online_valid_credentials(browser):
    vopay.test_connect_my_bank_online_valid_credentials()
    assert vopay.test_connect_my_bank_online_verify_question('What is the color of sky? Answer: blue') == True, "What is the color of sky? Answer: blue - text not found"
    assert vopay.test_connect_my_bank_online_verify_question('Verify your identity') == True, "Verify your identity - text not found"
    assert vopay.test_connect_my_bank_online_verify_identity_continue('Please provide the answer along with the user token.') == True, "Please provide the answer along with the user token. - text not found"
    vopay.test_connect_my_bank_online_verify_answer()
    assert vopay.test_connect_my_bank_online_check_account('Please select an account') == True, "Please select an account - text not found"
    assert vopay.test_connect_my_bank_online_check_account('Chequing (***9999)') == True, "Chequing (***9999) - text not found"
    assert vopay.test_connect_my_bank_online_check_account('$50,000.00 CAD') == True, "$50,000.00 CAD - text not found"
    assert vopay.test_connect_my_bank_online_check_account('Chequing (***9988)') == True, "Chequing (***9988) - text not found"
    assert vopay.test_connect_my_bank_online_check_account('$5,000.00 USD') == True, "$5,000.00 USD - text not found"
    vopay.test_connect_my_bank_online_select_account()
    vopay.test_outer_redirect_token()

@allure.suite('Vopay Outer Iframe')
@allure.title('Connect my bank manually')
def test_connect_my_bank_manually(browser):
    vopay.test_browser_load_outer()
    vopay.test_switchttoiframe()
    vopay.test_loadMore()
    vopay.test_showall_banklist()
    vopay.test_place_holder_searchbar()
    vopay.test_search_bank()
    vopay.test_connect_my_bank_manually()

@allure.suite('Vopay Outer Iframe')
@allure.title('Manual banking credentials')
def test_my_bank_manually(browser):
    vopay.test_vopay_logo_exists()
    vopay.test_transit_account_nbr_value_required()
    vopay.test_manual_continue_btn()
    assert vopay.test_transit_account_nbr_value_too_short_err_msg('This value is too short. It should have 7 characters or more.') == True, "This value is too short. It should have 7 characters or more. - text not found"
    vopay.test_account_nbr_clear()
    vopay.test_transit_nbr_clear()
    vopay.test_valid_transit_account_nbr()
    vopay.test_manual_continue_btn()

@allure.suite('Vopay Outer Iframe')
@allure.title('Manual banking Account type')
def test_my_bank_manually_account_type(browser):
    assert vopay.test_account_type('Select your Account Type') == True, "Select your Account Type - text not found"
    assert vopay.test_account_type('Personal Account') == True, "Personal Account - text not found"
    assert vopay.test_account_type('Business Account') == True, "Business Account - text not found"

@allure.suite('Vopay Outer Iframe')
@allure.title('Manual banking Account type - Personal Account')
def test_my_bank_manually_personal_account(browser):
    vopay.test_select_personal_account()
    vopay.test_manual_account_type_continue_btn()
    vopay.test_input_invalid_email()
    vopay.test_manual_personal_complete_continue_btn()
    assert vopay.test_invalid_email_err_msg('This value should be a valid email.') == True, "This value should be a valid email. - text not found"
    vopay.test_invalid_email_clear()
    vopay.test_input_valid_email()
    vopay.test_add_my_address()
    vopay.test_google_address()
    vopay.test_scroll_down()
    vopay.test_add_address()
    vopay.test_manual_personal_complete_continue_btn()
    vopay.test_get_outer_redirect_token()

@allure.suite('Vopay Outer Iframe')
@allure.title('Connect my bank manually - Business Account')
def test_connect_my_bank_manually_business_account(browser):
    vopay.test_browser_load_outer()
    vopay.test_switchttoiframe()
    vopay.test_search_bank()
    vopay.test_connect_my_bank_manually()
    vopay.test_vopay_logo_exists()
    vopay.test_transit_account_nbr_value_required()
    vopay.test_manual_continue_btn()
    assert vopay.test_transit_account_nbr_value_too_short_err_msg('This value is too short. It should have 7 characters or more.') == True, "This value is too short. It should have 7 characters or more. - text not found"
    vopay.test_account_nbr_clear()
    vopay.test_transit_nbr_clear()
    vopay.test_valid_transit_account_nbr()
    vopay.test_manual_continue_btn()
    vopay.test_select_business_account()
    vopay.test_manual_account_type_continue_btn()

@allure.suite('Vopay Outer Iframe')
@allure.title('Connect my bank manually - Business Account Add Company Name and Address')
def test_connect_my_bank_manually_business_account_add_company_name(browser):
    vopay.test_add_company_name()
    vopay.test_add_my_address_business()
    vopay.test_add_my_address_cancel()
    vopay.test_add_my_address_business()
    vopay.test_google_address_business_account()
    vopay.test_scroll_down()
    vopay.test_add_address_business()
    vopay.test_get_outer_redirect_token()