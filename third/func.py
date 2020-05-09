#-*- coding = utf-8 -*-
#@Time      : 2020/4/28 8:24
#@Author    : Shanhe.Tan
#@File      : func.py
#@Software  : PyCharm

'''
#函数的定义
def printinfo():
    print("---------------------")
    print("    Hello World      ")
    print("---------------------")

#函数的调用

printinfo()
'''

'''
#带参数的函数
def add2Num(a, b):
    c = a + b
    print(c)

add2Num(11, 22)
'''

'''
#带返回值的参数
def add2Num(a, b):
    return a + b    #通过return来返回运算结果

result = add2Num(11, 22)
print(result)
print(add2Num(11, 22))
'''
'''
#返回多个值的函数

def divid(a, b):
    shang = a/b
    yushu = a%b
    return shang, yushu #多个值得返回方式

sh,yu  = divid(5, 2)    #需要使用多个值来保存返回内容
print("shang: %d, yushu: %d"%(sh,yu))

'''

'''
#打印一条线
def OneLine():
    print("-------------------")

def MultiLines(n):
    i = 0
    while i < n:
        OneLine()
        i += 1

MultiLines(5)
'''

#求3个数的和
def sum3Number(a,b,c):
    return a + b + c
#完成3个数的平均值
def average3Number(a,b,c):
    sumResult = sum3Number(10,20,30)
    averResult = sumResult/3.0
    return averResult

result = average3Number(10,20,30)
print(result)














