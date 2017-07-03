#!/usr/bin/env python
# coding=utf-8

str = "《东方》 \n\n描述：双方双方"
if str.find('《') != -1 and str.find('》') != -1:
    print(str.find('《'))
    print(str[str.find('《') + 1:str.find('》')])
print(str[str.find('：') + 1:])
