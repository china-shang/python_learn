# -*- coding: utf-8 -*-
# /usr/bin/env python
# coding=utf-8

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
#import pymysql
from scrapy.exceptions import DropItem
import aiohttp


import aiomysql
import asyncio


class TutorialPipeline(object):

    def __init__(self):
        self.loop = asyncio.get_event_loop()
        self.count = 0
        self.loop.run_until_complete(self.create_pool())

    async def create_pool(self):
        self.pool = await aiomysql.create_pool(host="127.0.0.1", user="root",
                                               password="123456", db="test",
                                               charset="utf8", autocommit=True,
                                               loop=self.loop, )

    async def execute(self, query, args=None):
        try:
            async with self.pool.get() as con:
                async with con.cursor() as cur:
                    result = await cur.execute(query, args)
                    return result
        except Exception as e:
            print("Exception:", e)

    def selectName(self, name):
        return self.loop.run_until_complete(self.execute(
            "select * from book where name = %s", (name, )))

    def insertBook(self, args=None):
        asyncio.ensure_future(self.execute(
            "insert into book(name, author, description, href, type) VALUES ( %s, %s, %s, %s, %s);", args))

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        result = self.selectName(item['name'])
        if(result != 0):
            raise DropItem("book has existed\n")
        else:
            self.count = self.count + 1
            #print("数据库中不存在", result, "存入数据库中")
            self.insertBook(
                (item['name'],
                 item['author'],
                 item['descr'],
                 item['book_href'],
                 item['book_type'],
                 ))

    def close_spider(self, spider):
        print("\n本次抓取:", self.count)
        self.loop.stop()
        self.loop.close()


# class TutorialPipeline(object):
    # con = pymysql.Connect(
        # user="root",
        # password='123456',
        # host="127.0.0.1",
        # database="test",
        # charset="utf8")
    # con.autocommit(True)
    #cur = None
    #count = 0

    # def process_item(self, item, spider):
        #self.cur.execute('SELECT * from `book` where `name`=%s;', item['name'])
        #result = self.cur.fetchone()
        # if(result):
            #raise DropItem("book has existed\n")
        # else:
            #self.count = self.count + 1
            # self.cur.execute('INSERT INTO `book` (`name`, `author`, `description`, `href`, `type`) VALUES (%s, %s, %s, %s, %s);',
                            # (item['name'], item['author'], item['descr'], item['book_href'], item['book_type'],))

    # def open_spider(self, spider):
        #self.cur = self.con.cursor()
        #print("start spider******\n\n")

    # def close_spider(self, spider):

        #print("end spider*****\n\n")
        # print(self.count)
        # print("关闭数据库连接中...\n")
        # self.con.close()
        # self.cur.close()
        # print("数据库连接已关闭\n")
