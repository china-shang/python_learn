#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Iter(object):

    def __init__(self):
        self._list=[1,2,3,4]

    def __iter__(self):
        for i in self._list:
            yield i



def interrupted_iter(iter:Iter):
    for i in iter:
        if(i==3):
            print("i==3,return")
            return

def new_for_in(iter:Iter):
    for i in iter:
        print("i=",i)

def test():
    iter=Iter()
    interrupted_iter(iter)
    new_for_in(iter)


if __name__=="__main__":
    test()

