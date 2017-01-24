#!/usr/bin/env python
# coding=utf-8

def fun(n):
    L=[1]
    while(len(L)<=n):
        yield L
        L=[0]+L+[0]
        L=[L[i]+L[i+1] for i in range(len(L)-1)]
a=fun(10)
for i in a:
    print(i)


