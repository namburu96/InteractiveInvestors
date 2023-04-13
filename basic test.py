import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)


driver.maximize_window()
driver.get("https://www.ii.co.uk")


driver.find_element(By.XPATH, "//div[@class='chakra-stack ii-10ritmr']/button").click()
# if "Open an account" in driver.page_source:
#     assert True
#     print("you are on the correct page")
# elif "Whether you are looking for a general trading account, an ISA or a SIPP, we’ve got you covered with a low, flat fee." in driver.page_source:
#     assert True
#     print("you are on the correct page")
# else:
#     assert False
#     print("this is not the correct page")
#
# driver.find_element(By.XPATH, "//button[normalize-space()='Accept']").click()
# print("the title of the page is", driver.title)
#
# driver.find_element(By.XPATH, "//span[@title='Services']").click()
# driver.find_element(By.XPATH, "//a[@class='chakra-link chakra-link ii-y41h9l'][normalize-space()='Trading Account']").click()

if "Open an account" in driver.page_source:
    assert True
    print("you are on the correct page")
elif "Whether you are looking for a general trading account, an ISA or a SIPP, we’ve got you covered with a low, flat fee." in driver.page_source:
    assert True
    print("you are on the correct page")
else:
    assert False
    print("this is not the correct page")

driver.find_element(By.XPATH, "//span[@title='Services']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//a[@class='chakra-link chakra-link ii-y41h9l'][normalize-space()='Trading Account']").click()


if "Ready to open your Trading Account?" in driver.page_source:
    assert True
    print("yes, this is Trading account page")
else:
    print("this is not trading account page")
    assert False
