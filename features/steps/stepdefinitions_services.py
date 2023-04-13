import time

from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@given('i am on the interactive investors page')
def launch_browser(context):
    s = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=s)
    context.driver.get("https://www.ii.co.uk/")
    context.driver.maximize_window()
    time.sleep(1)
    context.driver.find_element(By.XPATH, "//button[normalize-space()='Accept']").click()
    print("the title of the page is", context.driver.title)
    if "Open an account" in context.driver.page_source:
        assert True
        print("you are on the correct page")
    elif "Whether you are looking for a general trading account, an ISA or a SIPP, we’ve got you covered with a low, flat fee." in context.driver.page_source:
        assert True
        print("you are on the correct page")
    else:
        assert False
        print("this is not the correct page")


@when('i click on the services link in the header')
def services_link(context):
    services = context.driver.find_element(By.XPATH, "//span[@title='Services']")
    services.click()
    time.sleep(1)


@then('the links in the services menu should work')
def services_menu(context):
    accounts_ele = context.driver.find_elements(By.XPATH,
                                                "//div[@id='navigationItemServices']//div[@class='ii-d8uz43']//a[contains(@href,'ii-accounts')]")
    print(len(accounts_ele))
    for j in accounts_ele:
        print(j.text)
        name = j.text
        j.click()
        print(context.driver.current_url)
        time.sleep(1)
        title = context.driver.title
        if name == "Stocks and Shares ISA":
            print(title)
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
            print("nothing matched")
            exit()
        context.driver.find_element(By.XPATH, "//span[@title='Services']").click()
