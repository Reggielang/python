# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 17:55:18 2021

@author: Administrator
"""

# 类结构:类名,属性,方法

class Person:
    # 类属性 --在类的内部定义的变量
    # name='小明'
    age=18
    
    # 实例属性--归属于实例所有
    # 1.在方法内部定义的(通过类似于self.变量名)变量
    def __init__(self):
        self.name='小明'

    # 实例方法: 
    # 1.在类的内部 2.使用def关键字 
    # 3.第一参数默认是self(名字可以是其他的,但是这个位置必须被占用)
    # 实例方法是归于类的实例所有
    def eat(self):
        print("大口的吃饭")
    def run(self):
        print("飞快的跑")
        
# 创建类的对象
p=Person()

# 调用类的函数
p.eat()
p.run()

#输出类的属性
print(p.age)

# 创建另一个实例对象,同样也可以使用实例方法
p2 = Person()
p2.eat()
print(p2.name)



