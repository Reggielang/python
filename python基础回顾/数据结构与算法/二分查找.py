# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 17:37:44 2021

@author: REGGIE
"""

#二分查找的前提必须是有序的序列 时间复杂度 O(logn)
def binary_search(li,target):
    #左右边界
    left = 0
    right = len(li)-1
    #候选区有值
    while left <= right:
        mid = (left+right)//2
        #找到了
        if li[mid] == target:
            return mid
        #目标值在中间值左侧
        elif li[mid]> target:
            right = mid-1
        #目标值在中间值右侧
        elif li[mid] < target:
            left = mid+1
    else:
        return None
    
li=[1,2,3,4,5,6,7]
print(binary_search(li,8))