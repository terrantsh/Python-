#-*- coding = utf-8 -*-
#@Time      : 2020/4/21 8:32
#@Author    : Shanhe.Tan
#@File      : dict.py
#@Software  : PyCharm

#字典的定义      键值对
info = {"name":"吴彦祖", "age":18}

#字典的访问
print(info["name"])

#访问了不存在的键
#直接访问会报错
# print(info["gender"])   #KeyError: 'gender'

#print(info.get("gender"))   #None

print(info.get("age","m"))      #找到的显示原值
print(info.get("gender","m"))   #没找到的时候可以设置默认值