# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 22:32:57 2021

@author: Administrator
"""

class Person:
    def __init__(self,name,pro):
        self.name = name
        self.pro = pro
        print('------init-----函数的执行')
    #打印对象,自定义对象 
    def __str__(self):
        return '%s 的专业是 %s'%(self.name,self.pro)
    
    # 创建对象实例的方法--每调用一次,就会生成一个新的对象
    
    # cls就是class的缩写
    # 可以控制创建对象的一些属性限度,经常用来做单例模式
    def __new__(cls,*args,**kwargs):
        print('-----new------函数的执行')
        # 在这里是真正创建对象实例的
        return object.__new__(cls)
xw=Person('小王','计算机')
print(xw)

# __new__和__init__的区别
# __new__函数是类的实例化方法并且必须有return关键字返回该实例,否则对象创建不成功
# 至少有一个参数cls,代表要实例化的类,此参数有实例化时由解释器自动提供
# __new__函数的执行是先于__init__


# __init__用来做数据属性的初始化工作,也可以被认为是实例的构造方法,接收类的实例并对其进行构造
