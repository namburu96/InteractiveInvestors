import time
from behave import *
from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from InteractiveInvestors.elements import Elements

use_step_matcher("re")


@when("i click on the Help link in the header")
def help_link(context):
    context.driver.find_element(By.XPATH, Elements.help).click()
    time.sleep(1)


@then("the links in the help_investments menu should work")
def help_investments_menu(context):
    print(len(context.driver.find_elements(By.XPATH, Elements.help_investments)))
    # Checking multiple links available
    for j in context.driver.find_elements(By.XPATH, Elements.help_investments):
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
        elif name == "Sustainable investing":
            assert context.driver.title == "Sustainable Investing | Sustainable Investing Ideas - interactive investor"
        elif name == "International share dealing":
            assert context.driver.title == "International investing & share dealing - interactive investor"
        elif name == "Quarterly Investment Review":
            assert context.driver.title == "Quarterly Investment Review - interactive investor"
        else:
            print("SORRY, this is not the correct page")
        context.driver.find_element(By.XPATH, Elements.help).click()
        time.sleep(3)


@then("the links in the help_learn menu should work")
def help_learn_menu(context):
    print(len(context.driver.find_elements(By.XPATH, Elements.help_learn)))
    # Checking multiple links available
    for j in context.driver.find_elements(By.XPATH, Elements.help_learn):
        print(j.text)
        name = j.text
        j.click()
        print(context.driver.current_url)
        time.sleep(1)
        title = context.driver.title
        print(title)
        if name == "Knowledge Centre":
            assert title == "Knowledge Centre - interactive investor"
        elif name == "Free newsletters":
            assert context.driver.title == "Free news and investing insight - interactive investor"
        elif name == "What is a Stocks and Shares ISA?":
            assert context.driver.title == "What is a Stocks & Shares ISA? | ISA rules explained - interactive investor"
        elif name == "What is a SIPP?":
            assert context.driver.title == "What is a SIPP? | Self-Invested Pensions Explained - interactive investor"
        elif name == "SIPP vs ISA":
            assert context.driver.title == "SIPP vs ISA: Differences & which to choose - interactive investor"
        else:
            print("SORRY, this is not the correct page")
        context.driver.find_element(By.XPATH, Elements.help).click()
        time.sleep(3)


@then("the links in the help_help menu should work")
def help_help_menu(context):
    print(len(context.driver.find_elements(By.XPATH, Elements.help_help)))
    # Checking multiple links available
    for j in context.driver.find_elements(By.XPATH, Elements.help_help):
        try:
            print(j.text)
            name = j.text
            j.click()
            time.sleep(3)
            print(context.driver.current_url)
            title = context.driver.title
            print(title)
            if name == "Help Centre":
                assert title == "Help centre"
            elif name == "Useful forms":
                assert context.driver.title == "Useful Forms - interactive investor"
            elif name == "SIPP forms and documents":
                assert context.driver.title == "SIPP Documents and Forms - interactive investor"
            else:
                print("SORRY, this is not the correct page")
            context.driver.find_element(By.XPATH, "//span[@title='Help & Learning'][@class='css-38yhqv']").click()
            time.sleep(3)
        except (NoSuchElementException,StaleElementReferenceException):
                print("some problem with this element, will try again")


