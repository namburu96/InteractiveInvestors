import time
from behave import *
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from InteractiveInvestors.elements import Elements

use_step_matcher("re")


@when("i click on the Investments link in the header")
def investments_link(context):
    context.driver.find_element(By.XPATH, Elements.investments).click()
    time.sleep(1)


@then("the links in the Investments_shares menu should work")
def investments_share_menu(context):
    print(len(context.driver.find_elements(By.XPATH, Elements.investments_shares)))
    # Checking multiple links available
    for j in context.driver.find_elements(By.XPATH, Elements.investments_shares):
        print(j.text)
        name = j.text
        j.click()
        print(context.driver.current_url)
        time.sleep(1)
        title = context.driver.title
        print(title)
        if name == "Search shares":
            assert title == "Stocks & Shares Prices | Today’s Live Markets - interactive investor"
        elif name == "Top UK shares":
            assert context.driver.title == "Top Performing UK Shares | Today's Risers & Fallers - interactive investor"
        elif name == "Share dealing":
            assert context.driver.title == "Share Dealing Account | Low Cost Share Dealing & Investing - interactive investor"
        elif name == "Share tips & ideas":
            assert context.driver.title == "Share Tips and Ideas | UK and Global Share Tips & Ideas - interactive investor"
        elif name == "International share dealing":
            assert context.driver.title == "International investing & share dealing - interactive investor"
        else:
            print("SORRY, this is not the correct page")
        context.driver.find_element(By.XPATH, Elements.investments).click()
        time.sleep(3)


@then("the links in the Investments_funds menu should work")
def investments_funds_menu(context):
    print(len(context.driver.find_elements(By.XPATH, Elements.investments_funds)))
    # Checking multiple links available
    for j in context.driver.find_elements(By.XPATH, Elements.investments_funds):
        print(j.text)
        name = j.text
        j.click()
        print(context.driver.current_url)
        time.sleep(1)
        title = context.driver.title
        print(title)
        if name == "Search funds":
            assert title == "Funds | Invest in Funds Today - interactive investor"
        elif name == "Top funds":
            assert context.driver.title == "Top Investment Funds | Top Funds to invest in - interactive investor"
        elif name == "ETFs":
            assert context.driver.title == "Exchange Traded Funds & ETF Trading - interactive investor"
        elif name == "Investment trusts":
            assert context.driver.title == "Investment Trusts | Invest in Investment Trusts - interactive investor"
        elif name == "Sustainable investing":
            assert context.driver.title == "Sustainable Investing | Sustainable Investing Ideas - interactive investor"
        else:
            print("SORRY, this is not the correct page")
        context.driver.find_element(By.XPATH, Elements.investments).click()
        time.sleep(3)


@then("the links in the Investments_expertpicks menu should work")
def investments_expertpicks_menu(context):
    print(len(context.driver.find_elements(By.XPATH, Elements.investments_expertpicks)))
    # Checking multiple links available
    for j in context.driver.find_elements(By.XPATH, Elements.investments_expertpicks):
        print(j.text)
        name = j.text
        j.click()
        print(context.driver.current_url)
        time.sleep(1)
        title = context.driver.title
        print(title)
        if name == "Quick-start Funds":
            assert title == "Quick-start Funds | Ready-made Investment Portfolios - interactive investor"
        elif name == "Super 60 investments":
            assert context.driver.title == "ii Super 60 investment Portfolio Ideas - interactive investor"
        elif name == "ACE 40 sustainable investments":
            assert context.driver.title == "ii ACE 40 Sustainable Investment Ideas - interactive investor"
        elif name == "Model portfolios":
            assert context.driver.title == "Ready Made Investment Portfolios - interactive investor"
        elif name == "Investment Pathways":
            assert context.driver.title == "Drawdown Investment Pathways - interactive investor"
        else:
            print("SORRY, this is not the correct page")
        context.driver.find_element(By.XPATH, Elements.investments).click()
        time.sleep(3)


@then("the links in the Investments_markets menu should work")
def investments_markets_menu(context):
    print(len(context.driver.find_elements(By.XPATH, Elements.investments_markets)))
    # Checking multiple links available
    for j in context.driver.find_elements(By.XPATH, Elements.investments_markets):
        try:
            print(j.text)
            name = j.text
            j.click()
            print(context.driver.current_url)
            time.sleep(1)
            title = context.driver.title
            print(title)
            if name == "FTSE 100":
                assert title == "FTSE 100 (UKX) Index - interactive investor"
            elif name == "FTSE 250":
                assert context.driver.title == "FTSE 250 (MCX) Index - interactive investor"
            elif name == "FTSE All Share":
                assert context.driver.title == "FTSE All Share (ASX) Index - interactive investor"
            elif name == "NASDAQ":
                assert context.driver.title == "NASDAQ Composite (IXIC) Index - interactive investor"
            elif name == "Dow Jones":
                assert context.driver.title == "Dow Jones Industrial Average (DJIA) Index - interactive investor"
            elif name == "All markets":
                assert context.driver.title == "International markets - interactive investor - interactive investor"
            else:
                print("SORRY, this is not the correct page")
        except StaleElementReferenceException:
            print("some problem with this element, will try again")

        context.driver.find_element(By.XPATH, Elements.investments).click()
        time.sleep(3)

