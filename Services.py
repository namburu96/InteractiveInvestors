import time

from selenium import webdriver
# from selenium.webdriver.support.ui import  WebDriverWait
# from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# import selenium.webdriver.chromium.service
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.core.utils import ChromeType
# from webdriver_manager.chromium import ChromiumDriverManager


s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
# wait=WebDriverWait(driver,10)
# driver.implicitly_wait(20)
driver.maximize_window()
driver.get("https://www.ii.co.uk/")
# title = driver.title
#
# if title == "interactive investor – the UK’s number one flat-fee investment platform":
#     assert True
# elif title == "Homepage - interactive investor":
#     assert True
# else:
#     print("Some other title has been found which is " + title)

if "Open an account" in driver.page_source:
    assert True
    print("you are on the correct page")
elif "Whether you are looking for a general trading account, an ISA or a SIPP, we’ve got you covered with a low, flat fee." in driver.page_source:
    assert True
    print("you are on the correct page")
else:
    assert False
    print("this is not the correct page")

driver.find_element(By.XPATH, "//button[normalize-space()='Accept']").click()

print("the title of the page is", driver.title)

# header_ele = driver.find_element(By.XPATH,
#                                  "//body/div[@id='root']/div[@class='ii-eqgpbd']/header[@class='ii-t8pnep']/div[@class='chakra-stack ii-z8pqfj']/nav[@class='ii-1cuznq2']/ul[@class='ii-9e6kxj']/li")
# print("the no of header elements in nav bar =", len(header_ele))
# for i in header_elements:
#     print(i.text)
#     i.click()
# services_elements=driver.find_elements(By.XPATH, "//div[@id='navigationItemServices']//div[@class='ii-k008qs']//div")
# # print(len(services_elements))
# for j in services_elements:
#     print(j.text)
services = driver.find_element(By.XPATH, "//span[@title='Services']")
services.click()
accounts_ele = driver.find_elements(By.XPATH,
                                    "//div[@id='navigationItemServices']//div[@class='ii-d8uz43']//a[contains(@href,'ii-accounts')]")
print(len(accounts_ele))
for j in accounts_ele:
    print(j.text)
    name=j.text
    j.click()
    print(driver.current_url)
    # wait=WebDriverWait(driver,10)
    # wait.until(EC.title_is(driver.title))
    time.sleep(3)
    title = driver.title

    if name == "Stocks and Shares ISA":
        print(title)
        assert title == "Stocks and Shares ISA | Open an ISA - interactive investor"
    elif name == "Trading Account":
        assert driver.title == "Trading Account | Open a Trading Account - interactive investor"
    elif name == "SIPP":
        assert driver.title == "Open a Self-Invested Personal Pension (SIPP) Today - interactive investor"
    elif name == "Junior ISA":
        assert driver.title == "Junior ISA | Junior Stocks and Shares ISA - interactive investor"
    elif name == "Cash Savings":
        assert driver.title == "Cash Savings - interactive investor"
    elif name == "See all accounts":
        assert driver.title == "Investment Account | Open an Online Investment Account - interactive investor"
    else:
        print("nothing matched")
        exit()
    services.click()
investing_ele = driver.find_elements(By.XPATH,
                                     "//div[@id='navigationItemServices']//div[2]//ul[1]//a[@class='chakra-link chakra-link ii-y41h9l']")
print(len(investing_ele))
for k in investing_ele:
    print(k.text)
    name = k.text
    k.click()
    time.sleep(3)
    if name == "Investing with ii":
        assert driver.title == "Choosing ii for your investing needs - interactive investor"
    elif name == "Our charges":
        assert driver.title == "Our Trading Charges - interactive investor"
    elif name == "Transfer to ii":
        assert driver.title == "Transfer Your Investments | Transfer Investment Accounts - interactive investor"
    elif name == "Recommend ii":
        assert driver.title == "Recommend ii | Refer a friend - interactive investor"
    elif name == "Friends and Family":
        assert driver.title == "Friends and Family - give a free subscription to ii - interactive investor"
    else:
        print("nothing matched")
        exit()
    services.click()
investmenttype_ele = driver.find_elements(By.XPATH,
                                          "//div[@id='navigationItemServices']//div[3]//ul[1]//a[@class='chakra-link chakra-link ii-y41h9l']")
print(len(investmenttype_ele))
for l in investmenttype_ele:
    print(l.text)
    name = l.text
    l.click()
    time.sleep(3)
    if name == "Shares":
        assert driver.title == "Stocks & Shares Prices | Today’s Live Markets - interactive investor"
    elif name == "Funds":
        assert driver.title == "Funds | Invest in Funds Today - interactive investor"
    elif name == "Investment trusts":
        assert driver.title == "Investment Trusts | Invest in Investment Trusts - interactive investor"
    elif name == "ETFs":
        assert driver.title == "Exchange Traded Funds & ETF Trading - interactive investor"
    elif name == "Bonds and Gilts":
        assert driver.title == "Buy Bonds & Gilts - interactive investor"
    elif name == "IPOs and new issues":
        assert driver.title == "Invest in New Shares Issues & IPOs - interactive investor"
    elif name == "US and international investing":
        assert driver.title == "International investing & share dealing - interactive investor"
    else:
        print("nothing matched")
        exit()
    services.click()
    # i.click()
    # driver.find_element(By.XPATH, "//body[1]/div[4]/div[1]/header[1]/div[1]/nav[1]/ul[1]/li[1]/div[2]/div[1]/div[3]/ul[1]/li[1]").click()

    # j.click()
#     services_accounts=driver.find_elements(By.XPATH, "//div[@id='navigationItemServices']//div[@class='ii-k008qs']//div[1]//ul[1]//li")
#     for h in services_accounts:
#         print(len(services_accounts))
#         print(h.text)
#         h.click()
# if "Stocks and Shares ISA" in driver.page_source:
#     assert True
# elif driver.title=="Trading Account | Open a Trading Account - interactive investor":
#     assert True
# elif driver.title=="Open a Self-Invested Personal Pension (SIPP) Today - interactive investor":
#     assert True
# elif driver.title=="Junior ISA | Junior Stocks and Shares ISA - interactive investor":
#     assert True
# elif driver.title=="Cash Savings - interactive investor":
#     assert True
# elif driver.title=="Investment Account | Open an Online Investment Account - interactive investor":
#     assert True
# else:
#     assert False

# assert driver.title == "interactive investor – the UK’s number one flat-fee investment platform"

# driver.find_element(By.XPATH,
#                     "//body/div[@id='root']/div[@class='ii-eqgpbd']/header[@class='ii-t8pnep']/div[@class='chakra-stack ii-z8pqfj']/nav[@class='ii-1cuznq2']/ul[@class='ii-9e6kxj']/li[1]").click()
# driver.find_element(By.XPATH,
#                     "//a[@class='chakra-link chakra-link ii-y41h9l'][normalize-space()='Trading Account']").click()

# title="Trading Account | Open a Trading Account - interactive investor"
# print(driver.title)
# # assert driver.title == title


#
# url = driver.current_url
# if url == "https://www.ii.co.uk/ii-accounts/trading-account":
#     assert True
# else:
#     assert False
#
# if "Ready to open your Trading Account?" in driver.page_source:
#     assert True
# else:
#     assert False
#

# driver.close()
