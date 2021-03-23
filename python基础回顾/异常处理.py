# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 12:07:18 2021

@author: REGGIE
"""

#except 在捕获错误异常的时，需要根据具体的错误类型来捕获

#一个try可以捕获多个except的异常
#try:
#    #捕获逻辑的代码
#    print(b)
##    li= [1,2,3]
##    print(li[10])
##except NameError as msg:
##    #捕获到错误，才会进行except中的代码
##    print(msg)
##
##except IndexError as msg:
##    print(msg)
#
#
##万能异常捕获 -- 对于不确定错误的情况下使用
#except Exception as result:
#    print(result)
    

def A(s):
    return 10/int(s)

def B(s):
    return A(s)*2

def main():
    try:
        B('0')
    except Exception as res:
        print(res)



#main()
#不需要再每一个地方去捕获异常，在合适的层次去捕获
#异常抛出机制 -- 如果在运算时发生异常，解释器回查找相应的捕获类型
#如果在当前函数为找到异常，回将异常传递给上层调用函数



try:
    print('我没有错误哦')
except Exception as res:
    print(res)
else:
    print('当try里面的代码，没有出现异常时，我才会执行')



try:
    int('ffffff')
except Exception as res:
    print(res)   
finally:
    #不管有没有异常都会执行--多用于释放文件资源，数据库链接资源等
    print('有没有出错我都执行')











