# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 15:15:32 2021

@author: Administrator
"""

class Student:
    def run(self):
        print("可以跑步")
        
s = Student()
s.run()

class sgClass:
    def __init__(self,name,color):
        self.color= color
        self.name = name
        
    def __str__(self):
        return '%s 颜色是 %s'%(self.name,self.color)
    
pg = sgClass('苹果', '红色')
print(pg)