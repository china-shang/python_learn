#!/usr/bin/env python
# coding=utf-8
import scrapy
from scrapy.selector import Selector
from bs4 import BeautifulSoup


class book_spider(scrapy.Spider):
    name = "qzone"

    def start_requests(self):
        cookie = {
        }
        header = {
        }
        yield scrapy.Request("https://user.qzone.qq.com/850747813/main/", cookies=cookie, headers=header)

    def parse(self, response):
        soup = BeautifulSoup(response.text, "lxml")
        print(soup)
        sel = Selector(response)
        print("****start****")
        for i in sel.xpath('//span/text()').extract():
            print(i)
