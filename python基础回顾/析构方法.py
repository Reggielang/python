# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 15:19:45 2021

@author: Administrator
"""

class Animal:
    def __init__(self,name):
        self.name = name
        print("这是构造方法")
    
    def __del__(self):
        # 主要的应用就是来操作对象的释放，一旦释放完毕，对象不存在
        # 回收内存等资源
        print('这是析构方法')
        print('%s 这个对象被清理了，释放了内存'%self.name)
        

dog = Animal('狗')
# 手动去清理对象，会执行析构函数
del dog 
input('程序等待中')