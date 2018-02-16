from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:\Users\Friends\PycharmProjects\selenium\drivers\chromedriver.exe")
driver.get("https://www.google.com")
driver.maximize_window()
driver.implicitly_wait(30)

inputbox = driver.find_element_by_name("q")
inputbox.send_keys("Kanchan Jadhav")
inputbox.send_keys(Keys.ENTER)

