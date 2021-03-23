# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 15:36:36 2021

@author: Administrator
"""
# 循环的方式实现阶乘
def func1(n):
    res = 1
    for item in range(1,n+1):
        res *=item
    return res

print(func1(5))

#递归函数--在函数的内部调用自己本身
# 递归满足条件:1.自己调用自己 2.必须有一个明确的结束条件
# 优点:逻辑简单,定义简单
# 缺点:容易导致栈溢出
def func2(n):
    if n==1:
        return 1
    else:
        return n*func2(n-1)

print(func2(5))


#递归案例 --树形结构的遍历 --寻找文件夹中的所有文件
import os

def Findfile(file_path):
    # 得到该路径下所有的文件和文件夹
    listR = os.listdir(file_path)
    for fileitem in listR:
        # 获取完成的文件路径
        full_path = os.path.join(file_path,fileitem)
        # 判断是否是文件夹
        if os.path.isdir(full_path):
            # 如果是一个文件夹,去递归
            Findfile(full_path)
        else:
            # 如果是文件就直接输出文件名
             print(fileitem)
    else:
        return 
    

Findfile('E:\\GIT远程库学习代码')
   
    