#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def createClass(className,fields):
    header="\n\n\npublic class {0}{{".format(className.title())
    text=""

    print(header)
    text += header

    for field in fields:
        init="""
            String {0}=null;
           """.format(field)

        print(init)
        text += init

    for field in fields:
        get="""
            public String get{0}{{
                return this.{1};
            }}

        """.format(field.title(),field)
        print(get)
        text += get

    for field in fields:
        set="""
            public void set{0}(String {1}){{
                this.{1}={1}
            }}

        """.format(field.title(),field)
        print(set)
        text += set

    with open(className.title()+".class","w") as f:
        f.write(text)

if __name__=="__main__":
    createClass(sys.argv[1],sys.argv[2:])
