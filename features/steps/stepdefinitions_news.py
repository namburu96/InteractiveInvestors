import time
from behave import *
from selenium.webdriver.common.by import By
from InteractiveInvestors.elements import Elements

use_step_matcher("re")


@when("i click on the news link in the header")
def news_link(context):
    context.driver.find_element(By.XPATH, Elements.news).click()
    time.sleep(1)


@then("the news link should work")
def news_link(context):
    print(context.driver.current_url)
    title = context.driver.title
    print(title)
    if title == "Latest Stock Market News & Analysis":
        assert True
    else:
        print("SORRY, this is not the correct page")
