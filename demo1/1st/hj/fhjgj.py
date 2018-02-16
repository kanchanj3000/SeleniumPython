from selenium import webdriver

driver = webdriver.Chrome("C:\Users\Friends\PycharmProjects\selenium\drivers\chromedriver.exe")
driver.get("http://visjs.org/examples/network/basicUsage.html")
driver.implicitly_wait(30)
driver.maximize_window()

#basic_usage = driver.find_element_by_xpath("(//a[@class='exampleLink'])[1]")
#basic_usage.click()


print driver.execute_script("return network.canvas.body.nodes[4].x")
print driver.execute_script("return network.canvas.body.nodes[4].y")