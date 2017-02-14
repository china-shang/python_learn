#!/usr/bin/env python
# coding = utf-8
import pymysql
con = pymysql.Connect(user = 'root', host = '127.0.0.1', database = 'base1', password = '',
                   )
cur = con.cursor()
cur.execute("select * from table1 ;")
cur.close()
class students(object):
    def __init__(self, id, name, age):
        self.name = name
        self.id = id
        self.age = age
    def insert(self, con):
        sql = "insert into table1 (id, name, age) values(%s, %s, %s)"
        cur = con.cursor()
        cur.execute(sql, (str(self.id), self.name, str(self.age)))
        cur.close()
stu = students(123, "new", 10)
stu.insert(con)
cur = con.cursor()
cur.execute("select * from table1 ;")
r = cur.fetchall()
for i in r:
    print(i)

