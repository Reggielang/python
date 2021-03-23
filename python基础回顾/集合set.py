# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 17:18:24 2021

@author: Administrator
"""

# 是无序而且不重复的元素集合
# set不支持索引和切片
# 类似与字典,但只有键
# 创建集合
set1 = {1,2,3}
print(set1)

# 添加操作
# set1.add('python')
# print(set1)

# 清空
# set1.clear()
# print(set1)

# 差集 a中存在b不存在
set2 = {2,3,4}

res = set1.difference(set2)

print(res)

# 交集 a和b
res2 = set1.intersection(set2)
print(res2)

#并集操作
res3 = set1.union(set2)
print(res3)



# pop 集合中随机删除一个元素
set2.pop()
print(set2)

# discard 移除指定的元素
set2.discard(4)
print(set2)


# update 更新--会去重
a = {5,6,7}
b= {6,7,8}
a.update(b)

print(a)







