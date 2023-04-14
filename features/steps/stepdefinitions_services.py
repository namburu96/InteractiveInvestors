import time
from behave import *
from InteractiveInvestors.elements import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@given('i am on the interactive investors page')
def launch_browser(context):
    #Instantiating the driver
    s = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=s)
    context.driver.get("https://www.ii.co.uk/")
    context.driver.maximize_window()
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//button[normalize-space()='Accept']").click()
    print("the title of the page is", context.driver.title)
    if "Open an account" in context.driver.page_source:
        assert True
        print("you are on the Interactive Investors home page")
    elif "Whether you are looking for a general trading account, an ISA or a SIPP, we’ve got you covered with a low, flat fee." in context.driver.page_source:
        assert True
        print("you are on the Interactive Investors home page")
    else:
        assert False
        print("SORRY, this is not the Interactive Investors home page")


@when('i click on the services link in the header')
def services_link(context):
    context.driver.find_element(By.XPATH, Elements.services).click()
    time.sleep(1)


@then('the links in the services_account menu should work')
def services_accounts_menu(context):
    print(len(context.driver.find_elements(By.XPATH, Elements.services_accounts)))
    # Checking multiple links available
    for j in context.driver.find_elements(By.XPATH, Elements.services_accounts):
        print(j.text)
        name = j.text
        j.click()
        print(context.driver.current_url)
        time.sleep(1)
        title = context.driver.title
        print(title)
        if name == "Stocks and Shares ISA":
            assert title == "Stocks and Shares ISA | Open an ISA - interactive investor"
        elif name == "Trading Account":
            assert context.driver.title == "Trading Account | Open a Trading Account - interactive investor"
        elif name == "SIPP":
            assert context.driver.title == "Open a Self-Invested Personal Pension (SIPP) Today - interactive investor"
        elif name == "Junior ISA":
            assert context.driver.title == "Junior ISA | Junior Stocks and Shares ISA - interactive investor"
        elif name == "Cash Savings":
            assert context.driver.title == "Cash Savings - interactive investor"
        elif name == "See all accounts":
            assert context.driver.title == "Investment Account | Open an Online Investment Account - interactive investor"
        else:
            print("SORRY, this is not the correct page")
        context.driver.find_element(By.XPATH, Elements.services).click()
        time.sleep(1)


@then("the links in the services_investing menu should work")
def services_investing_menu(context):
    print(len(context.driver.find_elements(By.XPATH, Elements.services_investing)))
    # Checking multiple links available
    for j in context.driver.find_elements(By.XPATH, Elements.services_investing):
        print(j.text)
        name = j.text
        j.click()
        print(context.driver.current_url)
        time.sleep(1)
        title = context.driver.title
        print(title)
        if name == "Investing with ii":
            assert title == "Choosing ii for your investing needs - interactive investor"
        elif name == "Our charges":
            assert context.driver.title == "Our Trading Charges - interactive investor"
        elif name == "Transfer to ii":
            assert context.driver.title == "Transfer Your Investments | Transfer Investment Accounts - interactive investor"
        elif name == "Recommend ii":
            assert context.driver.title == "Recommend ii | Refer a friend - interactive investor"
        elif name == "Friends and Family":
            assert context.driver.title == "Friends and Family - give a free subscription to ii - interactive investor"
        else:
            print("SORRY, this is not the correct page")
        context.driver.find_element(By.XPATH, Elements.services).click()
        time.sleep(1)


@then("the links in the services_investment types menu should work")
def services_investmenttypes_menu(context):
    print(len(context.driver.find_elements(By.XPATH, Elements.services_investmenttype)))
    # Checking multiple links available
    for j in context.driver.find_elements(By.XPATH, Elements.services_investmenttype):
        print(j.text)
        name = j.text
        j.click()
        print(context.driver.current_url)
        time.sleep(1)
        title = context.driver.title
        print(title)
        if name == "Shares":
            assert title == "Stocks & Shares Prices | Today’s Live Markets - interactive investor"
        elif name == "Funds":
            assert context.driver.title == "Funds | Invest in Funds Today - interactive investor"
        elif name == "Investment trusts":
            assert context.driver.title == "Investment Trusts | Invest in Investment Trusts - interactive investor"
        elif name == "ETFs":
            assert context.driver.title == "Exchange Traded Funds & ETF Trading - interactive investor"
        elif name == "Bonds and Gilts":
            assert context.driver.title == "Buy Bonds & Gilts - interactive investor"
        elif name == "IPOs and new issues":
            assert context.driver.title == "Invest in New Shares Issues & IPOs - interactive investor"
        elif name == "US and international investing":
            assert context.driver.title == "International investing & share dealing - interactive investor"
        else:
            print("SORRY, this is not the correct page")
        context.driver.find_element(By.XPATH, Elements.services).click()
        time.sleep(1)
