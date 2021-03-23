# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 22:12:42 2021

@author: Administrator
"""

# 1.self和对象指向通一个地址,可以认为self就是对象的引用
class Person:
    def __init__(self,pro):
        self.pro=pro #实例属性的定义
        
    # 实例方法
    def eat(self,name,food):
        # print('self=%s',id(self))
        print('%s 喜欢吃 %s 修的专业是%s'%(name,food,self.pro))
        
        
        
xw=Person('计算机')
# print('xw=%s',id(xw))
xw.eat('小王','榴莲')

# 小结 self
# self只有在类中定义 实例方法的时候才有意义,在调用的时候不需要传入相应参数
# 是由解释器自动去指向
# 名称可以不叫self
# self指的是类实例对象本身