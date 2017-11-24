#!/usr/bin/env python
# coding=utf-8
# [0-9a-zA-Z\_]可以匹配一个数字、字母或者下划线；

# [0-9a-zA-Z\_]+可以匹配至少由一个数字、字母或者下划线组成的字符串，比如'a100'，'0_Z'，'Py3000'等等；

# [a-zA-Z\_][0-9a-zA-Z\_]*可以匹配由字母或下划线开头，后接任意个由一个数字、字母或者下划线组成的字符串，也就是Python合法的变量；

# [a-zA-Z\_][0-9a-zA-Z\_]{0, 19}更精确地限制了变量的长度是1-20个字符（前面1个字符+后面最多19个字符）。

# A|B可以匹配A或B，所以(P|p)ython可以匹配'Python'或者'python'。

# ^表示行的开头，^\d表示必须以数字开头。

# $表示行的结束，\d$表示必须以数字结束。

# 你可能注意到了，py也可以匹配'python'，但是加上^py$就变成了整行匹配，就只能匹配'py'了。

import re

str1 = '32 \\-23  32 '
print(str1)
str1 = r'32 \\-23  32 '
if re.match(r'\\\\3', '\\3'):
    print("yes")
else:
    print("no")
print(' fj i   ijf'.split(' '))
print(re.split(r'\d+', '32fj3j3j34'))
#//用于拆分的字符被删除
# 第一个与最后一个拆分字符会用‘ ‘替换
print("////////")
var1 = re.match(r'(\d+)\-(\d+)', '3434-1211')
print(var1.group(2), var1.groups())
# group(0)return  原字符group(i)return which group ,groups return all by list
var2 = re.match(r'(\d+)(\d*)', '3333')
print(var2.group(1))
var2 = re.match(r'(\d+?)(\d*)', '3333')
print(var2.group(1))
#//默认贪婪
var2 = re.match(r'(\d+)(33)', '33334')
print(var2.group(1))
# 贪婪也不会吧3全匹配，后面也是不定个数才会全部匹配
var2 = re.match(r'(\d+?)(33)', '33334')
print(var2.group(1))
# 加？后尽可能匹配更少
recom = re.compile(r'aaa')
recom.match('fjijf')
# 不需要第一个参数,编译后
print("123".replace('1', '2'))
