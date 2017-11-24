# !/usr/bin/env python
# coding = utf-8
import sys
sys.path.append("/home/zh/python/tutorial")

import scrapy
from scrapy.selector import Selector
from tutorial.items import TutorialItem

print(sys.path)

class book_spider(scrapy.Spider):
    name = "book"
    url_start = "http://fin.qidian.com/?size=-1&sign=-1&tag=-1&chanId=-1&subCateId=-1&orderId=&update=-1&page=1&month=-1&style=2&vip=-1"
    # url_mid = "quanben"
    # 全本
    url_mid = "qb4_"
    url_end = ".html"
    page_num = 0
    count = 0

    def start_requests(self):
        url = [" ", "  ", " ", " "]
        for i in range(1, 30):
            url[0] = "http://fin.qidian.com/?size=-1&sign=-1&tag=-1&chanId=-1&subCateId=-1&orderId=&update=-1&page=" + \
                str(i) + "&month=-1&style=2&vip=-1"
            url[1] = "http://fin.qidian.com/?size=-1&sign=-1&tag=-1&chanId=21&subCateId=-1&orderId=&update=-1&page=" + \
                str(i) + "&month=-1&style=2&vip=-1"
            url[2] = "http://fin.qidian.com/?size=-1&sign=-1&tag=-1&chanId=2&subCateId=-1&orderId=&update=-1&page=" + \
                str(i) + "&month=-1&style=2&vip=-1"
            url[3] = "http://fin.qidian.com/?size=-1&sign=-1&tag=-1&chanId=22&subCateId=-1&orderId=&update=-1&page=" + \
                str(i) + "&month=-1&style=2&vip=-1"
            for i in url:
                yield scrapy.Request(i)

    def parse_book(self, response):
        item = TutorialItem()
        item['book_href'] = response.meta['ref']
        item['name'] = response.meta['name']
        item['author'] = response.meta['author']
        item['book_type'] = response.meta['type']
        item1 = response.meta['item']

        sel = Selector(response)
        item['descr'] = ''
        dd = ""
        for des_temp in sel.xpath(
                '//div/div/div/div/div[@class = "book-intro"]/p/text()').extract():
            try:
                des = des_temp.split('\u3000')[2]
            except:
                des = des_temp.split('\u3000')[0]
            try:
                des = des.rsplit('\r')[0]
            except:
                print(des_temp)

            item['descr'] = item['descr'] + des
        yield item

    def parse(self, response):
        sel = Selector(response)
        item = TutorialItem()
        # print(sel.xpath('//a/text()').extract())
        for page_section in sel.xpath('//tbody/tr'):
            books_section = page_section.xpath('.//a/text()').extract()
            book_type = books_section[0] + "" + books_section[1]
            book_name = books_section[2]
            book_ref = "http://" + \
                page_section.xpath('.//a/@href').extract()[2][2:]
            book_author = books_section[-1]
            self.count = self.count + 1
            yield scrapy.Request(book_ref, callback=self.parse_book,
                                 meta={'name': book_name, 'author': book_author, 'type': book_type,
                                       'ref': book_ref, 'item': item})

            # print(
                #"\n",
                # self.count,
                #"作者：",
                # book_author,
                #"\n类型：",
                # book_type,
                #"\n书名：",
                # book_name,
                #"\n链接:",
                # book_ref)
