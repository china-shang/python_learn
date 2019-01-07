#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class TestClass(object):
    def __new__(cls,*arg,**args):
        print("in TestClass","in __new__")
        for i in arg:
            print(i)
        return super().__new__(cls)

    def __init__(self,test):
        print(type(self).__name__,"in __init")
        #print(test)

class MyMetaClass(type):
    def __new__(cls,name,bases,attr):
        print("in MyMetaClass __new__")
        for i,j in attr.items():
            print(i,j)
        return type.__new__(cls,name,bases,attr)

class TestClass1(TestClass,metaclass=MyMetaClass):
    attr="myattr"
    def __new__(cls,*arg,**args):
        print(cls.__name__,"in __new__")
        return super().__new__(cls,arg,args)

    def __init__(self,test):
        print(type(self).__name__,"in __init")
        self.name=test
        #super().__init__(self,test)

    def __getattr__(self,attr):
        print("in __getattr__")

def log(meg):
    def decorator(func):
        def run(*arg,**args):
            print(meg)
            return func(*arg,**args)
            # func(arg,args)代表调用
            #而func(*arg，**args)代表任意参数的函数定义
        return run
    return decorator


@log("message")
def doSomething():
    print("doSomething")

def test():
    #testObject=TestClass("sjdfij")
    testObject=TestClass1("sjdfij")
    testObject.sjdifj
    testObject.attr="jdfisdj"
    print("testObject.attr=",testObject.attr)
    print("name=",testObject.name)
    doSomething()
if(__name__=="__main__"):
    test()

