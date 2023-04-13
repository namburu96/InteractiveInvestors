import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import ElementNotInteractableException

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.implicitly_wait(10)
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
driver.find_element(By.XPATH, "//div[@class='chakra-stack ii-10ritmr']/button").click()
investments = driver.find_element(By.XPATH, "//span[@title='Investments']")
investments.click()

# code

# investments_shares=driver.find_elements(By.XPATH, "//div[@id='navigationItemInvestments']//div[@class='ii-k008qs']//div[1]//ul//li//a")
# print(len(investments_shares))
#
# for i in investments_shares:
#     print(i.text)
#     name=i.text
#     i.click()
#     time.sleep(1)
#     print(driver.current_url)
#     if name == "Search shares":
#         assert driver.title == "Stocks & Shares Prices | Today’s Live Markets - interactive investor"
#     elif name == "Top UK shares":
#         assert driver.title == "Top Performing UK Shares | Today's Risers & Fallers - interactive investor"
#     elif name == "Share dealing":
#         assert driver.title == "Share Dealing Account | Low Cost Share Dealing & Investing - interactive investor"
#     elif name == "Share tips & ideas":
#         assert driver.title == "Share Tips and Ideas | UK and Global Share Tips & Ideas - interactive investor"
#     elif name == "International share dealing":
#         assert driver.title == "International investing & share dealing - interactive investor"
#     else:
#         print("nothing found")
#
#     investments.click()
#
# investments_funds= driver.find_elements(By.XPATH, "//div[@id='navigationItemInvestments']//div[@class='ii-k008qs']//div[2]//ul//li//a")
# print(len(investments_funds))
# for j in investments_funds:
#     print(j.text)
#     name=j.text
#     j.click()
#     time.sleep(1)
#     if name == "Search funds":
#         assert driver.title == "Funds | Invest in Funds Today - interactive investor"
#     elif name == "Top funds":
#         assert driver.title == "Top Investment Funds | Top Funds to invest in - interactive investor"
#     elif name == "ETFs":
#         assert driver.title == "Exchange Traded Funds & ETF Trading - interactive investor"
#     elif name == "Investment trusts":
#         assert driver.title == "Investment Trusts | Invest in Investment Trusts - interactive investor"
#     elif name == "Sustainable investing":
#         assert driver.title == "Sustainable Investing | Sustainable Investing Ideas - interactive investor"
#
#     else:
#         print("nothing found")
#     investments.click()
#
# investments_expertpicks=driver.find_elements(By.XPATH, "//div[@id='navigationItemInvestments']//div[@class='ii-k008qs']//div[3]//ul//li//a")
# print(len(investments_expertpicks))
# for k in investments_expertpicks:
#     print(k.text)
#     name=k.text
#     k.click()
#     time.sleep(1)
#     if name == "Quick-start Funds":
#         assert driver.title == "Quick-start Funds | Ready-made Investment Portfolios - interactive investor"
#     elif name == "Super 60 investments":
#         assert driver.title == "ii Super 60 investment Portfolio Ideas - interactive investor"
#     elif name == "ACE 40 sustainable investments":
#         assert driver.title == "ii ACE 40 Sustainable Investment Ideas - interactive investor"
#     elif name == "Model portfolios":
#         assert driver.title == "Ready Made Investment Portfolios - interactive investor"
#     elif name == "Investment Pathways":
#         assert driver.title == "Drawdown Investment Pathways - interactive investor"
#     else:
#         print("nothing found")
#     investments.click()
# # //div[@id='navigationItemInvestments']//div[@class='css-k008qs']//div[4]//ul/li/a
# # "//div[@id='navigationItemInvestments']//div[@class='ii-k008qs']//div[4]//ul//a"
# //div[@id='navigationItemInvestments']//div[4]//ul/li


investments_markets = driver.find_elements(By.XPATH, "//div[@id='navigationItemInvestments']//div[4]//ul[1]//li//a")
print(len(investments_markets))
for l in investments_markets:
    # time.sleep(2)
    print(l.text)
    name = l.text
    l.click()
    time.sleep(5)
    print(driver.title)
    print(driver.current_url)

    # investments = driver.find_element(By.XPATH, "//span[@title='Investments']")
    # investments.click()

    if name == "FTSE 100":
        assert driver.title == "FTSE 100 (UKX) Index - interactive investor"
    elif name == "FTSE 250":
        assert driver.title == "FTSE 250 (MCX) Index - interactive investor"
    elif name == "FTSE All Share":
        assert driver.title == "FTSE All Share (ASX) Index - interactive investor"
    elif name == "NASDAQ":
        assert driver.title == "NASDAQ Composite (IXIC) Index - interactive investor"
    elif name == "Dow Jones":
        assert driver.title == "Dow Jones Industrial Average (DJIA) Index - interactive investor"
    elif name == "All markets":
        assert driver.title == "International markets - interactive investor - interactive investor"
    else:
        print("nothing found")

    ele=driver.find_element(By.XPATH, "//span[@title='Investments']")
    ele.click()
# try:
#     print(l.text)
#     l.click()
#
#     investments.click()
# except ElementNotInteractableException as Exception:
#     print('ElementNotInteractableException while trying to click, trying to find element again')
#
#
#
