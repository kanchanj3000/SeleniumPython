from selenium import webdriver
from selenium.webdriver.support.select import Select
import sys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome("C:\Users\Friends\PycharmProjects\selenium\drivers\chromedriver.exe")
driver.get("https://www.makemytrip.com/")
driver.implicitly_wait(30)
driver.maximize_window()

bus = driver.find_element_by_xpath("//a[@id='header_tab_bus']")
bus.click()

textbox = driver.find_element_by_xpath("//input[@id='hp-widget__sfrom']")
textbox.clear()
textbox.send_keys("Pune")
textbox.click()

textbox1 = driver.find_element_by_xpath("//input[@id='hp-widget__sTo']")
textbox1.clear()
textbox1.send_keys("Yavatmal")

import datetime

from datetime import timedelta
k = datetime.datetime.now() + timedelta(days=2)
start_day = str(k.day)


xpath_new = "//*[@class='ui-datepicker-group ui-datepicker-group-first']//a[text()='" + start_day + "']"
date = driver.find_element_by_xpath("//input[@id='hp-widget__depart']")
date.click()
driver.find_element_by_xpath(xpath_new).click()

search = driver.find_element_by_xpath("//button[@id='searchBtn']")
search.click()
driver.implicitly_wait(30)

checkbox = driver.find_element_by_xpath("(//span[@class='check'])[1]")
checkbox.click()

select_button = driver.find_element_by_xpath("(//a[@id='seatmap_btn_0'])[1]")
select_button.click()


#driver.switch_to_active_element()

boarding_point = driver.find_element_by_xpath("//select[@id='boarding_ptdbl_select']")
select_boarding_point = Select(boarding_point)
select_boarding_point.select_by_value("824423")


drop_point = driver.find_element_by_xpath("//select[@id='drop_ptdbl_select']")
select_drop_point = Select(drop_point)
select_drop_point.select_by_value("824467")

seat = driver.find_element_by_xpath("(//span[@id='seat_0_1_6'])[2]")
ActionChains(driver).move_to_element(seat).click().perform()

select_seat = driver.find_element_by_xpath("(//button[@id='selectSeatsdbl'])[1]")
#driver.execute_script("arguments[0].scrollIntoView();",select_seat)
ActionChains(driver).move_to_element(select_seat).click().perform()


















'''
seat = driver.find_element_by_xpath("(//span[@id='seat_0_1_6'])[2]")
print seat.location["x"]
print seat.location["y"]



ActionChains(driver).move_to_element(seat).click().perform()

ActionChains(driver).




'''