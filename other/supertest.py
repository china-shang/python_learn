#!/usr/cin/env python
# coding=utf-8
s = [4, 5]

import socket
#rsock, wsock = socket.socketpair()
# print(rsock.recv(5))


class A(object):
    def __init__(self, a):
        print("this A")

    def f(self):
        print("this A's f")

    def seta(self):
        self.a = a


class B(A):
    def __init__(self, a, b):
        print("this B")
        super().__init__(a)
        self.b = b

    def f(self):
        print("this b's f")

    def setb(self):
        self.a = a
        print(self.a, self.b, "this is b")


class C(A):
    def __init__(self, a, c):
        print("this C")
        super().__init__(a)
        self.c = c

    def f(self):
        print("this c's f")

    def setc(self):
        self.a = a
        print(self.a, self.c, "this is c")


class D(B, C):
    def __init__(self, a, b, c, d):
        print("this D")
        #super(B, self).__init__(a, c)
        super(B, self).__init__(a, c)
        super().__init__(a, b)

    def f(self):
        print("this d's f")

    def setd(self):
        self.d = d
        print(self.a, self.b, self.c, self.d)


import pprint
pprint.pprint(D.__mro__)
b = B(1, 2)
b.f()
print('\n\n')

d = D(1, 2, 3, 4)
d.f()
