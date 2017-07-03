#!/usr/bin/env python
# coding=utf-8
s = [4, 5]

import socket
rsock, wsock = socket.socketpair()
print(rsock.recv(5))
