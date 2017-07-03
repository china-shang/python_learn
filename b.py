#!/usr/bin/env python
# coding=utf-8
import re
str = 'fiji ijfi owp prfm fsjow fjow'
lis1 = ['ijfi', 'owp']
lis2 = str.split(' ')
res = [len(word) for word in lis2 if not word in lis1]
print(res)
s = 'abcdabcdabab'
p = re.compile(r'(a|b).*ab')
print(p.search(s).group())
import os
os.system("ls -a")
