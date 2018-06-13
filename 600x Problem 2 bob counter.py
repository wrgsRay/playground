#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 14:08:53 2017

@author: raymond
"""

s = 'bobobobobobobobobobobobobob'
Num = 0
Cstart = 0
Cend = 3
while Cend <= len(s):
    if s[Cstart:Cend] == "bob":
        Num += 1
        Cstart += 1
        Cend += 1
    else: 
        Cstart += 1
        Cend += 1
print("Number of times bob occurs is: " + str(Num))
