#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 01:54:40 2019

@author: grigoriy
"""

import sys

int_list = []
t = [0] * 101
n = int(sys.stdin.readline().strip())
for i in range(int(n)):
    s = sys.stdin.readline().strip()
    try:
        num = int(s[:s.find(' ')])
    except ValueError:
        continue
    for index, value in enumerate(s.split(' ')):
        if index == 0:
            continue
        elif index == num + 1:
            break
        try:
            t[int(value)] += 1
        except ValueError:
            pass
    del s

for i in range(101):
    if t[i]:
        print(' '.join([str(i)] * t[i]), end=' ')