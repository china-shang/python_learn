#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def do():

    for i in range(10):
        if i == 5:
            raise StopIteration
        yield i


def generator():

    iter = do()

    # yield from fo()
    # is equal under
    #try:
       #while True:
           #yield next(iter)
    #except StopIteration as e:
        #print(e)

    while True:
       yield next(iter)
    print("end")


a=generator()
try:
    while True:
        result=next(a)
        print(result)
except StopIteration as e:
    print(e)

class Generator:

    def __init__(self):
        self.count=3

    def __enter__(self):
        print("in enter")
        return "hello world"

    def __exit__(self,exc_type,exc,fg):
        print("in exit")

    def __iter__(self):
        return self

    def __next__(self):
        self.count -= 1
        if(self.count < 0):
            raise StopIteration
        return self.count

print("----------Class--------")
a=Generator()

print("for in start ")


for i in a:
    print(i)

print("for in end ")

print("with as start")
with a as i:
    print(i)

print("with as end")









