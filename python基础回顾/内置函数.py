# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 16:10:16 2021

@author: Administrator
"""

# 绝对值函数
print(abs(-10))

# 四舍五入取整
print(round(3.5))
print(round(3.55,1))

# 求幂运算
print(pow(3,3))
# 3**3

#求最大值
print(max([1,2,3,4,5]))
print(max(23,142))

# 求和
print(sum([1,2,3]))

# 执行字符串表达式
a,b,c=3,3,3
print('动态执行的函数={}'.format(eval('a+b+c')))

def test():
    print('我执行了么?')
    
# 可以执行自己定义的函数
eval('test()')

# 十进制转二进制
print(bin(10)) #转二进制

print(hex(23)) #十六进制

# 将元组转列表
tup= (1,2,3)
print(list(tup))

li = [1,2,3]
print(tuple(li))

# 创建字典
dic = dict(name = '小明',age=19)
print(dic)

# bytes转换
print(bytes('我喜欢python',encoding='utf-8'))















