#!/usr/bin/env python
# coding=utf-8
import requests
from bs4 import BeautifulSoup

what = 'print'
# response=requests.get('http://dict.youdao.com/w/eng/'+what+'/#keyfrom=dict2.index.suggest')
# soup=BeautifulSoup(response.text,'lxml')
# for  i in soup.findAll('div',class_='trans-wrapper',id='phrsListTab'):
# for j in i.findAll('ul'):
# print(j.text)
response = requests.get(
    'http://dict.youdao.com/w/%E4%BA%BA/#keyfrom=dict2.top')
soup = BeautifulSoup(response.text, 'lxml')
for i in soup.findAll('div', id='authDictTrans'):
    for j in i.findAll('span', class_='def wordGroup'):
        print(j.text)
