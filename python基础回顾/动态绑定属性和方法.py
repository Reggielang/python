# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 16:01:18 2021

@author: REGGIE
"""
import types #添加方法的库


#先定义要添加的方法
def dymicmethod(self):
    print('{}的体重是{}， 在{}读大学'.format(self.name,self.weight,Student.school))


#定义要添加的类方法
@classmethod
def classtest(cls):
    print('这是一个类方法')

@staticmethod
def staticmethodtest():
    print('一个静态方法')

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def __str__(self):
        return '{}今年{}岁了'.format(self.name,self.age)


print('--------绑定的类方法-----------')
#绑定类方法
Student.Testmethod = classtest
Student.Testmethod()

Student.Testmethod2 = staticmethodtest
Student.Testmethod2()

s=Student('张艳华',20)

print(s)
print('------实例打印动态绑定的类方法')
s.Testmethod()

#动态添加属性
s.weight = 80

#动态的绑定实例方法
s.printinfo=types.MethodType(dymicmethod,s)



print(s.weight)
print('-------------另外一个实例对象   张明---- ')



s2 = Student('张明',20)
print(s2)
#print(s2.weight)


print('---------给类对象添加属性------------')
Student.school = '电子科大'
print(s2.school)
    
print('--------执行动态调用添加实例方法-----------')

#调用动态的方法
s.printinfo()













