# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 13:43:52 2021

@author: Administrator
"""

def fun1():
    print('--------fun1 start-----------')
    
    print('--------fun1 end-----------')




    
def fun2():
    print('--------fun2 start-----------')
    # 调用第一个函数
    fun1()
    print('--------fun2 end-----------')
    

fun2()
#函数的分类:根据函数的返回值喝函数的参数
#有参数无返回值
#有参数有返回值
#无参数有返回值
#无参数无返回值