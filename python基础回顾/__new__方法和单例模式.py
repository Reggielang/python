# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 10:07:03 2021

@author: REGGIE
"""

class Animal:
    def __init__(self):
        self.color = '红色'
#        如果不重写 __new___方法， 默认结构如下：
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)

#实例化的过程会自动调用__new__ 去创建实例
tigger = Animal()
#在新式类中， __new__才是真的实例化方法，为类提供外壳制造出实力框架，调用该框架内的构造方法__init__进行丰满操作
#__new__方法就是开辟对象在内存的地址，然后用__init__去构造这个类

#单例模式 -目的是某一个类只有一个实例存在

#创建一个单例对象 --基于__new__去实现的 推荐的方式

class Databaseclass:
    def __new__(cls, *args, **kwargs):
#        cls._instance=cls.__new__(cls) 不能使用自身的new方法，容易造成一个深度递归
#        应该调用父类的new方法
        #如果不存在就创建对象
        if not hasattr(cls,'_instance'):
            cls._instance=super().__new__(cls,*args,**kwargs)
        return cls._instance
    


class DB2(Databaseclass):
    pass

#无论创建多少个对象，都是返回的第一次创建的对象
db1 = Databaseclass()
print(id(db1))
db2 = Databaseclass()
print(id(db2))


db3 = DB2()
print(id(db3))
