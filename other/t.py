#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class T(object):
    def __init__(self):
        self.list=[3,5]

    def __iter__(self):
        for i in self.list:
            yield i

t=T()

s=[]

s+=t

for i in s:
    print(i)
