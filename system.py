#!/usr/bin/env python
# coding=utf-8
import os
import sys

for i in range(5):
    print("start",i)
    os.system("python ./tcp_client.py")
