# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 13:28:01 2021

@author: Administrator
"""

# 函数执行完成会返回一个对象,如果在函数内部有return 就可以返回实际的值
# 否则返回None.
# 类型: 可以返回任意类型 --类型取决于return后面的类型
# 在一个函数体内可以出现多个return值,但是只能返回一个return
# 如果在一个函数体内执行了return, 那么函数就退出.不会执行后面的代码

def Sum(a,b):
    sum=a+b
    return sum#将计算的结果返回

# 函数的返回值返回到调用的地方

print(Sum(10,20)) 
#可以将返回值赋值给对象
rs = Sum(10,20)
print(rs)


def calComputer(num):
    result =0
    i=1
    while i<=num:
        result+=i
        i+=1
        
    return result


val = calComputer(10)
print(val)


# 返回元组类型
def returnTuple():
    # return 1,2,3
    return{"name":"aaa"}


A=returnTuple()
print(A)
