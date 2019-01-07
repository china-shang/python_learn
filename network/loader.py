#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import configparser


def loadHead():

    with open("./test.head","r") as f:
        lines=f.readlines()

    headers=dict(zip(
        [i.split(":")[0] for i in lines],
        [i.split(":")[-1][1:-1] for i in lines]
        ))

    return headers

def loadParams():
    with open("./params.ini","r") as f:
        lines=f.readlines()

    params=dict(zip(
        [i.split("=")[0] for i in lines],
        [i.split("=")[-1][:-1] for i in lines]
        ))
    return params

def loadUserInfoParams():
    with open("./userinfoparams.ini","r") as f:
        lines=f.readlines()

    params=dict(zip(
        [i.split("=")[0] for i in lines],
        [i.split("=")[-1][:-1] for i in lines]
        ))
    return params

def getparams(params=None):

    config=configparser.ConfigParser()
    with open("./userinfoparams.ini","r") as f:
        config.read_file(f)
    if(params is None):
        for i in config.sections():
            print(i,dict(config[i]))
        return
    if(config.has_section(params)):
        return dict(config[params])
    else:
        return 

    

def test():
    print("loadHead=",loadHead())
    print("loadParams=",loadParams())
    print("loadUserInfoParams=",loadUserInfoParams())
    print("getparams",getparams())


if(__name__=="__main__"):
    test()
    


