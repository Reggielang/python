# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 16:52:59 2021

@author: Administrator
"""

# 类方法 用@classmethod来修饰 第一个参数是类对象cls
class Person:
    country = '中国'
    @classmethod
    def get_country(cls):
        return cls.country #访问类属性
    # 在类方法中修改类属性的值
    @classmethod
    def change_country(cls,data):
        cls.country=data
    
    # 静态方法 --用@staticmethod修饰，不需要任何参数
    # 注意--一般情况下不需要通过实例对象去访问静态方法
    # 由于静态方法主要存放逻辑性代码，本身和类以及实例对象没有交互
    # 在静态方法中，一般不会涉及到类中的方法和属性的操作
    # 数据资源能够得到有效的利用
    @staticmethod
    def getdata():
        return Person.country
    
print(Person.getdata())
#通过类对象直接调用类方法
print(Person.get_country())

#实例对象访问类方法
s= Person()
print(s.get_country())

# print(s.getdata())

# 在类方法中修改类属性的值
Person.change_country('英国')
print(Person.get_country())

import time
# demo
class timetest():
    def __init__(self,hour,mins,sec):
        self.hour=hour
        self.mins=mins
        self.sec =sec
    @staticmethod
    def showtime():
        return time.strftime('%H:%M:%S',time.localtime())
    pass
# 直接使用类对象调用静态方法
print(timetest.showtime())