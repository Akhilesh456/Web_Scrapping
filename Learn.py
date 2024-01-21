from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

PATH = r"C:/SeleniumDrivers/chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get('https://www.techwithtim.net/')
print(driver.title)

search = driver.find_element(By.NAME, 's')
search.send_keys('C++')
search.send_keys(Keys.RETURN)

time.sleep(10)