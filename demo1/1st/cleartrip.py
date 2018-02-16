from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome("C:\Users\Friends\PycharmProjects\selenium\drivers\chromedriver.exe")
driver.get("https://www.cleartrip.com/")
driver.implicitly_wait(30)
driver.maximize_window()

#FROM
inputbox = driver.find_element_by_xpath("//input[@id='FromTag']")
inputbox.send_keys("Mumbai, IN - Chatrapati Shivaji Airport (BOM)")

#TO
inputbox1 = driver.find_element_by_xpath("//input[@id='ToTag']")
inputbox1.send_keys("Bangalore, IN - Kempegowda International Airport (BLR)")

#DATE
departdate = driver.find_element_by_xpath("//input[@id='DepartDate']")
departdate.send_keys("Thu, 17 Feb, 2018")
departdate.send_keys(Keys.TAB)

adults = driver.find_element_by_xpath("//select[@id='Adults']")
select_adults = Select(adults)
select_adults.select_by_value("2")

children = driver.find_element_by_xpath("//select[@id='Childrens']")
select_children = Select(children)
select_children.select_by_visible_text("2")

infants = driver.find_element_by_xpath("//select[@id='Infants']")
select_infants = Select(infants)
select_infants.select_by_index("1")

searchbutton = driver.find_element_by_xpath("//input[@id='SearchBtn']")
searchbutton.click()

book_button = driver.find_element_by_xpath("(//img[@alt='SpiceJet'])[1]/ancestor::li//button[@class='booking']")
book_button.click()
#(//img[@alt='SpiceJet'])[1]/ancestor::li//button[@class='booking']

checkbox = driver.find_element_by_xpath("//input[@id='insurance_box']")

print driver.execute_script("return arguments[0].checked;", checkbox)

if driver.execute_script("return arguments[0].checked;", checkbox):
    checkbox.click()

add_meal = driver.find_element_by_xpath("//button[@id='MealButton']")
ActionChains(driver).move_to_element(add_meal).click().perform()

select_seat = driver.find_element_by_xpath("//button[contains(text(),'Select Seat')]")
ActionChains(driver).move_to_element(select_seat).click().perform()

#//div[@class='pull-left pax-counter-container']//div[@class='paxCounter'][1]//ul[@class='adult_counter']