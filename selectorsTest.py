#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import selectors
sel=selectors.DefaultSelector()

def read(fd,mask):
    print(mask)
    print(fd.readline())
    fd.close()

f=open("yd.py","r+")
print(f.readline())
sel.register(f,selectors.EVENT_READ,read)


    
