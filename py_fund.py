# !/usr/bin/env python
# coding=utf-8

a = b = []
a.append(4)
print(b)
a = 1
b = 1
print(a is b, a is 1)
a = '11'
b = '11'
a.replace('1', '2')
print(a is b, a is '11')
a = int(3)
b = int(3)

print(a is b, a is 3)
a = ()
b = ()
print(a is b, a is ())
# /不可变对象赋值时相等，这为同一对象
a = b = []
a.append(2)
print(a is b)
a = [3]
print(a is b)
# 重新赋值后,变量与之前完全无关
a = [1]
print((3,))
print(type(b'ff'))
print(type('ff'.encode('utf-8')))
print(b'fjfj' == 'fjfj'.encode())
# //b'str' 与'str'.encode() 与'str'.encode('utf-8')一致
dict = {'fj': 34, 3: 35}
dict['fj']
set = frozenset([34, 423, 234])
dict[set] = 43
print(dict.get(3), dict[set])
print(len.__doc__)


def fun(arg1, *, num=3, name, age=3, **kw):
    print(arg1, name, age)
    pass


fun(23, name="mi")
dict[(3, 3)] = 5
# from . import fun
# from .. import module1
# from .. import module2
# . 代表上次from 位置，..代表.的上级位置
for x in range(1, 10):
    print(repr(x * x).ljust(3), repr(x * x * x).rjust(4))
# output control
print("we are {1},you are {0}".format("knight", "NI"))
print("{this},{that}".format(this="this", that="that"))
dict = {"aaa": 1234, "bbb": 2222}
# print('{0[aaa]:d]},{0[bbb]:d}'.format(dict))
print('{aaa},{bbb}'.format(**dict))
import math
print("pi = %5.10f" % math.pi)


class Myclass(object):
    def __init__(self):
        pass


def changeinfun(var):
    var.append(34)


l = []
changeinfun(l)
print(l)
a = 2


def chang(var):
    var = 3


chang(a)
print(a)


def chang(var):
    var['fji'] = 34


dict = {}
chang(dict)
print(dict)
