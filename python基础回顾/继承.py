# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 15:33:28 2021

@author: Administrator
"""

class Animal:
    
    def eat(self):
        print('吃东西')
        
    def drink(self):
        print('喝水')
        
        
#继承了Animal 父类， Dog为子类 
class Dog(Animal):
    def wwj(self):
        print('小狗汪汪叫')
    
class Cat(Animal):
    def mmj(self):
        print('小猫喵喵叫')
        
d=Dog()
# 继承了父类的方法
d.eat()

c=Cat()
c.drink()

# 多继承
class Shen:
    def fly(self):
        print('神仙都会飞')
        
class Monkey:
    def chitao(self):
        print('猴子喜欢吃桃')

#继承了两个父类 
class Wukong(Shen,Monkey):
    pass
    
sw = Wukong()
sw.chitao()
sw.fly()

#当多个父类当中存在同名方法时：
class D():
    def eat(self):
        print('D.eat')
        
        
class C(D):
    def eat(self):
        print('C.eat')
        
class B(D):
    pass

class A(B,C):
    pass

# 在执行eat方法 --顺序是1.首先是从A类，然后是B类，然后是C类。C类存在方法调用该方法。
# A-B-C-D 顺序也是继承的顺序
a =A()
a.eat()


# 可以显示类的依次继承关系
print(A.__mro__)


# 间接继承
class GrandFather:
    def eat(self):
        print('吃的方法')
        
class Father(GrandFather):
    def eat(self):
        print('爸爸经常是海鲜')

class Son(Father):
    pass

s = Son()
# 此方法从GrandFather继承

s.eat()
print(Son.__mro__)















