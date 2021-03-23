# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 09:33:20 2021

@author: REGGIE
"""
#私有化的方法只能在类的内部调用，不能被继承

class Animal:
    def __eat(self):
        print('吃东西')
    def run(self):
#        调用私有化方法
        self.__eat()
        print('飞快的跑')
        
        
class Bird(Animal):
    pass

b1=Bird()
#b1.eat()
b1.run()
        