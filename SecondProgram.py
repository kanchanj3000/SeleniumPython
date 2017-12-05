from selenium import webdriver

driver = webdriver.Chrome("C:\Users\Friends\PycharmProjects\selenium\drivers\chromedriver.exe")
driver.get("http:\\www.myntra.com")
driver.quit()