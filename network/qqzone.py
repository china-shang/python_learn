#!/usr/bin/env python
# coding=utf-8


import sys
import requests
import json
import pymysql
import threading
import functools

import loader


with open("test.t","r") as f:
    data=json.loads(f.read())

class Owner(object):

    @classmethod
    def hasAuthority(qq):
        return true

    def __init__(self):
        self.headers=loader.loadHead()


class QQZone(object):


    def __init__(self,qq):
        self.qq=qq

    def getMsg():
        pass

    def getLeaveMessae():
        pass

    def getInfo():
        pass

    def doLike(id):
        pass


class Msg(object):

    def __init__(self):
        pass

class Comment(object):
    
    def __init__(self):
        pass

def test():
    pass


if __name__=="__main__":
    test()


