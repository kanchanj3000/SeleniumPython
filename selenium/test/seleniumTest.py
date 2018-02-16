from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os



driver = webdriver.Chrome("C:\Users\Friends\PycharmProjects\selenium\drivers\chromedriver.exe")
driver.get("http:\\www.google.com")
driver.find_element_by_name("q").send_keys("Kanchan Jadhav")
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
driver.find_element_by_xpath("(//h3/a)[1]").click()
driver.find_element_by_name("email").send_keys("jadhav.kanchan196@gmail.com")
driver.find_element_by_name("pass").send_keys("mayur@143")
driver.find_element_by_id("u_0_2").click()
driver.maximize_window()


