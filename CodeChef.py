import time 
from selenium import webdriver 
from selenium.webdriver import Chrome 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

# start by defining the options 
options = webdriver.ChromeOptions() 
options.headless = True # it's more scalable to work in headless mode 
# normally, selenium waits for all resources to download 
# we don't need it as the page also populated with the running javascript code. 
options.page_load_strategy = 'none' 
# this returns the path web driver downloaded 
chrome_path = ChromeDriverManager().install() 
chrome_service = Service(chrome_path) 
# pass the defined options and service objects to initialize the web driver 
driver = Chrome(options=options, service=chrome_service) 
driver.implicitly_wait(5)

url = "https://www.codechef.com/contests" 
 
driver.get(url) 

# time.sleep(20)
WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, '_table__container_jhph2_249')))
print(driver.page_source)

u_o_contests = driver.find_elements(By.CLASS_NAME, '_table__container_jhph2_249')

o_c = u_o_contests[0]
u_c = u_o_contests[1]

open_contests = []
upcoming_contests = []

o_contests = o_c.find_elements(By.CLASS_NAME, '_data__container_jhph2_382')
u_contests = u_c.find_elements(By.CLASS_NAME, '_data__container_jhph2_382')

for c in o_contests:
    con_details = {}
    con_details['name'] = c.find_element(By.TAG_NAME, 'span').text
    con_details['ends'] = c.find_element(By.CLASS_NAME, '_timer__container_jhph2_402').text
    # print(con_details)
    open_contests.append(con_details)
    
for c in u_contests:
    con_details = {}
    con_details['name'] = c.find_element(By.TAG_NAME, 'span').text
    time = c.find_element(By.CLASS_NAME, '_timer__container_jhph2_402').find_elements(By.TAG_NAME, 'p')
    con_details['starts'] = time[0].text + ' ' + time[1].text
    # print(con_details)
    upcoming_contests.append(con_details)