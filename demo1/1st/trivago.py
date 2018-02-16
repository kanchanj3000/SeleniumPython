from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:\Users\Friends\PycharmProjects\selenium\drivers\chromedriver.exe")
driver.get("https://www.trivago.in/")
driver.implicitly_wait(20)
driver.maximize_window()

inputbox = driver.find_element_by_xpath("//input[@id='horus-querytext']")
inputbox.send_keys("Pune")
inputbox.send_keys(Keys.ENTER)
