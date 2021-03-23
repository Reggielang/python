# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 13:54:16 2021

@author: Administrator
"""

#写函数 接收n个数字,求这些参数数字的和
def Sumfunc(*args):
    res=0
    for item in args:
        res+=item
        
    return res

val = Sumfunc(1,2,3,4,5,6,7)
print(val)

val = Sumfunc(4,5,6,7,8,9)
print("val = %d"%val)

#写函数 找出传入列表或元组的奇数位对应的元素,并返回一个新列表
def Find(lis):
    listA = []
    index =1
    for item in lis:
        if index%2!=0:
            listA.append(item)
        index+=1
    return listA

a = Find([1,2,3,4,5,6,7])
print(a)

a1 = Find(tuple(range(10,30)))
print(a1)

#写函数,检查传入字典的每个value的长度,如果大于2,那么仅保留前两个长度的内容
#并将新内容返回给调用者 PS:字典中的value只能是字符串或列表
def check(dic):
    res = {}
    for key,value in dic.items(): #key-value
        if len(value)>=2:
            # 新字典添加数据
            res[key]=value[:2]
        else:
            res[key]=value
    return res


dic = {'name':'奥特曼','爱好':['打球','打游戏','跳舞'],'pro':'中国艺术'}
b = check(dic)
print(b)

            
    
    
    


