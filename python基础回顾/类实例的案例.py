# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 22:54:31 2021

@author: Administrator

"""

import time

# 两个角色对站,有名字和血量
# 技能有捅人-10血,砍人-15血,吃药+10血,以及打印状态


class Player:
    def __init__(self,name,blood):
        self.name =name
        self.blood=blood
        
    def tong(self,enemy):
        enemy.blood-=10
        info = '%s 捅了 %s 一刀'%(self.name,enemy.name)
        print(info)
        
    def kanren(self,enemy):
        enemy.blood-=15
        info = '%s 砍了 %s 一刀'%(self.name,enemy.name)
        print(info)
    def chiyao(self):
        self.blood +=10
        info = '%s 恢复了 10血量'%(self.name)
        print(info)
    def __str__(self):
        return '%s 还剩下 %s 血量'%(self.name,self.blood)
        
# 创建两个实例化对象
P1=Player('西门吹雪',100)
P2=Player('叶孤城',100)

while True:
    if P2.blood<=0 or P1.blood<=0:
        # 满足条件退出循环
        break
    P1.tong(P2)
    print(P2)
    print('********************')
    P1.kanren(P2)
    print(P2)
    print('********************')
    P2.tong(P1)
    P2.chiyao()
    print(P2)
    print('********************')
    time.sleep(1) #休眠一秒