#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 00:21:02 2019

@author: grigoriy
"""

import sys

counter = sys.stdin.readline().strip()

maximum = 0
result = 0
for i in range(int(counter)):
   item = int(sys.stdin.readline().strip())
   if item == 1:
       result += 1
   else:
       if result > maximum:
           maximum = result
       result = 0
print(max(maximum, result))