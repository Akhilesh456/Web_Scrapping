from bs4 import BeautifulSoup
import requests

def add(t):
    ti = t.split(':')
    minutes = int(ti[1])
    hours = int(ti[0])
    minutes += 30
    if(minutes >= 60):
        minutes -= 60
        hours += 1
    hours += 2
    if(minutes < 10):
        minutes = '0'+str(minutes)
    new_time = str(hours)+':'+str(minutes)
    return new_time

html = requests.get('https://codeforces.com/contests').text
soup = BeautifulSoup(html, 'lxml')
datatable = soup.find('div', class_='datatable')
template = datatable.find('table')
hackths = template.find_all('tr')[1:]
hackathons = []
for hackt in hackths:   
    hackathon = {}
    tds = hackt.find_all('td')
    hackathon['name'] = tds[0].text.lstrip().rstrip()
    time = tds[2].a.text.lstrip().rstrip().split(' ')
    hackathon['start_time'] = time[0]+' '+add(time[1])
    hackathon['length'] = tds[3].text.lstrip().rstrip()
    if(tds[4].span.span is None):
        hackathon['before_start'] = tds[4].span.text.lstrip().rstrip()
    else:
        hackathon['before_start'] = tds[4].span.span.text.lstrip().rstrip()
    if(tds[5].a != None and tds[5].span.span is not None):
        hackathon['before_registration'] = 'Registration in Open!'
    else:
        if(tds[5].span.span is None):
            hackathon['before_registration'] = tds[5].span.text
        else:
            hackathon['before_registration'] = tds[5].span.span.text.lstrip().rstrip()
    # print(hackathon)
    hackathons.append(hackathon)

print(hackathons)