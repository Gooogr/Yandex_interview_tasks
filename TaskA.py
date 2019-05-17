#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 17 17:23:19 2019

@author: grigoriy
"""
# -*- coding: utf-8 -*-
import sys

 
j = sys.stdin.readline().strip()
s = sys.stdin.readline().strip()

result = 0
for symbol in s:
  if symbol in j:
    result+=1
print(result)


