# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 15:18:19 2021

@author: Administrator
"""
# 语法
# lambda 参数1,参数2,参数3:表达式
# 没有名字,表达式有且只有一个,匿名函数自带return

#只能是单个表达式,不是一个代码块,只是会了简单的函数
# 仅仅能封装简单的函数复杂逻辑不行

def Sum(a,b):
    return a+b

res = lambda a,b:a+b
res(10, 20)
print(res(10, 20))

a = lambda x,y,z:x*y*z

print(a(12,13,14))

# b if a else c
age=15
print("可以参军" if age>18 else'继续上学')

b = lambda x,y:x if x>y else y
print(b(10,12))

# 直接调用
b = (lambda x,y:x if x>y else y)(10,12)
print(b)

val = lambda x: (x**2)+890

print(val(2))


