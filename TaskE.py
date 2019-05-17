#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 01:17:46 2019

@author: grigoriy
"""

import sys

s1 = list(sys.stdin.readline().strip())
s2 = list(sys.stdin.readline().strip())
print(int(s1[::-1] == s2))
