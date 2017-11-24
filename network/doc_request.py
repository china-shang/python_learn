#!/usr/bin/env python
# coding=utf-8

import requests
import urllib.request
from bs4 import BeautifulSoup
import gzip
from io import BytesIO
import pymysql

# con = pymysql.Connect(
    # user='root',
    # host='localhost',
    # database='test',
    # password='123456',
    # charset="utf8")

# con.autocommit(True)
#cur = con.cursor()

cookie = {
    'pgv_pvi': '5989879808',
    'pgv_si': 's6603044864',
    'pgv_pvid': '8257983848',
    'pgv_info': 'ssid=s378647184',
    'ptisp': 'cm',
    'ptui_loginuin': '850747813',
    'pt2gguin': 'o0850747813',
    'uin': 'o0850747813',
    'skey': '@dyfWmlv57',
    'RK': 'fcGCrSjubi',
    'ptcz': 'cecec2e60fcee2119de7a209aa7ad…817c4e265373772709a629a2968c',
    'rv2': '807C429F912F3B4F13CB109C0C38ABB4009A9B1C1DA5EE0A5D',
    'property20': '5750F4F4DDF4B809C32D8523169B3…7FCF28871B818694411C8942D778',
}
header = {
    'Host': 'h5.qzone.qq.com',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Cookie': 'pgv_pvi=5989879808; pgv_si=s6603044864; pgv_pvid=8257983848; pgv_info=ssid=s378647184; ptisp=cm; ptui_loginuin=850747813; pt2gguin=o0850747813; uin=o0850747813; skey=@dyfWmlv57; RK=fcGCrSjubi; ptcz=cecec2e60fcee2119de7a209aa7ada5eb35d817c4e265373772709a629a2968c; p_uin=o0850747813; p_skey=4eOiZPGMdohVEp0cwghlEnvgP3eSZtkYRIdAY*xc490_; pt4_token=59HwL8vjdtJvBtszQtP11Y7-QTVcD8FHCGyaEYM1pWs_; Loading=Yes; QZ_FE_WEBP_SUPPORT=0; cpu_performance_v8=23; __Q_w_s__QZN_TodoMsgCnt=1; __Q_w_s_hat_seed=1; rv2=80CB11BC789D5540C3579DA3229B0192985153F11B494D3984; property20=BA102A499459757A60E39592B732A1CC4DAD87052774745E2093250545CCC8E33F730D7AEE0CDE60',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'If-None-Match': '"1813370259"',
    'Cache-Control': 'max-age=0',
}
response = requests.get('https://user.qzone.qq.com/850747813/main/', headers=header ,  timeout=3)
soup = BeautifulSoup(response.text, 'lxml')
print(response.text)
print(soup)
# for i in soup.findAll('a'):
# if(i.get('title')):
# if '《' in i.get('title'):
# print(i.get('title'),":",i.get('href'))
# for i in range(1, 30):
    # try:
        # response = requests.get(
            #'http://quanben.hongxiu.com/qb4_' +
            # str(i) +
            #'.html',
            # timeout=1)
        #soup = BeautifulSoup(response.text, "lxml")
        # for i in soup.findAll('a'):
            # if(i.get('title'.encode('ISO-8859-1').decode('gbk'))):
                # if '《' in i.get('title').encode('ISO-8859-1').decode('gbk'):
                    #str1 = i.get('title').encode('ISO-8859-1').decode('gbk')
                    # if str1.find('《') != -1 and str1.find('》') != -1:
                        #name = str1[str1.find('《') + 1:str1.find('》')]
                        # print(name)

                    #des = str1[str1.find('：') + 1:]
                    # print(des)
                    # cur.execute(
                        #"select * from books where `name` = %s", (name,))
                    #result = cur.fetchone()
                    # if(not result):
                        # cur.execute(
                            #"insert into books values (%s,%s)", (name, des))
                    # else:
                        # print(result)
                        #print("There are same book:".format(name))
    # except Exception as e:
        # print(e)
        # break
    # finally:
        # con.commit()
