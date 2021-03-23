# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 21:45:42 2021

@author: Administrator
"""
class Person:
    # 初始化方法--在创建新对象的时候,自动执行
    def __init__(self):
        # 实例属性的声明
        self.name='小倩'
        self.sex ='女生'
        self.age=20
    def eat(self):
        print("喜欢吃西瓜")
        
        
P=Person()
P.eat()
# 添加实例属性

print(P.name,P.sex,P.age)

P2=Person()
P2.name='小倩'
P2.sex = '女生'
P2.age=20

P3=Person()
print(P3.name) #输出默认值
P3.name="小明"
print(P3.name)
# 如果有n个对象,被实例化,那么就需要添加很多次的属性

# 改进 __init__传参
class Pepole:
    # 初始化方法--在创建新对象的时候,自动执行
    def __init__(self,name,sex,age):
        # 实例属性的声明
        self.name=name
        self.sex =sex
        self.age=age
    def eat(self,food):
        print(self.name+"喜欢吃"+food)

zp=Pepole('帐篷', '男生', 18)
print(zp.name,zp.age)
zp.eat('香蕉')

lh=Pepole('李辉', '男生', 18)
print(lh.name,lh.age)
lh.eat('苹果')

xh=Pepole('小花', '女生', 18)
print(xh.name,xh.age)
xh.eat('橘子')

# 总结 __init__
# 1.python自带的内置函数具有特殊含义
# 使用双下划线--魔术方法
#2.可以认为是一个初始化方法--主要用来定义实例属性和初始化数据
# 并且是在创建对象时,自动调用
# 3.可以利用传参的机制




