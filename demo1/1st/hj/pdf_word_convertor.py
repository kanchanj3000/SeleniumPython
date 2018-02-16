from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import pyautogui

driver = webdriver.Chrome("C:\Users\Friends\PycharmProjects\selenium\drivers\chromedriver.exe")
driver.get("http://pdf2doc.com/")
driver.implicitly_wait(30)
driver.maximize_window()

upload = driver.find_element_by_xpath("(//span[@class='ui-button-text'])[11]")
ActionChains(driver).move_to_element(upload).click().perform()

k = r"C:\Users\Friends\Desktop\tikona_bill.pdf"

time.sleep(1)

#pyautogui.getWindow(title="Open",exact=False).set_foreground()
pyautogui.typewrite(k)
pyautogui.press('enter')
