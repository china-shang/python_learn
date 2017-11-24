#!/usr/bin/env python
# coding=utf-8
import requests
from bs4 import BeautifulSoup
response = requests.get("https://www.baidu.com/")
soup = BeautifulSoup(response.text, "lxml")
print(response.headers)
print(response.content)
