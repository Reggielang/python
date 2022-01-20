# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 14:09:20 2021

@author: REGGIE
"""
#插入排序
#时间复杂度 O(n^2)
def insert_sort(li):
    #i表示摸到牌的下标
    for i in range(1,len(li)):
        temp=li[i]
        j=i-1 #指的是手里牌的下标
        while li[j]>temp and j >= 0:
            li[j+1]=li[j]
            j-=1
        li[j+1]=temp
        print(li)
        
li=[3,2,4,1,5,7,8,9,6]
insert_sort(li)


def insert_sort2(li):
    for i in range(1,len(li)):
        temp = li[i]
        j=i-1
        while li[j]>temp and j>=0:
            li[j+1]=li[j]
            j -=1
        li[j+1]=temp
        print(li)
        
        