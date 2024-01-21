import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://www.codechef.com/contests'

PATH = "C:/SeleniumDrivers/chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get(url)
WebDriverWait(driver, 15).until(EC.title_contains('Competitive Programming and Coding Challenges | CodeChef'))
print(driver.title)