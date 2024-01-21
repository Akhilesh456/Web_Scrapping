from bs4 import BeautifulSoup
import requests

url = "https://www.hackerearth.com/challenges/?filters=competitive%2Chackathon"

result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

def add(t):
    segments = t.split(' ')
    month = segments[0][:3]
    date = int(segments[1][0:2])
    year = int(segments[2][0:4])
    time = segments[3]
    ampm = segments[4]
    ti = time.split(':')
    hour = int(ti[0])
    minutes = int(ti[1])
    minutes+=30
    if (hour==12):
        hour=0
    if minutes>=60:
        minutes-=60
        hour+=1
    hour+=5
    if hour>=12:
        if ampm == 'AM':
            hour-=12
            ampm = 'PM'
        if ampm == 'PM':
            hour-=12
            ampm = 'AM'
            date+=1
            if (date>31 and month=='Jan'):
                date=1
                month = 'Feb'
            elif (leap(year)==1 and date>29 and month == 'Feb'):
                date = 1
                month = 'Mar'
            elif (leap(year)==0 and date>28 and month == 'Feb'):
                date = 1
                month = 'Mar'
            elif (date>31 and month=='Mar'):
                date = 1
                month = 'Apr'
            elif (date>30 and month=='Apr'):
                date = 1
                month = 'May'
            elif (date>31 and month=='May'):
                date = 1
                month = 'Jun'
            elif (date>30 and month=='Jun'):
                date = 1
                month = 'Jul'
            elif (date>31 and month=='Jul'):
                date = 1
                month = 'Aug'
            elif (date>31 and month=='Aug'):
                date = 1
                month = 'Sep'
            elif (date>30 and month=='Sep'):
                date = 1
                month = 'Oct'
            elif (date>31 and month=='Oct'):
                date = 1
                month = 'Nov'
            elif (date>30 and month=='Nov'):
                date = 1
                month = 'Dec'
            if (date>31 and month=='Dec'):
                year+=1
                date =1 
                month = 'Jan'
    if hour==0:
        hour=12
    hr = str(hour)
    minu = str(minutes)
    if len(str(hour))==1:
        hr='0'+hr
    if len(minu)==1:
        minu = '0'+minu
    new_time = str(month)+' '+str(date)+', '+str(year)+', '+hr+':'+minu+' '+str(ampm)
    return new_time
def leap(year):
    if year%400!=0 and (year%4!=0 or year%100==0):
        return 0
    else:
        return 1
running = doc.find('div', class_='ongoing challenge-list')
hackths = running.find_all('div', class_='challenge-card-modern')

name_running=[]
url_running=[]
for hack in hackths:
    title=hack.find('span', class_="challenge-list-title challenge-card-wrapper")
    name_running.append(title.string)
    start=hack.find('a', class_="challenge-card-wrapper challenge-card-link")
    url1 = start['href']
    url_running.append(url1)
data_running={name_running[i]: url_running[i] for i in range(len(name_running))}
upcoming = doc.find('div', class_='upcoming challenge-list')
upchack = upcoming.find_all('div', class_="challenge-card-modern")
name_upcoming=[]
starting_time=[]
ending_time=[]
urls=[]
for hack in upchack:
    title=hack.find('span', class_="challenge-list-title challenge-card-wrapper")
    name_upcoming.append(title.string)
    start=hack.find('a', class_="challenge-card-wrapper challenge-card-link")
    url1 = start['href']
    urls.append(url1)
    result1 = requests.get(url1).text
    doc1 = BeautifulSoup(result1, "html.parser")
    timings = doc1.find('div', class_="start-time-block")
    startime = timings.find('div', class_="regular bold desc dark")
    starting_time.append(startime.string)
    temings = doc1.find('div', class_="end-time-block")
    endtime = temings.find('div', class_="regular bold desc dark")
    ending_time.append(endtime.string)

ISTstarting_time=[]
ISTending_time=[]
for i in range(len(starting_time)):
    starting_time[i]=starting_time[i].lstrip().rstrip()
    ending_time[i]=ending_time[i].lstrip().rstrip()
    ISTstarting_time.append(add(starting_time[i]))
    ISTending_time.append(add(ending_time[i]))
data_upcoming={name_upcoming[i]: [ISTstarting_time[i], ISTending_time[i], urls[i]] for i in range(len(name_upcoming))}
print(data_upcoming)
print(data_running)


#dictionary data_running will give you (name of contest, url of that contest)
#name_running will give names of running contest
#url_running will give you url of running contest
#add fucntion is to convert time to IST, remove it to get the time on website
#list named name_upcoming, ISTstarting_time, ISTending_time will give you information accordingly such that ith element corresponding to each list will be referring to ith contest
#list named starting_time, ending_time will give you original starting time and ending time respectively which is not in IST
#data_upcoming dictionary will give you (name of contest, starting time (in IST), ending time (in IST), url of that contest)