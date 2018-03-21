#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import scrapy

class TestSpider(scrapy.Spider):
    name="test1"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]


    def parse(self,response):
        print(response)


