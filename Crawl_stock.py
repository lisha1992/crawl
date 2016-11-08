# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 09:39:04 2016

@author: ceciliaLee

Change 'startDate', 'endDate', location and name of CSV
"""


import requests
from bs4 import BeautifulSoup
#import urllib,urllib2
#import numpy as np
#import re
import datetime
from datetime import datetime
import csv

def get_page(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }
    html_doc=requests.get(url, headers=headers).content
    return html_doc
    

def get_soup(html_doc):
    soup = BeautifulSoup(html_doc)
 #   print(soup.prettify())
    return soup    

      
def get_all_data(soup):
    all_data=[]
    open_price=[]
    high_price=[]
    low_price=[]
    close_price=[]
    volume=[]
    date_list=[]
    for date in soup.findAll("td", { "class":"lm" }):
        date_list.append(date.get_text().encode('utf-8').strip('\n'))
  #  price=np.zeros(shape=(len(all_data)/5,5))
    for td in soup.findAll("td", { "class":"rgt" }):
        all_data.append(td.get_text().encode('utf-8').strip('\n'))
    #return all_data
    for i in range((len(all_data)/5)):
       # for j in range(5):            
        open_price.append(all_data[5*i])
        high_price.append(all_data[5*i+1])
        low_price.append(all_data[5*i+2])
        close_price.append(all_data[5*i+3])
        volume.append(all_data[5*i+4])

    return date_list, open_price, high_price, low_price, close_price, volume
    
startDate='2014-07-12'
endDate='2016-07-12'
inter_days=(datetime.strptime(endDate, '%Y-%m-%d')-datetime.strptime(startDate, '%Y-%m-%d')).days
iter_times=inter_days/200
urls=['https://www.google.com.hk/finance/historical?cid=7521596&startdate='+startDate+'&enddate='+endDate+'&num=200&gl=cn&ei=gGWEV7mIBYej0ATms7XYAQ&start={}'.format(str(i)) for i in range(0,inter_days, 200)]
#get_all_data(get_soup(get_page(url)))     
#url='https://www.google.com.hk/finance/historical?q=SHA%3A000001&gl=cn&start=0&num=30&ei=CmqDV5KMFsGR0AT2mK7YAQ'
#urls=['https://www.google.com.hk/finance/historical?cid=7521596&startdate=2014-07-12&enddate=2016-07-12&num=200&gl=cn&ei=gGWEV7mIBYej0ATms7XYAQ&start=0']
date_list, open_price, high_price, low_price, close_price, volume=[], [], [], [], [], []
for url in urls:
    date,openP,highP,lowP,closeP,vol=get_all_data(get_soup(get_page(url)))
    date_list.extend(date)
    open_price.extend(openP)
    high_price.extend(highP)
    close_price.extend(closeP)  
    low_price.extend(lowP)
    volume.extend(vol)
    

#print date_list
#print open_price
#print high_price
#print low_price
#print close_price
#print volume 


write_data=[]
for i in range(len(date_list)):
    temp=[]
    temp.append(date_list[i])
    temp.append(open_price[i])
    temp.append(high_price[i])
    temp.append(low_price[i])
    temp.append(close_price[i])
    temp.append(volume[i])
    write_data.append(temp)

with open( '/Users/ceciliaLee/Desktop/stock.csv', 'wb') as f:
    writer=csv.writer(f)
    writer.writerow(['date', 'open_price', 'high_price','low_price','close_price','volume',])
    writer.writerows(write_data)
f.close()




        