#!/usr/bin/env python
# coding=utf-8

import requests
import urllib.request
from bs4 import BeautifulSoup
import gzip
from io import BytesIO
import pymysql

con = pymysql.Connect(
    user='root',
    host='localhost',
    database='test',
    password='123456',
    charset="utf8")

con.autocommit(True)
cur = con.cursor()
response = requests.get('http://top.hongxiu.com/plyb.html', timeout=3)
soup = BeautifulSoup(response.text, 'lxml')
# for i in soup.findAll('a'):
# if(i.get('title')):
# if '《' in i.get('title'):
# print(i.get('title'),":",i.get('href'))
for i in range(1, 30):
    try:
        response = requests.get(
            'http://quanben.hongxiu.com/qb4_' +
            str(i) +
            '.html',
            timeout=1)
        soup = BeautifulSoup(response.text, "lxml")
        # if (i in soup.findAll('a')):
        # break
        for i in soup.findAll('a'):
            if(i.get('title'.encode('ISO-8859-1').decode('gbk'))):
                if '《' in i.get('title').encode('ISO-8859-1').decode('gbk'):
                    str1 = i.get('title').encode('ISO-8859-1').decode('gbk')
                    if str1.find('《') != -1 and str1.find('》') != -1:
                        name = str1[str1.find('《') + 1:str1.find('》')]
                        print(name)

                    des = str1[str1.find('：') + 1:]
                    print(des)
                    cur.execute(
                        "select * from books where `name` = %s", (name,))
                    result = cur.fetchone()
                    if(not result):
                        cur.execute(
                            "insert into books values (%s,%s)", (name, des))
                    else:
                        print(result)
                        print("There are same book:".format(name))
    except Exception as e:
        print(e)
        break
    finally:
        con.commit()
