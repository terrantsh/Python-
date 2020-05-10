#-*- coding = utf-8 -*-
#@Time      : 2020/5/10 22:29
#@Author    : Shanhe.Tan
#@File      : file.py
#@Software  : PyCharm

'''
f = open("test.txt", "w")   #打开文件，写模式，文件不存在就新建
f.write("hello world, I'm here")

f.close()   #关闭文件
'''

'''     #Read方法，最开始在头，向后移动
f = open("test.txt", "r")
content = f.read(5)
print(content)
content = f.read(5)
print(content)
f.close()
'''

'''
f = open("test.txt", "r")

content = f.readlines() #一次性读取全部文件为列表

# print(content)

i = 1
for temp in content:
    print("%d:%s"%(i,temp))
    i += 1

f.close()
'''