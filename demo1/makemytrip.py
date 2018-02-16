from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
driver = webdriver.Chrome("C:\Users\Friends\PycharmProjects\selenium\drivers\chromedriver.exe")
driver.get("https://www.makemytrip.com/")
driver.implicitly_wait(30)
driver.maximize_window()

#Book domestic and international flights

book = driver.find_element_by_xpath("//h1")
print book.text


input_box = driver.find_element_by_xpath("//input[@id='hp-widget__sfrom']")
input_box.clear()
input_box.send_keys("Mumbai (BOM)")

input_box1 = driver.find_element_by_xpath("//input[@id='hp-widget__sTo']")
input_box1.clear()
input_box1.send_keys("New Delhi (DEL)")


import datetime

from datetime import timedelta
k = datetime.datetime.now() + timedelta(days=2)
start_day = str(k.day)


xpath_new = "//*[@class='ui-datepicker-group ui-datepicker-group-first']//a[text()='" + start_day + "']"
date = driver.find_element_by_xpath("//input[@id='hp-widget__depart']")
date.click()
driver.find_element_by_xpath(xpath_new).click()

#(//td[@class='ui-datepicker-week-end  ui-state-range']//a[text()='4'])[1]
#//*[@class='ui-datepicker-group ui-datepicker-group-first']//a[text()='8']

passengers = driver.find_element_by_xpath("//input[@id='hp-widget__paxCounter']")
passengers.click()

adults = driver.find_element_by_xpath("//div[@class='paxCounter']//ul[@class='adult_counter']//li[text()='3']")
adults.click()


Childrens = driver.find_element_by_xpath("//div[@id='flight_children']//li[text()=2]")
Childrens.click()


done = driver.find_element_by_xpath("//*[text()='Done']")
done.click()

classes = driver.find_element_by_xpath("//input[@id='hp-widget__class']")
classes.click()

search = driver.find_element_by_xpath("//button[@id='searchBtn']")
search.click()

book = driver.find_element_by_xpath("(//span[text()='Jet Airways']/ancestor::div[@class='top_first_part clearfix']//a[text()='Book'])[1]")
book.click()

radiobutton = driver.find_element_by_xpath("//*[@class='no_insure']//span[@class='upsell_radio_icon insure_radio_icon']")
radiobutton.click()

insurance_checkbox = driver.find_element_by_xpath("//span[@class='custom-box']")
insurance_checkbox.is_selected()

email_address = driver.find_element_by_xpath("//input[@type='email']")
email_address.send_keys("jadhavkanchi@gmail.com")

aggrement = driver.find_element_by_xpath("//span[@class='checkbox_state_review pull-left active']")
aggrement.click()

login = driver.find_element_by_xpath("(//a[@class='btn btn-lg btn-block btn-secondary'])[1]")
login.click()


