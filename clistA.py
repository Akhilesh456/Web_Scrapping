from bs4 import BeautifulSoup
import requests
import csv

html_text = requests.get('https://clist.by').text

soup = BeautifulSoup(html_text, 'lxml')

competitions = soup.findAll('div', class_='contest row running bg-success')

dataset = []

for data in competitions:
    contest = {}
    contest['name'] = data.find('div', class_='col-md-7 col-sm-8 event').text.lstrip().rstrip()
    x = data.find('div', class_='col-md-7 col-sm-8 event').find('a', class_='title_search').get('href').lstrip().rstrip()
    contest['link'] = x;

    contest['start_time'] = data.find('div', class_='col-md-5 col-sm-12 start-time').text.lstrip().rstrip()
    contest['duration'] = data.find('div', class_='col-md-3 col-sm-6 duration').text.lstrip().rstrip()
    print(contest)
    dataset.append(contest)
