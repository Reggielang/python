# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 16:27:35 2021

@author: REGGIE
"""
#限制要添加的实例属性
#节约内存空间


class Student:
    __slots__ = ('name','age','score')
    def __str__(self):
        return '{}...{}'.format(self.name,self.age)
    pass

s = Student()
s.name = '小王'
s.age = 20
s.score = 99
#所有可用的属性都在这里存储 不足的地方就是占用的内存空间大
#在定义了__slots__变量之后，Student类的实例不能随意创建不在slots变量中定义的属性
#并且实例中将不存在dict
#print(s.__dict__)
print(s)



#在继承关系下__slots__
#子类未声明 __slots__ 那么是不会继承父类的__slots__ 子类可疑随意的添加属性
#子类声明了__slots__ 那么回继承父类的__slots__ 那么子类的__slots__的范围是子类+父类的__slots__
class subStudent(Student):
    __slots__=('gender','pro')
    pass

s2 = subStudent()
s2.gender = '男'
s2.pro = '计算机'
#继承了父类的__slots__
s2.name = 'a'

print(s2.gender,s2.pro,s2.name)