#!/usr/bin/env python
# coding=utf-8

def fun():
    i=0
    while True:
        yield i
    return None
g=fun()
def log(func):
    def other(*arg,**kw):
        print("do otherthing")
        return func(*arg,**kw)
    return other
#decorator
def func(var):
    print(var)
func=log(func)
func("hhh")
print("\n\n")
def log(text):
    def decorator(func):
        def other(*arg,**kw):
            print(text)
            print("do otherthing")
            return func(*arg,**kw)
        return other
    return decorator
@log("text")
def f():
    print("this fun")
f()
log("jfidf")(f)
f()

