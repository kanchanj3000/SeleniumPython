from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import sys

driver = webdriver.Chrome("C:\Users\Friends\PycharmProjects\selenium\drivers\chromedriver.exe")
driver.get("https://paytm.com/")
driver.implicitly_wait(30)
driver.maximize_window()

search = driver.find_element_by_xpath("//input[@type='search']")
search.send_keys("Moto g5")
search.send_keys(Keys.ENTER)
driver.implicitly_wait(20)


mobile_accessories = driver.find_element_by_xpath("(//span[@class='_2o8O'])[1]")
ActionChains(driver).move_to_element(mobile_accessories).click().perform()

mobiles = driver.find_element_by_xpath("//span[contains(text(),'Mobiles')]")
ActionChains(driver).move_to_element(mobiles).click().perform()

smartphones = driver.find_element_by_xpath("//a[contains(text(),'Smart Phones')]")
ActionChains(driver).move_to_element(smartphones).click().perform()

in_stock = driver.find_element_by_xpath("//span[@class='check']")
ActionChains(driver).move_to_element(in_stock).click().perform()

#mobile = driver.find_element_by_xpath("(//div[@class='_27VV'])[3]")
#ActionChains(driver).move_to_element(mobile).click().perform()

moto = driver.find_element_by_xpath("//img[@alt='Motorola Moto G5 XT1677 16 GB (Fine Gold)']")
driver.execute_script("arguments[0].scrollIntoView();",moto)
moto.click()


change = driver.find_element_by_xpath("//span[@class='_35OV']")
change.click()
#driver.execute_script("arguments[0].scrollIntoView();",change)
#change.click()

pin = driver.find_element_by_xpath("//input[@class='_3Jju']")
pin.send_keys("445204")
pin.send_keys(Keys.ENTER)


checkbox = driver.find_element_by_xpath("//span[@class='check']")
ActionChains(driver).move_to_element(checkbox).click().perform()

sys.exit()



code = driver.find_element_by_xpath("(//span[@class='eLIZ'])[2]")
ActionChains(driver).move_to_element(code).click().perform()








#//div[@class='_2AaQ']//span[@class='_350V']