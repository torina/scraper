from selenium import webdriver

#working code
BASE_URL = "http://www.canadiantire.ca/en/pdp/"

XPATH = '//span[@class="price__reg-value"]'
ITEMS = [['0540260p.html',100]]

driver = webdriver.Chrome()
for item in ITEMS:
    driver.get(BASE_URL+item[0])
    elem = driver.find_element_by_xpath(XPATH)
    print(elem.text)

driver.close()
