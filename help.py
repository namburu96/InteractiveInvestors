from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import StaleElementReferenceException

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

# code
help=driver.find_element(By.XPATH, "//span[@title='Help & learning']")
help.click()


help_invest = driver.find_elements(By.XPATH,"//div[@id='navigationItemHelpLearning']//div[@class='ii-k008qs']//div[1]//ul[1]//li//a")
print(len(help_invest))
for i in help_invest:
    print(i.text)
    i.click()
    if name == "Quick-start Funds":
        assert driver.title == ""
    elif name == "Super 60 investments":
        assert driver.title == ""
    elif name == "ACE 40 sustainable investments":
        assert driver.title == ""
    elif name == "Model portfolios":
        assert driver.title == ""
    elif name == "Sustainable investing":
        assert driver.title == ""
    elif name == "International share dealing":
        assert driver.title == ""
    elif name == "Quarterly Investment Review":
        assert driver.title == ""
    else:
        print("nothing matched")
        exit()
    help.click()


help_learn = driver.find_elements(By.XPATH, "//div[@id='navigationItemHelpLearning']//div[@class='ii-k008qs']//div[2]//ul[1]//li//a")
print(len(help_learn))
for j in help_learn:
    print(j.text)
    j.click()
    if name == "Knowledge Centre":
        assert driver.title == ""
    elif name == "Free newsletters":
        assert driver.title == ""
    elif name == "What is a Stocks and Shares ISA?":
        assert driver.title == ""
    elif name == "What is a SIPP?":
        assert driver.title == ""
    elif name == "SIPP vs ISA":
        assert driver.title == ""

    else:
        print("nothing matched")
        exit()
    help.click()


help_help = driver.find_elements(By.XPATH, "//div[@id='navigationItemHelpLearning']//div[@class='ii-k008qs']//div[3]//ul//li//a")
print(len(help_help))
for k in help_help:
    if name == "Help Centre":
        assert driver.title == ""
    elif name == "":
        assert driver.title == ""
    elif name == "":
        assert driver.title == ""
    elif name == "":
        assert driver.title == ""
    elif name == "":
        assert driver.title == ""
    elif name == "":
        assert driver.title == ""
    elif name == "":
        assert driver.title == ""
    else:
        print("nothing matched")
        exit()
    try:
        print(k.text)
        k.click()
        help.click()
    except StaleElementReferenceException as Exception:
        print('StaleElementReferenceException while trying to click, trying to find element again')


