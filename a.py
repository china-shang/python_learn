#!/usr/bin/env python
# coding=utf-8
var=[1,2,3,4,5,6]
#for i in var:
    #print(i)
#i=[i**j for i in var for j in var]
#print(i)
#mat = [ [1, 2, 3], [4, 5, 6], [7, 8, 9], ]
#knights = {'gallahad': 'the pure', 'robin': 'the brave'}
#for k, v in knights.items():
    #print(k, v)
#knights.items()
import urllib.request
#for line in urllib.request.urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl'):
    #line = line.decode('utf-8')  # 将二进制文件解码成普通字符
    #if 'EST' in line or 'EDT' in line:  # 查找西方国家的时间
        #print(line)
import re
p=re.compile(".*")
a= urllib.request.urlopen('http://dict.youdao.com/w/%E7%BF%BB%E8%AF%91/#keyfrom=dict2.top').read().decode('utf-8')
print(a)
p.search(a)
if a:
    print( re.findall(r"[a-z\s;\.]*:</span>",a)[0][1:-8])


#header=urllib.request.ProxyHandler({'http':'127.0.0.1:8087'})
#opener=urllib.request.build_opener(header)
#urllib.request.install_opener(opener)
#req=urllib.request.Request('http://www.google.com')
#req.add_header=('Referer','http://www.baidu.com')
#line=urllib.request.urlopen('http://www.google.com').read()
#line=urllib.request.urlopen(req).read()
#line=opener.open('http://www.google.com')
#print (line.read())


#在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
