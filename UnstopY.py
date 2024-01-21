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
while True:
    driver.get(url)
    try:
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, product_id)))
        break
    except TimeoutException:
        driver.quit()

SCROLL_PAUSE_TIME = 5
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
    
    contest_details['link'] = contest.get_attribute('href')
    
    temp = contest.find_elements(By.CLASS_NAME, 'ng-star-inserted')
    if(len(temp) == 0):
        contest_details['time_left'] = contest.find_element(By.CLASS_NAME, 'launch-tag ng-star-inserted').text
    else:   
        contest_details['time_left'] = temp[0].find_element(By.XPATH, '//*[@id="s_menu"]/div[1]/main/app-explore/section/div/div[2]/app-opportunity-listbox/a[1]/div[2]/div[2]/div[1]/div[2]/strong').text
    
    temp = contest.find_elements(By.CLASS_NAME, 'inr ng-star-inserted')
    mon = contest.find_elements(By.CLASS_NAME, 'tags')[0].text
    try:
        money = mon.split('\n')[1]
    except:
        money = 'NIL'
    contest_details['prize_money'] = money
    
    # temp_url = contest_details['link']
    # driver.get(temp_url)
    # location = driver.find_element(By.CLASS_NAME, 'location ng-tns-c150-2 ng-star-inserted').text
    # print(location)
    # driver.close()
    print(contest_details)
    
    unstop_contest.append(contest_details)