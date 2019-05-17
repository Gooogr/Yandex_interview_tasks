#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 01:13:40 2019

@author: grigoriy
"""
import sys
n = int(sys.stdin.readline().strip())


def foo(s, l, r, pairs):
    if l == pairs and r == pairs:
        print(s)
    else:
        if l < pairs:
            foo(s + '(', l + 1, r, pairs)
        if r < l:
            foo(s + ')', l, r + 1, pairs)

foo('', 0, 0, n)

