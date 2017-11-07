#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rsa
import OpenSSL

clearText = input("input:")

pub, pri = rsa.newkeys(512)
encryptText = rsa.encrypt(clearText.encode(), pub)

print("加密后")
print(encryptText)

print("解密后")
print(rsa.decrypt(encryptText, pri).decode())

help(OpenSSL.crypto.rsa)



