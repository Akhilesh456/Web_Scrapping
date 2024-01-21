from bs4 import BeautifulSoup
import requests

url = 'https://unstop.com/competitions-challenges?filters=,all,open,all&types=teamsize,payment,oppstatus,eligible'

result = requests.get(url).text
soup = BeautifulSoup(result, "html.parser").text

contest_element = soup.find_element(By.TAG_NAME, 'app-opportunity-listbox')
contests = contest_element.find_elements(By.TAG_NAME, 'a')
