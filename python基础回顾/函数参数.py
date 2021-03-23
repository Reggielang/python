# 1.必选参数--在调用是必须要给实参
def sum(a,b):#形参：只是一种形式，在定义的时候不占内存地址的
    sum=a+b
    print(sum)
    pass

#函数的调用
sum(10,20) #实际参数，实在的参数，占用了内存地址

#2.默认参数--默认参数，必须要存在参数列表的尾部
def sum(a=20,b=30):
    print("默认参数的使用=%d"%(a+b))
    pass

sum()#调用函数时未赋值，就会使用默认参数的默认值。

#3.可变参数--当参数的个数不确定的时候使用，比较灵活 
# 接收的数据是元组类型
def getComputer(*args):
    '''
    args 可变长的参数类型
    '''
    # print(args)
    result=0
    for item in args:
        result +=item
        pass
    print("result=%d"%result)
    pass


getComputer(1)
getComputer(1,2)
getComputer(1,2,3)

#4.关键字可变参数 
#**来定义 
#在函数体内 参数关键字接收的是字典类型，key是一个字符串
def keyFunc(**kwargs):
    print(kwargs)
    pass

# keyFunc(1,2,3) --不可以的
dictA={"name":"Leo","age":35} 

# 以字典类型直接传
keyFunc(**dictA) 
keyFunc(name='pater',age=20)

#可变参数,关键字可变参数一起使用,会自动识别填充传入的参数
# 可变参数,必须放到关键字可选参数之前!
def complexFunc(*args,**kwargs):
    print(args)
    print(kwargs)
    pass

complexFunc()
#
complexFunc(1,2,3,4,name="Kodi",age=10)
#
complexFunc(name="Kodi",age=10)


# def Test(**kwargs,*args):
#     pass
    











