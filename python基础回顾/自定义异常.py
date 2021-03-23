# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 15:34:13 2021

@author: REGGIE
"""

class LongException(Exception):
    def __init__(self,leng):
        self.len = leng
        
        
    def __str__(self):
        return '输入的数据长度是'+str(self.len)+'已经超出长度了'
    


def name_test():
    name = input('输入姓名：')
    try:
        if len(name) >= 4:
            raise LongException(len(name))
        else:
            print(name)
    except LongException as res:
        print(res)
    finally:
        print()
        
        
name_test()