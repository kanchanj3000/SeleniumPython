from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import sys

driver = webdriver.Chrome("C:\Users\Friends\PycharmProjects\selenium\drivers\chromedriver.exe")
driver.get("https://www.makemytrip.com/")
driver.implicitly_wait(30)
driver.maximize_window()
import datetime
from datetime import timedelta

cabs = driver.find_element_by_xpath("//a[@id='header_tab_cabs']")
ActionChains(driver).move_to_element(cabs).click().perform()

froms = driver.find_element_by_xpath("//input[@id='hp-widget__sfrom']")
froms.clear()
froms.send_keys("Pune, Maharashtra, India")
froms.click()

to = driver.find_element_by_xpath("//input[@id='hp-widget__sTo']")
to.clear()
to.send_keys("Yavatmal, Maharashtra, India")
to.click()

k = datetime.datetime.now() + timedelta(days=2)
str_date = str(k.day)

new_xpath = "(//td[@class='ui-datepicker-week-end  ui-state-range']//a[text()='" + str_date + "'])[1]"
date =