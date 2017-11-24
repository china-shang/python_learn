#!/usr/bin/env python3
# -*- coding: utf-8 -*-
R = 1000
inner = 0
total = 0
for x in range(R):
    for y in range(R):
        total += 1
        if x * x + y * y <= R * R:
            inner += 1
PI = inner * 4 / total
print("Pi = %f" % PI)
