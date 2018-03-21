#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pymysql
import pylab 
import numpy as np
import time
import datetime
import matplotlib.dates as mdates
import matplotlib as mpl



zhfont=mpl.font_manager.FontProperties(fname='/usr/share/fonts/opentype/noto/NotoSansCJK-Medium.ttc')


class DataHander():

    def connectMysql(self):
        self.con=pymysql.Connect(user="root",
                       password="123456",
                       database="qqzone",
                       charset="utf8",
                       host="localhost")
        self.con.autocommit(True)
        self.cur=self.con.cursor()

    def __init__(self):
        self.connectMysql()
        self._message_time_list=[]
        pass

    def fetchAllMessage(self):

        self.cur.execute("SELECT `create_time` FROM `message` ")


        for data in self.cur.fetchall():
            self._message_time_list.append(datetime.datetime.fromtimestamp(data[0]))

    def drawByHour(self,year=None):

        
        x = [datetime.datetime.now() + datetime.timedelta(hours=i) for i in range(24)]
        y=[]
        hour_list=[t.hour for t in self._message_time_list if year is None or t.year==year]

        for t in x:
            y.append(hour_list.count(t.hour)/len(hour_list)*100)

        pylab.plot(x,y)
        
        myFmt = mdates.DateFormatter('%H:%M')
        pylab.gca().xaxis.set_major_formatter(myFmt)

        pylab.xlabel("发表时间",FontProperties=zhfont)
        pylab.ylabel("所占百分比",FontProperties=zhfont)

        if(year is None):
            pylab.title("每小时发表说说比例",FontProperties=zhfont)
        else:
            pylab.title(str(year)+"年"+"每小时发表说说比例",FontProperties=zhfont)




        pylab.show()

    def drawByMon(self,year=None):

        y=[]
        x=[]

        datetime.datetime(2015,1,1)

        mons=range(1,13)

        for year in range(2015,2018):

            mons_list=[t.month for t in self._message_time_list if year is None or t.year==year]
            for t in mons:
                x.append(datetime.datetime(year,t,1))
                y.append(mons_list.count(t))

        pylab.plot(x,y)
        
        #myFmt = mdates.DateFormatter('%Y:%M')
        #pylab.gca().xaxis.set_major_formatter(myFmt)

        pylab.text(x[1],y[1],"text")
        pylab.xlabel("发表的月份",FontProperties=zhfont)
        pylab.ylabel("所占百分比",FontProperties=zhfont)

        pylab.title("每月发表说说比例",FontProperties=zhfont) 


        pylab.show()








dataHander=DataHander()
dataHander.fetchAllMessage()
#dataHander.drawByHour(2015)
#dataHander.drawByHour(2016)
#dataHander.drawByHour(2017)
dataHander.drawByMon(2017)
#dataHander.drawByMon(2016)
#dataHander.drawByMon(2015)



