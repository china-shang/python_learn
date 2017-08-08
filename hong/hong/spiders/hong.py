#!/usr/bin/env python
# coding=utf-8

import scrapy
from scrapy.selector import Selector
from bs4 import BeautifulSoup
import ../items


class book_spider(scrapy.Spider):
    name = "hong"

    def start_requests(self):
        cookie = {
            'Hm_lvt_3594cda47af1cb8ae0c461a6a0afc9cc': '1497494996',
            'Hm_lpvt_3594cda47af1cb8ae0c461a6a0afc9cc': '1497524488',
            '21rednet': 'UserID=50014710&UserName=dfxfsdfsdf&OpenKey=0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000&IDTable=00&LoginHash=6AF4FB40F71CF50EA13A34FC3517F437&md5ps=99754106633f94d350db34d548d6091a&LoginDate=20170615070236&IsVipLogin=&JSUserName=dfxfsdfsdf&UserIP=59.54.57.229&glok=true&zz=dfxfsdfsdf&id=50014710&passuser=; ASP.NET_SessionId=jfih4q3cbyaks1454n4k2iqx',
        }
        header = {
            'Referer': ' http://sns.hongxiu.com/',
            'Host': ' sns.hongxiu.com',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'DNT': '1',
            'Cookie': ' Hm_lvt_3594cda47af1cb8ae0c461a6a0afc9cc=1497494996; Hm_lpvt_3594cda47af1cb8ae0c461a6a0afc9cc=1497524488; 21rednet=UserID=50014710&UserName=dfxfsdfsdf&OpenKey=0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000&IDTable=00&LoginHash=6AF4FB40F71CF50EA13A34FC3517F437&md5ps=99754106633f94d350db34d548d6091a&LoginDate=20170615070236&IsVipLogin=&JSUserName=dfxfsdfsdf&UserIP=59.54.57.229&glok=true&zz=dfxfsdfsdf&id=50014710&passuser=; ASP.NET_SessionId=jfih4q3cbyaks1454n4k2iqx',
            'Connection': 'keep-alive',
            'If-Modified-Since': ' Tue, 02 Jul 2013 09:31:54 GMT',
            'If-None-Match': ' "06117fd677ce1:102d"',
            'Cache-Control': ' max-age=0',
        }
        yield scrapy.Request("http://sns.hongxiu.com/", headers=header, cookies=cookie)

    def parse(self, response):
        soup = BeautifulSoup(response.text, "lxml")
        print(soup)
        sel = Selector(response)
        for i in sel.xpath('//span/text()').extract():
            print(i)
