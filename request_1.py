#!/usr/bin/env python
# coding=utf-8
import requests
from bs4 import BeautifulSoup
response = requests.get("https://jecvay.com/")
soup=BeautifulSoup(response.text,"lxml")
print(soup.title.text)
