#!/usr/bin/env python
# coding=utf-8


def fun(n):
    L = [1]
    while(len(L) <= n):
        yield L
        L = [0] + L + [0]
        L = [L[i] + L[i + 1] for i in range(len(L) - 1)]


def fun1(n):
    while n >= 1:
        yield from fun(n)
        n = n - 1


for i in fun1(10):
    print(i)
