#!/usr/bin/env python
# coding=utf-8

import requests
import urllib.request
from bs4  import BeautifulSoup
import  gzip
from io import BytesIO
import pymysql
#con=pymysql.Connect(user='root',host='localhost',database='test',password='123456')
#cur=con.cursor()
response=requests.get('http://top.hongxiu.com/plyb.html',timeout=3)
soup=BeautifulSoup(response.text,'lxml')
#for i in soup.findAll('a'):
    #if(i.get('title')):
        #if '《' in i.get('title'):
            #print(i.get('title'),":",i.get('href'))
for i in range(1,20):
    try:
        response=requests.get('http://quanben.hongxiu.com/qb4_'+str(i)+'.html',timeout=1)
        soup=BeautifulSoup(response.text,"lxml")
        #if (i in soup.findAll('a')):
            #break
        for i in soup.findAll('a'):
            if(i.get('title'.encode('ISO-8859-1').decode('gbk'))):
                if '《' in i.get('title').encode('ISO-8859-1').decode('gbk'):
                    str=i.get('title').encode('ISO-8859-1').decode('gbk')
                    if str.find('《')!=-1 and str.find('》')!=-1:
                        print(str[str.find('《')+1:str.find('》')])
                    print(str[str.find('：')+1:])
                    #print(i.get('title').encode('ISO-8859-1').decode('gbk'),":",i.get('href'))
    except Exception as e:
        print(e)
        break
