# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 16:35:45 2021

@author: Administrator
"""

# all() 函数
# 用于判断给定的可迭代参数中的所有元素都为true,就是不包含0,空,false
# 注意空列表空元组返回的是true
li = [1,2,3,None]
li2 = [1,2,0]
print(all(li))
print(all(li2))

# any()函数
# 用于判断给定的可迭代参数中的所有元素都为false,如果存在一个true就是返回true
a= [1,2,3,0]
print(any(a))

# sorted() 函数
# 用于所有可迭代参数进行排序操作,返回一个列表
# sort是list上的方法
li = [21,1,67,10]
li.sort() #list的排序方法 --直接修改的原始对象
print(li)

# sorted是返回一个新的对象,不是在原来的对象上进行排序
#升序排列
li3=[21,1,67,10]
#降序排列
val = sorted(li3,reverse = True)
print(val)

tup = (21,1,67,10)
varT = sorted(tup)
print(varT)

# zip()
# 用于将可迭代参数将对象对应的元素打包成一个个元组,然后返回这些元组组成的列表
# 会把序列中的对应的索引位置存储为一个元组
# 如果各个迭代器的元素不一致,则按照最少的对象进行压缩,利用*可将元组压缩成列表.
s1 = ['a','b','c']
s2 = ['你','我','它']
s3 = ['你','我','它','谁']
print(zip(s1))
print(list(zip(s1)))

ziplist = zip(s1,s3)
print(list(ziplist))

def printbookinfo():
    # 图书信息
    books=[]
    # 图书编号
    id = input('请输入编号:每个项以空格分割')
    bookname = input('请输入书名:每个项以空格分割')
    bookPos = input('请输入位置:每个项以空格分割')
    idlist=id.split(' ')
    bookname = bookname.split(' ')
    bookPos = bookPos.split(' ')
    # 打包处理成元组
    bookinfo=zip(idlist,bookname,bookPos)
    # 遍历图书信息转化成进行存储
    for bookitem in bookinfo:
        dictinfo={'编号':bookitem[0],'书名':bookitem[1],'位置':bookitem[2]}
        # 将字典对象假如到列表容器中
        books.append(dictinfo)
    for i in books:
        print(i)

# printbookinfo()

# enumerate()
# 用于将可遍历的数据对象 组合成一个索引序列,同时列出数据和数据索引
# 可以自己确定索引
l = ['a','b','c']

for index,item in enumerate(l,2):
    print(index,item)
    
dic = {}
dic['name'] = '李易峰'
dic['hobby'] = '打球'

for index, item in enumerate(dic):
    print(item)


