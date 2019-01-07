#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Test(object):
    def __init__(self,num):
        if(num%2):
            raise Exception()

l=[]
for i in range(6):
    try:
        l.append(Test(i))
    except Exception as e:
        pass
print(l)




