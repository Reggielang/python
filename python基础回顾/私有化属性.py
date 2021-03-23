# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 08:59:20 2021

@author: REGGIE
"""

#私有化属性
#1.不想让类的外部进行直接调用
#2. 不想让属性的值被随意更改
#3.保护这个属性，不想让派生类继承

#离开了类就是外部
class Person:
    __hobby = '跳舞'
    def __init__(self):
#        加两个下划线将属性私有化
        self.__name='李四'
        self.age=30
#        在类的内部可以访问私有属性
    def __str__(self):
        return '{}的年龄是{},爱好是{}'.format(self.__name,self.age,Person.__hobby)
    def change_val(self):
        Person.__hobby = '唱歌'
    
    
    
class Student(Person):
    def printinto(self):
#        print(self.__name)
        print(self.age)
    pass    
    
    
x=Person()
#通过实例对象在外部访问的
#print(x.__name)
print(x)

#修改私有属性的值
x.change_val()
print(x)


s=Student()
#私有属性不能被继承
#print(s.__name)
s.printinto()


#小结 1.私有化的实例属性 不能在外部直接访问 可以在类的内部随意使用
#2.子类不能继承父类的私有化属性
#3.在属性的名的前面加两个下划线就可以变为私有属性









