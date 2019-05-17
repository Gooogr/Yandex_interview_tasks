#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 00:49:19 2019

@author: grigoriy
"""

# =============================================================================
# import sys
# 
# counter = int(sys.stdin.readline().strip())
# 
# unique_list = []
# 
# for i in range(counter):
#     item = int(sys.stdin.readline().strip())
#     if item not in unique_list:
#         unique_list.append(item)
#     else:
#         continue
# 
# for item in unique_list:
#     print(item)
# =============================================================================

import sys

counter = int(sys.stdin.readline().strip())

unique_list = []

test_number = -99999999999999 # с not in list работало слишком долго, поэтому сравниваю с образом
                # Это работает, так как список цифр упорядочен по условию

for i in range(counter):
    item = int(sys.stdin.readline().strip())
    if item != test_number:
        unique_list.append(item)
    test_number = item

for item in unique_list:
    print(item)
