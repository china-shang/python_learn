#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class metaClass(type):
    def __new__(cls,name,bases,attrs):
        print("this in metaClass")
        for j,k in attrs.items():
            print(j)

            if(j=="attr"):
                __mapping__={j:k}
        for i in __mapping__:
            attrs.pop(i)
        attrs["__mapping__"]=__mapping__

        return super().__new__(cls,name,bases,attrs)

class testClass(dict,metaclass=metaClass):
    attrs1=0
    attr="hello "
    def __init__(self):
        pass

a=testClass()
if "attr" not in dir(a):
    print("no attr")

if "__mapping__" in dir(a):
    print("has __mapping__")
print(a.__mapping__["attr"])
