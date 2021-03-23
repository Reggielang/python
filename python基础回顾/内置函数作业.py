# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 17:36:14 2021

@author: Administrator
"""

#求三组连续自然数的和: 求出1到10,20到30,35到45的三个和
def sumRange(m,n):
    return sum(range(m,n+1))

print(sumRange(1, 10))
print(sumRange(20, 30))
print(sumRange(35, 45))

#100个和尚吃100个馒头,大和尚一个人吃3个馒头,小和尚三个人吃一个馒头 大小和尚多少人

def person():
    for a in range(1,100):
        if a*3+(100-a)*(1/3) ==100:
            return (a,100-a)


res = person()
print(res)


#指定一个列表,列表里有一个唯一出现过一次的数据.输出这个数字

lis = [1,1,2,2,3,3,4,4,5]
set1= set(lis)

# lis中保留重复的元素
for i in set1:
    lis.remove(i)


# set1中数字和lis中重复的元素进行对照 --输出lis中没有的元素
for i in set1:
    if i not in lis:
        print(i)
    

