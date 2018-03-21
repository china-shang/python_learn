#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from scapy.all import *
    
test_domain="www.jju.edu.cn"
test_ip="192.168"

a=IP()
a.dst=test_domain
a.show()
send(a)
