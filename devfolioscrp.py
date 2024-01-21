from bs4 import BeautifulSoup
import requests
from csv import writer
url='https://devfolio.co/hackathons'
page=requests.get(url)

soup=BeautifulSoup(page.text,"html.parser")

lists=soup.find_all(class_="sc-iuStju bcUeMb sc-eEpejC ktHUdV")
# if we want to store it in csv then we can use this
'''with open ("Scrapped.csv","w",encoding="utf8",newline='') as f:
      thewiter=writer(f)
      header=['Contest Name',"Duration","Date ","Link"]
      thewriter.writerow(header)'''
condel=[]
for list in lists:
      contest_name=list.find(class_="sc-jKDlA-D bfNete").text.replace('\n','')
      mode=list.find_all('div',class_="sc-gJwTLC kvcXze")
      date=list.find_all(class_="sc-jKDlA-D iRGQAO")
      
      link=list.find(class_="sc-hCgVqe dEyqTH")
      if len(mode)==3 and len(date)==2 :
            data=[contest_name,mode[0],mode[1],mode[2],date[1],link]
            condel.append(data)
      elif len(mode)==3 and len(date)==3 :
            data=[contest_name,mode[0],mode[1],mode[2],date[1],link,date[2]]
            condel.append(data)
      elif len(mode)==3 and len(date)==4 :
            data=[contest_name,mode[0],mode[1],mode[2],date[1],link,date[2],date[3]]
            condel.append(data)


m=[]
for lsit in condel:
      dict={}
     
      dict['name']=lsit[0]    
      a=str(lsit[1])
      c=''
      for g in range(59,len(a)):
            if a[g]!="<":
                  c=c+a[g]
                  if a[g+1]=="<":
                        break
      #print(c)
      dict['mode']=c
      b=str(lsit[2])
      c=''
      for g in range(59,len(b)):
            if b[g]!="<":
                  c=c+b[g]
                  if b[g+1]=="<":
                        break
      #print(c)    
      dict['status']=c
      k=str(lsit[3])
      #print(lsit[3],k)
      c=''
      for g in range(59,len(k)):
             if k[g]!="<":
                  #print(k[g],k[g+1],k[g+2])
                  c=c+k[g]
                  #print(c)
                  if k[g+1]=="<":
                        break
      #print(c)
      dict['date']=c
      e=str(lsit[4])
      c=''
      for g in range(29,len(e)):
             if e[g]!="<":
                  c=c+e[g]
                  if e[g+1]=="<":
                        break
      #print(c)
      dict['requirement1']=c
      f=str(lsit[5])
      c=''
      for g in range(33,len(f)):
            if f[g]!='"':
                  c=c+f[g]
                  if f[g+1]=='"':
                        break
      #print(c)
      dict['link']=c
      
      
      if len(lsit)==7:
            q=str(lsit[6])
            c=''
            for g in range(29,len(q)):
                   if q[g]!="<":
                        c=c+q[g]
                        if q[g+1]=="<":
                              break
            #print(c)
            dict['requirement2']=c
            
      elif len(lsit)==8:
            q=str(lsit[6])
            c=''
            for g in range(29,len(q)):
                   if q[g]!="<":
                        c=c+q[g]
                        if q[g+1]=="<":
                              break
            #print(c)
            dict['requirement2']=c
            w=str(lsit[7])
            c=''
            for g in range(29,len(w)):
                   if w[g]!="<":
                        c=c+w[g]
                        if w[g+1]=="<":
                              break
            #print(c)
            dict['requirement3']=c
      m.append(dict)


print("YOUR MASTER LIST CONTANING ALL THE DETAILS",m)

      

