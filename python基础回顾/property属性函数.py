# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 09:44:50 2021

@author: REGGIE
"""

class Person:
    
    def __init__(self):
        self.__age = 18
#        
#    def get_age(self):
#        return self.__age
#    def set_age(self,age):
#        if age<0:
#            print('年龄不能小于0')
#        else:
#            self.__age=age
#            
##    定义一个类属性，通过直接访问属性的形式去访问私有的属性
#    age = property(get_age,set_age)
        
#        实现方式-2 通过装饰器去声明
    @property #用装饰器添加属性标识  #提供getter方法
    def age(self):
        return self.__age
    
    @age.setter #提供setter方法
    def age(self,age):
        if age<0:
            print('年龄不能小于0')
        else:
            self.__age=age
        
        
        
p=Person()
print(p.age)
p.age=20
print(p.age)
#听过方法来获得私有属性，或者修改
#p.get_age()
#p.set_age(19)
