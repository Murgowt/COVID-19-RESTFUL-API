#Imports
import requests
from bs4 import BeautifulSoup as bs
import re
import pandas as pd

#For String to Integer conversion
def str2int(s):
    return(int(re.sub('[^ 0-9 .]','',s)))
#For World Model
def WorldScraper():
    url='https://www.worldometers.info/coronavirus/'
    req=requests.get(url)
    content=req.content
    soup=bs(content,'html.parser')
    #total  deaths  recovered  active_cases
    cases=soup.find_all('div',{'class':'maincounter-number'})
    total=cases[0].text
    deaths=cases[1].text
    recover=cases[0].text
    active_panel=soup.find_all('div',{'class':'content-inner'})
    for var in active_panel:
        panel=var.find_all('div',{'class':'panel panel-default'})
        for ivar in panel:
            title=ivar.find_all('div',{'class':'panel-heading'})[0].text

            if("Active" in title):
                active=ivar.find_all('div',{'class':'number-table-main'})[0].text
    total=str2int(total)
    deaths=str2int(deaths)
    recover=str2int(recover)
    active=str2int(active)
    print(total,deaths,recover,active)

#For the Countries
def CountryScraper():
    url = 'https://www.worldometers.info/coronavirus/'
    req = requests.get(url)
    content = req.content
    soup = bs(content, 'html.parser')
    table=soup.table
    table_rows=table.find_all('tr')
    rows=[]
    for tr in table_rows:
        td=tr.find_all('td')
        row=[i.text for i in td]
        if(len(row)>1):
            if(row[0]!='' and str2int(row[0])<=215):
                rows.append(row)
    for i in rows:
        print(i)


#For the States
def StateScraper():
    url='https://www.mohfw.gov.in/'
    req=requests.get(url)
    content=req.content
    soup=bs(content,'html.parser')
    table=soup.table
    table_rows=table.find_all('tr')
    rows=[]
    for tr in  table_rows:
        td=tr.find_all('td')
        row=[i.text for i in td]
        if (len(row) > 1):
            if (row[0] != '' and row[0].isdigit() and str2int(row[0]) <= 33):
                rows.append(row)
    for i in rows:
        print(i)
StateScraper()
