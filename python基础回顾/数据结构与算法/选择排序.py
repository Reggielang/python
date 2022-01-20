# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 12:18:57 2021

@author: REGGIE
"""

#选择排序
#时间复杂度O(n^2)
#这个例子要用创建新的内存来存储新的列表
li = [3,4,1,2,5,6,7,8,9]
def select_sort_simple(li):
    li_new = []
    for i in range(len(li)):
        min_val = min(li)
        li_new.append(min_val)
        li.remove(min_val)
    return li_new

#
#print(select_sort_simple(li))

#li = [3,2,4,1,5,6,7,8,9]
def select_sort(li):
    #i是第几趟
    for i in range(len(li)-1):
        min_loc = i
        for j in range(i+1,len(li)):
            if li[j] <li[min_loc]:
                min_loc = j
        li[i],li[min_loc] = li[min_loc],li[i]
        print(li)

select_sort(li)

li = [3,4,1,2,5,6,7,8,9]
def select_sort2(li):
    for i in range(len(li)-1):
        min_loc=i
        for j in range(i+1,len(li)):
            if li[j]<li[min_loc]:
                min_loc = j
        li[i],li[min_loc]=li[min_loc],li[i]
        
        
        

select_sort2(li)
print(li)