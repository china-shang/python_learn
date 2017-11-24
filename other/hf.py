#!/usr/bin/env python
# coding = utf-8
import os

print(os.getcwd())
os.chdir("/home/zh/Download/")
print(os.getcwd())

a = ['fj', 'woi', 'cao', 'wpn']
a[2:4] = ['fjifij']
a[1] = "jfi"
a.remove('fj')

os.chdir("/")
print(os.path.abspath('.'))
print(os.getgid())
import subprocess
print(subprocess.call('ls'))
