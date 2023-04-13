import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

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
driver.find_element(By.XPATH, "//button[normalize-space()='Accept']").click()

# the code
pensions=driver.find_element(By.XPATH, "//span[@title='Pensions']")
pensions.click()


pensions_pensions=driver.find_elements(By.XPATH, "//div[@id='navigationItemPensions']//div[@class='ii-k008qs']//div[1]//ul[1]//li//a")
print(len(pensions_pensions))

for i in pensions_pensions:
    print(i.text)
    name=i.text
    i.click()
    print(driver.current_url)
    time.sleep(1)
    print(driver.title)
    if name == "SIPP (Self-Invested Personal Pension)":
        assert driver.title == "Open a Self-Invested Personal Pension (SIPP) Today - interactive investor"
    elif name == "Transfer my pension":
        assert driver.title == "SIPP Transfer | Transfer your Pension - interactive investor"
    elif name == "SIPP charges":
        assert driver.title == "SIPP Charges, Rates and Fees - interactive investor"
    elif name== "SIPP investment ideas":
        assert driver.title == "SIPP Investment Ideas I Top SIPP Investments - interactive investor"
    elif name == "What is a SIPP?":
        assert driver.title == "What is a SIPP? | Self-Invested Pensions Explained - interactive investor"
    elif name == "Pension Trading Account":
        assert driver.title == "Pension Trading Account - interactive investor"
    else:
        print("nothing found")
        exit()

    pensions.click()
# //div[@id='navigationItemPensions']//div[@class='ii-k008qs']//div[2]//ul//li
# //div[@id='navigationItemPensions']//div[@class='ii-k008qs']//div[2]//ul//li//a
retirement_pensions=driver.find_elements(By.XPATH, "//div[@id='navigationItemPensions']//div[@class='ii-k008qs']//div[2]//ul//li//a")
print(len(retirement_pensions))
for j in retirement_pensions:
    print(j.text)
    name = j.text
    j.click()
    print(driver.current_url)
    time.sleep(1)
    print(driver.title)
    if name == "Options at retirement":
        assert driver.title == "Pension Options at Retirement | Income Options - interactive investor"
    elif name == "Tax-free lump sum":
        assert driver.title == "SIPP - tax-free lump sum - interactive investor"
    elif name == "SIPP drawdown":
        assert driver.title == "SIPP Drawdown | SIPP Income Drawdown - interactive investor"
    elif name == "Lump sums (UFPLS)":
        assert driver.title == "UFPLS Explained | Uncrystallised Funds Pension Lump Sum - interactive investor"
    elif name == "Investment Pathways":
        assert driver.title == "Drawdown Investment Pathways - interactive investor"
    elif name == "Pensions and retirement hub":
        assert driver.title == "Pensions Planning & Expert Ideas - interactive investor"
    else:
        print("nothing found")
        exit()

    pensions.click()
