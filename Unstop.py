# format

import time
from selenium import webdriver 
from selenium.webdriver import Chrome 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions() 
options.headless = True 
chrome_path = ChromeDriverManager().install() 
chrome_service = Service(chrome_path)
driver = Chrome(options=options, service=chrome_service) 

url = 'https://unstop.com/competitions-challenges?filters=,all,open,all&types=teamsize,payment,oppstatus,eligible'
driver.get(url)
wait = WebDriverWait(driver, 30)
wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'ng-star-inserted')))

SCROLL_PAUSE_TIME = 3
last_height = driver.execute_script("return document.body.scrollHeight")

for i in range(3):
    driver.execute_script(f"window.scrollTo(0, {last_height})")
    time.sleep(SCROLL_PAUSE_TIME)
    last_height = driver.execute_script("return document.body.scrollHeight")
    
contest_element = driver.find_element(By.TAG_NAME, 'app-opportunity-listbox')
contests = contest_element.find_elements(By.TAG_NAME, 'a')

unstop_contest = []

for contest in contests:
    contest_details = {}
    
    n_list = contest.find_element(By.TAG_NAME, 'h2').text.lstrip().rsplit()
    name = ""
    for a in n_list: name += a+' '
    contest_details['name'] = name.rstrip()
    
    c_ele = contest.find_element(By.TAG_NAME, 'h3').text
    contest_details['instutite'] = c_ele
    
    contest_details['link'] = contest.get_attribute('href')
    
    temp = contest.find_element(By.CLASS_NAME, 'registered')
    ttemp = temp.find_elements(By.CLASS_NAME, 'ng-star-inserted')
    if(len(ttemp) != 0):
        contest_details['time_left'] = ttemp[1].text
    else:
        contest_details['time_left'] = 'Launching Soon!'
    
    temp = contest.find_elements(By.CLASS_NAME, 'inr ng-star-inserted')
    mon = contest.find_elements(By.CLASS_NAME, 'tags')[0].text
    print(mon)
    if(len(temp) == 0):
        contest_details['prize_money'] = 'NIL'
    else:
        contest_details['prize_money'] = "Upto Rupees "+temp[0].text
        
    print(contest_details)
    
    unstop_contest.append(contest_details)