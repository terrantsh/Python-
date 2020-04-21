#-*- coding = utf-8 -*-
#@Time      : 2020/4/21 8:08
#@Author    : Shanhe.Tan
#@File      : tuple.py
#@Software  : PyCharm

'''
tup1 = ()       #创建空的元组
print(type(tup1))

#tup2 = (50)    #<class 'int'>
#tup2 = (50,)    #<class 'tuple'>

tup2 = (50,60,70)   #<class 'tuple'>
print(type(tup2))
'''

'''
tup1 = ("abc","def",2000,2020)

print(tup1[0])
print(tup1[-1])     #访问最后一个元素
print(tup1[1:5])    #左闭右开进行切片
'''

#增      连接了两个元组
# tup1 = (12,34,56)
# tup2 = ("abc","xyz")
# tup = tup1 + tup2
# print(tup)

#删      删除了整个，而不是里面的某一个元素
tup1 = (12,34,56)
print(tup1)
del tup1        #删除了整个元组变量
print("删除后：")
print(tup1)

#改  不能改
#tup1 = (12,34,56)
#tup1[0]  = 100      #报错，不允许修改

#查      直接访问