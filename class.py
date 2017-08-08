#!/usr/bin/env python
# coding=utf-8


class c1(object):
    name = "class"
    # 类的属性

    @property
    def sum(self):
        return self._sum

    @property
    def sum(self):
        return self._sum

    @sum.setter
    def sum(self, n):
        self._sum = n

    @sum.deleter
    def sum(self):
        del self._sum

    def __init__(self, name, num):

        self.__name = name
        self.__num = num
        self._sum = 0
        print("className = ", c1.name)
        # 实例属性

    def print_(self):
        print(self.__name, self.__num)

    def print1_(self):

        print(self.__name)
 

class c2(c1):
    __slots__ = ['one', "jdfi", "__other"]

    def __init__(self, name, num, other):
        super().__init__(name, num)
        self.__other = other


def otherff(self):
    print("new func in runing add")


def DoNothing():
    pass


c1.other_func = otherff
# 函数附加到类
ex = c1("c1", 20)
ex.__name = "c2"
ex.print_ = DoNothing
ex.print_()
ex.print1_ = DoNothing
ex.print1_()
ex.other_func()


ex2 = c2("c2", 40, "fji")
# ex2 define
# print(ex2.name)
print("slots == ", getattr(ex2, '__slots__'))
ex2.ne1 = 3434
print(ex2.ne1)



def otherf(self):
    print("add to ex")


from types import MethodType
ex2.otherf = MethodType(otherf, ex2)
# 函数附加至实例
ex2.otherf()
ex2.new = 3
from enum import Enum
import urllib


theday = Enum('weekday', ('nn', 'fjf', 'jidf'))
print(theday)
var = theday.nn
print(var)


class A(object):
    def __init__(self, data):
        self.data = data


class B(A):
    def __init__(self, data):
        super().__init__(self, data)

    def Print(self):
        print(self.data)


class A(object):
    pass


class Bjfi(A):
    def __new__(cls):
        return object.__new__(cls)

    def __init__(self):
        self.data = "data"
        pass

    def Print(self):
        print(self.data)

