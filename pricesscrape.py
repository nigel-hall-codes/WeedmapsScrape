from selenium import webdriver
import time

driver = webdriver.Chrome("/Users/Hallshit/Downloads/chromedriver")

driver.get("https://weedmaps.com/deliveries/medi-green-express")
pagestart = 300
scrolllength = 500
x = 1
menu = {}
"""To retrieve the indicas"""


driver.execute_script("window.scrollTo(0, {});".format(pagestart))
time.sleep(1)
ycord = driver.find_element_by_xpath('//*[@id="weedmenuPane"]/wm-menu/section[2]/div[1]/div/div[1]/div/div[1]/div[2]/button').location['y']
driver.execute_script("window.scrollTo(0, {});".format(ycord - 60))
time.sleep(3)
driver.find_element_by_xpath('//*[@id="weedmenuPane"]/wm-menu/section[2]/div[1]/div/div[1]/div/div[1]/div[2]/button').click()

prices = driver.find_elements_by_class_name('label-value')
for price in prices:
    print price.text
"""to retrieve the sativas"""
driver.execute_script("window.scrollTo(0, {});".format(pagestart + scrolllength))
ycord = driver.find_element_by_xpath('//*[@id="weedmenuPane"]/wm-menu/section[2]/div[1]/div/div[2]/div/div[1]/div[2]/button').location['y']
driver.execute_script("window.scrollTo(0, {});".format(ycord - 60))
driver.find_element_by_xpath('//*[@id="weedmenuPane"]/wm-menu/section[2]/div[1]/div/div[2]/div/div[1]/div[2]/button').click()

time.sleep(2)
driver.find_element_by_xpath('//*[@id="weedmenuPane"]/wm-menu/section[2]/div[1]/div/div[2]/div/div[1]/div[2]/button').click()
pagestart = ycord + scrolllength
time.sleep(3)
prices = driver.find_elements_by_class_name('label-value')

for price in prices:
    print price.text

"""To open all prices of the hybrids"""
driver.execute_script("window.scrollTo(0, {});".format(pagestart))
ycord = driver.find_element_by_xpath('//*[@id="weedmenuPane"]/wm-menu/section[2]/div[1]/div/div[3]/div/div[1]/div[2]/button').location['y']
driver.execute_script("window.scrollTo(0, {});".format(ycord - 60))
driver.find_element_by_xpath('//*[@id="weedmenuPane"]/wm-menu/section[2]/div[1]/div/div[3]/div/div[1]/div[2]/button').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="weedmenuPane"]/wm-menu/section[2]/div[1]/div/div[3]/div/div[1]/div[2]/button').click()
pagestart = ycord
while x < 10:
    prices = driver.find_elements_by_class_name('label-value')
    for price in prices:
        print price.text
    driver.execute_script("window.scrollTo(0, {});".format(pagestart + scrolllength))
    time.sleep(1)
    pagestart = scrolllength + pagestart
    x += 1




driver.close()

