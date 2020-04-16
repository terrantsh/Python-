#-*- coding = utf-8 -*-
#@Time      : 2020/4/16 20:49
#@Author    : Shanhe.Tan
#@File      : list.py
#@Software  : PyCharm


# namelist = [] #定义一个空的列表
namelist = ["小张","小王","小李"]
'''
print(namelist[0])
print(namelist[1])
print(namelist[2])
testlist = [1, "test"]
print(testlist[0])
print(testlist[1])
'''

'''
for name in namelist:
    print(name)

length = (len(namelist))
i = 0
while i < length:
    print(namelist[i])
    i += 1
'''


#增:    [append]
'''
print("--------增加前列表的数据----------")
for name in namelist:
    print(name)

nametemp = input("添加学生姓名")
namelist.append(nametemp)   #在末尾增加一个元素

print("--------增加后列表的数据----------")
for name in namelist:
    print(name)
'''


#增：     [extend]
'''
a = [1,2]
b = [4,5]
a.append(b)     #将列表当做一个元素加到a列表中
print(a)

a.extend(b)     #将b列表中的每个元素逐一添加到a列表中
print(a)
'''

#增:     [insert]
'''
a = [0,1,2]
a.insert(1,3)       #第一个元素表示下标，第二个表示元素
print(a)            #指定下标位置插入元素
'''


#删:     [del][pop][remove]
'''
movieName = ["加勒比海盗", "骇客帝国","指环王","闪灵","速度与激情8"]
print("--------增加前列表的数据----------")
for name in movieName:
    print(name)

#del movieName[2]           #指定位置删除
#movieName.pop()            #弹出末尾最后一个元素
movieName.remove("指环王") #直接删除指定内容的元素，找到的第一元素

print("--------增加后列表的数据----------")
for name in movieName:
    print(name)
'''


#改：     []
namelist = ["小张","小王","小李"]
print("--------增加前列表的数据----------")
for name in namelist:
    print(name)

namelist[1] = "小红"      #修改指定下标的元素内容

print("--------增加后列表的数据----------")
for name in namelist:
    print(name)














