#!/usr/bin/env python
# coding=utf-8
class c1(object):
    name="class"
    #类的属性
    @property
    def onlyread(self):
        return "onlyread"
    @property
    def sum(self):
        return self._sum

    @sum.setter
    def sum(self,n):
        self._sum=n

    def __init__(self,name,num):
        self.__name=name
        self.__num=num
        self.__other="other"
        #实例属性

    def print_(self):
        print(self.__name,self.__num)
    def print1_(self):
        print(self.__other)
class c2(c1):
    __slots__=('one','iii')
    def __init__(self,name,num,other):
        self.__name=name
        self.__num=num
        self.__other=other

def other_func(self):
    print("new func in runing add")

c1.other_func=other_func
#函数附加到类
ex=c1("c1",20)
ex.__name="c2"
ex.print_()
ex.print1_()
ex.other_func()
print(hasattr(ex,'__slots__'))
print(ex.onlyread)
ex.sum=-3
ex.sum=45
print(ex.sum)


ex2=c2("c2",40,"fji")
#ex2 define
print(ex2.name)
print (dir(ex2))
print (hasattr(ex,'name'))
print(ex._c1__name)
def otherf(self):
    print("add to ex")

from types import MethodType
ex2.otherf=MethodType(otherf,ex2)
#函数附加至实例
ex2.otherf()
ex2.new=3
from enum import Enum,unique


theday=Enum('weekday',('nn','fjf','jidf'))
print(theday)
var=theday.nn
print(var)



















