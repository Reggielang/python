# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 16:18:20 2021

@author: Administrator
"""

# 要想实现多态，必须有两个前提
# 1.多态必须发送在父类和子类之间（必须存在继承关系）
# 2.子类必须重写父类的方法

# 增加程序的灵活性 增加程序的扩展性

# python是鸭子类型，关注的不是对象类型本身，而是它是怎么使用的

class Animal:
    def say_who(self):
        print("我是一个动物")
        
        
class Duck(Animal):
    # 重写父类的方法
    def say_who(self):
        print("我是鸭子")
    pass
        

class Dog(Animal):
    def say_who(self):
        print('我是一条狗')


class Cat(Animal):
    def say_who(self):
        print('我是小猫猫')



    
# duck1 = Duck()
# duck1.say_who()

# dog1 = Dog()
# dog1.say_who()

# cat1 = Cat()
# cat1.say_who()


# 统一调用方法
def commotInvoke(obj):
    obj.say_who()

listobj = [Duck(),Dog(),Cat()]

for i in listobj:
        commotInvoke(i)



