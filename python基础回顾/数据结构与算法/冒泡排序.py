# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 11:58:43 2021

@author: REGGIE
"""
import random

#时间复杂度 O(n^2)

def bubble_sort(li):
    #第i趟
    for i in range(len(li)-1):
        exchange = False
        for j in range(len(li)-i-1):
            if li[j] > li[j+1]:
                li[j], li[j+1]= li[j+1], li[j]
                exchange =True
        print(li)
        if not exchange:
            return

li = [6,4,8,9,0,1,2,3]





def bubble_sort2(li):
    for  i in range(len(li)-1):
        for j in range(len(li)-i-1):
            if li[j]>li[j+1]:
                li[j],li[j+1]=li[j+1],li[j]


bubble_sort2(li)
print(li)