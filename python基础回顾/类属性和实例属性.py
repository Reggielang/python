# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 16:38:18 2021

@author: Administrator
"""

# 类属性是类对象拥有的属性，他是被所有类对象的实例对象共有
# 实例属性 是实例拥有的属性，是被实例拥有

class Student:
    # 类属性被类所拥有
    name ='黎明'
    # 实例属性
    def __init__(self,age):
        self.age =age
   
#类属性只能通过类对象去修改 
Student.name = '多帅哦'
s=Student(18)

# 通过实例对象访问类属性
print(s.name)
# 通过实例对象无法修改类属性 --只是声明了一个新的实例属性
# s.name = '六的大'
print(s.name)
print(s.age)

# 通过类对象去访问
print(Student.name) #类.属性名 形式访问类属性

# print(Student.age)
# 类属性可以被类对象和实例对象共同访问
# 实例属性只能由实例对象访问

xh = Student(28)
print(xh.name)
print(xh.age)