# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 14:32:25 2021

@author: Administrator
"""
#局部变量--作用域只能在函数的内部
#不同的函数,可以定义相同的局部变量,不存在互相影响
#作用:为了临时的保存数据,需要在函数体内定义来存储

#---------全局变量-----------
pro='计算机不得了'
name='吴老师'
#全局变量--作用域的范围不同 在整个文件当中
#当全局变量和局部变量出现重复的时候,程序会优先使用函数内部定义的变量
#如果在函数的内部要想对全局变量进行修改,必须global关键字进行声明

def printinfo():
    name = 'teacher'
    print(name,pro)

def test():
    name='多帅哦'
    print(name,pro)


def change():
    #局部变量
    # pro ='奥特曼'
    
    #修改全局变量
    global pro 
    pro = '奥特曼'


printinfo()
test()

#修改全局变量
change()
print(pro)




