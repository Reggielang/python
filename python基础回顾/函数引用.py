# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 14:51:53 2021

@author: Administrator
"""

a=1 #不可变类型

def func(x):
    print('x的地址:{}'.format(id(x)))
    x=2
    
    print('x修改之后的地址:{}'.format(id(x)))
    print(x)


print('a的地址:{}'.format(id(a)))    
func(a)

print(a)

#可变类型--地址不会改变的
li = []
def test(parms):
    li.append([1,23,3,4])
    print(id(parms))
    print("内部的变量对象:{}".format(parms))

print(id(li))

test(li)
print("外部的变量对象:{}".format(li))

#对于python来讲,在python当中,所有的东西都是对象.
# 在函数调用时,实参传递的就是对象的引用.

#可以更好的把控在函数内部的处理是否会影响函数外部数据变化
#参数传递是通过对象的引用来完成