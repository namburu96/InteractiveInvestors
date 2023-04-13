import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://www.ii.co.uk")

if "Open an account" in driver.page_source:
    assert True
    print("you are on the correct page")
elif "Whether you are looking for a general trading account, an ISA or a SIPP, we’ve got you covered with a low, flat fee." in driver.page_source:
    assert True
    print("you are on the correct page")
else:
    assert False
    print("this is not the correct page")
# cookie_accept
driver.find_element(By.XPATH, "//button[normalize-space()='Accept']").click()

driver.find_element(By.XPATH, "//span[@title='News']").click()

time.sleep(1)
print(driver.current_url)
title = driver.title

if title == "Latest Stock Market News & Analysis":
    assert True

else:
    print("wrong page")

