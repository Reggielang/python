# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 16:04:51 2021

@author: Administrator
"""

# 父类的方法不满足子类的需要-那么就可以重写父类
class Dog:
    def __init__(self,name,color):
        self.name=name
        self.color =color
        
    def jiao(self):
        print('汪汪叫')
        
class keji(Dog):
    # 重写父类的构造函数
    def __init__(self,name,color):
        # 如果想要使用父类的构造函数可以这样调用
        Dog.__init__(self, name, color)
        #自动的找到对应的父类 --如果有多个父类，那么会按照顺序依次调用
        # super().__init__(name,color) 
        
        # 也可以扩展自己的属性
        self.height = 90
        self.wight = 80
    
    def jiao(self):
        super().jiao() #调用父类的方法
        print("柯基疯狂的叫")
        
    def __str__(self):
        return '{}的颜色是{}，它的身高是{}，体重是{}'.format(self.name, self.color,self.height,self.wight)
        
a = keji('柯基犬','红色')
a.jiao()
print(a)