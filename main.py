from selenium import webdriver
import time
import pdb
import



driver = webdriver.Chrome("/Users/Hallshit/Downloads/chromedriver")

driver.get("https://weedmaps.com/deliveries/medi-green-express")
pagestart = 500
scrolllength = 780
x = 1
menu = {}
menuTotals = {}
indicaMenu = {}
sativaMenu = {}
hybridMenu = {}
extractMenu = {}
edibleMenu = {}
driver.execute_script("window.scrollTo(0, {});".format(pagestart))
time.sleep(3)
totals = driver.find_elements_by_tag_name('h3')
for total in totals[:5]:
    total = total.text.split('(')
    menuTotals[total[0][:-1]] = int(total[1][:-1])

def getIndicas():
    totalind = menuTotals['Indica']
    strains = []
    prices = []

    ycord = driver.find_element_by_xpath(
        '//*[@id="weedmenuPane"]/wm-menu/section[2]/div[1]/div/div[1]/div/div[1]/div[2]/button').location['y']
    driver.execute_script("window.scrollTo(0, {});".format(ycord - 60))
    time.sleep(3)
    driver.find_element_by_xpath(
        '//*[@id="weedmenuPane"]/wm-menu/section[2]/div[1]/div/div[1]/div/div[1]/div[2]/button').click()
    driver.execute_script("window.scrollTo(0, {});".format(ycord))
    pagestart = ycord
    for x in range(totalind):
        if (x + 1) % 11 == 0:
            driver.execute_script("window.scrollTo(0, {});".format(pagestart + scrolllength))
            pagestart = pagestart + scrolllength
            time.sleep(2)
        pricesEl = driver.find_elements_by_class_name('label-value')
        for price in pricesEl:
            if price in prices:
                continue
            else:
                prices.append(price.text)
        strainsEl = driver.find_elements_by_class_name('wm-menu-item-name')
        for strain in strainsEl:
            if strain in strains:
                continue
            else:
                strains.append(strain.text)
    for x in range(totalind):
        start = (x + 1) * 6 - 6
        currprices = prices[start:(x + 1) * 6]
        for y, price in enumerate(currprices):
            currprices[y] = price
        indicaMenu[strains[x]] = currprices
    return indicaMenu

def getSativas():
    totalsav = menuTotals['Sativa']
    prices = []
    strains = []
    ycord = driver.find_element_by_xpath(
        '//*[@id="weedmenuPane"]/wm-menu/section[2]/div[1]/div/div[2]/div/div[1]/div[2]/button').location['y']
    driver.execute_script("window.scrollTo(0, {});".format(ycord - 60))
    time.sleep(3)
    driver.find_element_by_xpath(
        '//*[@id="weedmenuPane"]/wm-menu/section[2]/div[1]/div/div[2]/div/div[1]/div[2]/button').click()
    time.sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="weedmenuPane"]/wm-menu/section[2]/div[1]/div/div[2]/div/div[1]/div[2]/button').click()
    driver.execute_script("window.scrollTo(0, {});".format(ycord))
    pagestart = ycord
    for x in range(totalsav):
        if (x + 1) % 11 == 0:
            driver.execute_script("window.scrollTo(0, {});".format(pagestart + scrolllength))
            pagestart = pagestart + scrolllength
            time.sleep(2)
        pricesEl = driver.find_elements_by_class_name('label-value')
        for price in pricesEl:
            if price in prices:
                continue
            else:
                prices.append(price.text)
        strainsEl = driver.find_elements_by_class_name('wm-menu-item-name')
        for strain in strainsEl:
            if strain in strains:
                continue
            else:
                strains.append(strain.text)
    for x in range(totalsav):
        start = (x + 1) * 6 - 6
        currprices = prices[start:(x + 1) * 6]
        for y, price in enumerate(currprices):
            currprices[y] = price
        sativaMenu[strains[x]] = currprices
    return sativaMenu


def getHybrids():
    totalhyb = menuTotals['Hybrid']
    prices = []
    strains = []
    ycord = driver.find_element_by_xpath(
        '//*[@id="weedmenuPane"]/wm-menu/section[2]/div[1]/div/div[3]/div/div[1]/div[2]/button').location['y']
    driver.execute_script("window.scrollTo(0, {});".format(ycord - 60))
    driver.find_element_by_xpath(
        '//*[@id="weedmenuPane"]/wm-menu/section[2]/div[1]/div/div[3]/div/div[1]/div[2]/button').click()
    time.sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="weedmenuPane"]/wm-menu/section[2]/div[1]/div/div[3]/div/div[1]/div[2]/button').click()
    driver.execute_script("window.scrollTo(0, {});".format(ycord))
    pagestart = ycord

    for x in range(totalhyb):
        if (x + 1) % 11 == 0:
            driver.execute_script("window.scrollTo(0, {});".format(pagestart + scrolllength))
            pagestart = pagestart + scrolllength
            time.sleep(2)
        pricesEl = driver.find_elements_by_class_name('label-value')
        for price in pricesEl:
            if price in prices:
                continue
            else:
                prices.append(price.text)
        strainsEl = driver.find_elements_by_class_name('wm-menu-item-name')
        for strain in strainsEl:
            if strain in strains:
                continue
            else:
                strains.append(strain.text)
    for x in range(totalhyb):
        start = (x + 1) * 6 - 6
        currprices = prices[start:(x + 1) * 6]
        for y, price in enumerate(currprices):
            currprices[y] = price
        hybridMenu[strains[x]] = currprices


    return hybridMenu

def getExtracts():
    totalext = menuTotals['Extract']
    prices = []
    strains = []
    ycord = driver.find_element_by_xpath(
        '//*[@id="weedmenuPane"]/wm-menu/section[2]/div[1]/div/div[4]/div/div[1]/div[2]/button').location['y']
    driver.execute_script("window.scrollTo(0, {});".format(ycord - 60))
    driver.find_element_by_xpath(
        '//*[@id="weedmenuPane"]/wm-menu/section[2]/div[1]/div/div[4]/div/div[1]/div[2]/button').click()
    time.sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="weedmenuPane"]/wm-menu/section[2]/div[1]/div/div[4]/div/div[1]/div[2]/button').click()
    driver.execute_script("window.scrollTo(0, {});".format(ycord))
    pagestart = ycord
    for x in range(totalext):
        if (x + 1) % 11 == 0:
            driver.execute_script("window.scrollTo(0, {});".format(pagestart + scrolllength))
            pagestart = pagestart + scrolllength
            time.sleep(2)
        pricesEl = driver.find_elements_by_class_name('label-value')
        for price in pricesEl:
            if price in prices:
                continue
            else:
                prices.append(price.text)
        strainsEl = driver.find_elements_by_class_name('wm-menu-item-name')
        for strain in strainsEl:
            if strain in strains:
                continue
            else:
                strains.append(strain.text)
    for x in range(totalext):
        start = (x + 1) * 3 - 3
        currprices = prices[start:(x + 1) * 3]
        for y, price in enumerate(currprices):
            currprices[y] = price
        extractMenu[strains[x]] = currprices
    return extractMenu

def getEdibles():
    totaledb = menuTotals['Edible']
    prices = []
    strains = []
    ycord = driver.find_element_by_xpath(
        '//*[@id="weedmenuPane"]/wm-menu/section[2]/div[1]/div/div[5]/div/div[1]/div[2]/div').location['y']
    driver.execute_script("window.scrollTo(0, {});".format(ycord - 60))
    driver.find_element_by_xpath(
        '//*[@id="weedmenuPane"]/wm-menu/section[2]/div[1]/div/div[5]/div/div[1]/div[2]/div').click()
    time.sleep(2)
    driver.find_element_by_xpath(
         '//*[@id="weedmenuPane"]/wm-menu/section[2]/div[1]/div/div[5]/div/div[1]/div[2]/div').click()
    driver.execute_script("window.scrollTo(0, {});".format(ycord))
    pagestart = ycord

    for x in range(totaledb):
        if (x + 1) % 11 == 0:
            driver.execute_script("window.scrollTo(0, {});".format(pagestart + scrolllength))
            pagestart = pagestart + scrolllength
            time.sleep(2)
        pricesEl = driver.find_elements_by_class_name('label-value')
        for price in pricesEl:
            if price in prices:
                continue
            else:
                prices.append(price.text)
        strainsEl = driver.find_elements_by_class_name('wm-menu-item-name')
        for strain in strainsEl:
            if strain in strains:
                continue
            else:
                strains.append(strain.text)
    for x in range(totaledb):
        start = x
        currprices = prices[start]

        edibleMenu[strains[x]] = currprices
    return edibleMenu










print menuTotals



indicaMenu = getIndicas()
sativaMenu = getSativas()
hybridMenu = getHybrids()
extractMenu = getExtracts()
edibleMenu = getEdibles()


print indicaMenu
print sativaMenu
print hybridMenu
print extractMenu
print edibleMenu



driver.close()

for item in indicaMenu:
    Weed.




