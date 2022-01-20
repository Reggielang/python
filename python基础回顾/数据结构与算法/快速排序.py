# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 14:29:53 2021

@author: REGGIE
"""

#快速排序 ：快
#问题 ：递归深度  以及最坏情况O(n^2) 
#x修改递归最大深度
#import sys
#sys.setrecursionlimit(100000)
#时间复杂度O(nlogn)
#思路：取一个元素（第一个元素），使元素p归位， 列表被P分成两部分，左边都比P小，右边比P大，然后进行递归

def partition(li,left,right):
    temp = li[left]
    
    while left<right:
        #从右边开始循环找比temp小的数
        while left < right and li[right] >= temp:
            #往左走一步
            right-=1
            #把右边的值写到左边的位置
        li[left]=li[right]
#        print(li,'right')
        while left < right and li[left] <=temp:
            left +=1
            #把左边的值写道右边的位置
        li[right] = li[left]
#        print(li,'left')
    #把temp归位   
    li[left] =temp
    #返回元素变动之后的新下标
    return left

li= [5,7,4,6,3,1,2,9,8]

print(li)

partition(li,0,len(li)-1)

print(li)

def quick_sort(data,left,right):
    if left < right:
        mid = partition(data,left, right)
        quick_sort(data,left, mid -1)
        quick_sort(data,mid+1,right)
        
        
quick_sort(li,0,len(li)-1)
        
print(li)

        
        
