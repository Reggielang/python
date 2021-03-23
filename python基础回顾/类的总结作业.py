# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 16:56:31 2021

@author: REGGIE
"""

class Person:
    def __init__(self,n,a):
        self.__name = n
        self.__age = a
        
        
    def __str__(self):
        return '{}的年龄是{}'.format(self.__name,self.__age)
    
    
    def getname(self):
        return self.__name
    
    def getage(self):
        return self.__age
    
    
    def setage(self, age):
        if age>0 and age<120:
            self.__age=age
        else:
            print('输入数字不合法')
    
    def setname(self, name):
        self.__name=name


class Student:
    def __init__(self):
        self.__name = '张三'
        self.__age = 20
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,name):
        self.__name=name
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self,age):
        self.__age=age
        
        
    def __str__(self):
        return ''
    
    ##将实例对象以函数的形式调用
    def __call__(self,*args,**kwargs):
        print('{}的年龄是{}'.format(self.__name,self.__age))
        

s= Student()
#将实例对象以函数的形式调用
s()
s.name = '李四'
s.age = 60
s()


    

    
import types

class Animal:
    pass


cat = Animal()

#动态绑定方法

def run(self):
    print('猫飞快的跑')

cat.run = types.MethodType(run,cat)
cat.run()

#绑定类属性
Animal.color = '黑色'
print(cat.color)

#动态绑定类方法
@classmethod
def info(cls):
    print('OK')
    
Animal.info = info
Animal.info()













    