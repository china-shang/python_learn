#!/usr/bin/env python
# coding=utf-8
import requests
from bs4 import BeautifulSoup
proxies = {
    'http': 'socks5://127.0.0.1:1080',
    'https': 'socks5://127.0.0.1:1080',
}
response = requests.get(
    "https://translate.google.cn/#en/zh-CN/what",
    proxies=proxies,
    timeout=3)
# print(response.text)
soup = BeautifulSoup(response.text, "lxml")
print(soup.text)
