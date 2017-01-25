#!/usr/bin/env python
# coding=utf-8

a=b=[]
a.append(4)
print(b)
a=1
b=1
print (a is b,a is 1)
a='11'
b='11'
a.replace('1','2')
print (a is b,a is '11')
a=int(3)
b=int(3)

print (a is b,a is 3)
a=()
b=()
print (a is b,a is ())
#//不可变对象赋值时相等，这为同一对象
a=b=[]
a.append(2)
print(a is b)
a=[3]
print(a is b)
#重新赋值后,变量与之前完全无关
a=[1]
print((3,))
print (type(b'ff'))
print (type('ff'.encode('utf-8')))
print(b'fjfj' == 'fjfj'.encode())
#//b'str' 与'str'.encode() 与'str'.encode('utf-8')一致
dict={'fj':34,3:35}
dict['fj']
set=frozenset([34,423,234])
dict[set]=43
print(dict.get(3),dict[set])
print(len.__doc__)
