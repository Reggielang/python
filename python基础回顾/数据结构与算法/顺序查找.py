# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 17:25:41 2021

@author: REGGIE
"""

li=[1,2,3]


def line_search(li,target):
    for index, val in enumerate(li):
        if val == target:
            print(index)
            return index
    else:
        return None
    
    
line_search(li,3)

#时间复杂度 O(n)