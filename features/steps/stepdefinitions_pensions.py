import time
from behave import *
from selenium.webdriver.common.by import By
from InteractiveInvestors.elements import Elements

use_step_matcher("re")


@when("i click on the Pensions link in the header")
def pensions_link(context):
    context.driver.find_element(By.XPATH, Elements.pensions).click()
    time.sleep(1)


@then("the links in the Pensions_pensions menu should work")
def pensions_pensions_menu(context):
    # Checking multiple links available
    print(len(context.driver.find_elements(By.XPATH, Elements.pensions_pensions)))
    for j in context.driver.find_elements(By.XPATH, Elements.pensions_pensions):
        print(j.text)
        name = j.text
        j.click()
        print(context.driver.current_url)
        time.sleep(1)
        title = context.driver.title
        print(title)
        if name == "SIPP (Self-Invested Personal Pension)":
            assert title == "Open a Self-Invested Personal Pension (SIPP) Today - interactive investor"
        elif name == "Transfer my pension":
            assert context.driver.title == "SIPP Transfer | Transfer your Pension - interactive investor"
        elif name == "SIPP charges":
            assert context.driver.title == "SIPP Charges, Rates and Fees - interactive investor"
        elif name == "SIPP investment ideas":
            assert context.driver.title == "SIPP Investment Ideas I Top SIPP Investments - interactive investor"
        elif name == "What is a SIPP?":
            assert context.driver.title == "What is a SIPP? | Self-Invested Pensions Explained - interactive investor"
        elif name == "Pension Trading Account":
            assert context.driver.title == "Pension Trading Account - interactive investor"
        else:
            print("SORRY, this is not the correct page")
        context.driver.find_element(By.XPATH, Elements.pensions).click()
        time.sleep(3)


@then("the links in the Pensions_retirement menu should work")
def pensions_retirement(context):
    #Checking multiple links available
    print(len(context.driver.find_elements(By.XPATH, Elements.pensions_retirement)))
    for j in context.driver.find_elements(By.XPATH, Elements.pensions_retirement):
        print(j.text)
        name = j.text
        j.click()
        print(context.driver.current_url)
        time.sleep(1)
        title = context.driver.title
        print(title)
        if name == "Options at retirement":
            assert title == "Pension Options at Retirement | Income Options - interactive investor"
        elif name == "Tax-free lump sum":
            assert context.driver.title == "SIPP - tax-free lump sum - interactive investor"
        elif name == "SIPP drawdown":
            assert context.driver.title == "SIPP Drawdown | SIPP Income Drawdown - interactive investor"
        elif name == "Lump sums (UFPLS)":
            assert context.driver.title == "UFPLS Explained | Uncrystallised Funds Pension Lump Sum - interactive investor"
        elif name == "Investment Pathways":
            assert context.driver.title == "Drawdown Investment Pathways - interactive investor"
        elif name == "Pensions and retirement hub":
            assert context.driver.title == "Pensions Planning & Expert Ideas - interactive investor"
        else:
            print("SORRY, this is not the correct page")
        context.driver.find_element(By.XPATH, Elements.pensions).click()
        time.sleep(3)
