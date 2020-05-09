#-*- coding = utf-8 -*-
#@Time      : 2020/4/21 8:32
#@Author    : Shanhe.Tan
#@File      : dict.py
#@Software  : PyCharm

'''
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
'''


info = {"name":"吴彦祖", "age":18}
'''
#增
newID = input("请输入新的学号")
info["id"] = newID

print(info["id"])
'''

#删
#[del]  #删除了整个键值对
# print("删除前:%s"%info["name"])
# del info["name"]
# print("删除后:%s"%info["name"])

# print("删除前：%s"%info)
# del info
# print("删除后：%s"%info)

#[clear]    #清空
# print("清空前:%s"%info)
# info.clear()
# print("清空后:%s"%info)

#改

#查  #遍历
#键的查询，值的查询

# info.keys()     #得到所有的键
# info.values()   #得到所有值
# info.items()    #得到所有的项，每个键值对是一个元组

#枚举函数
# enumerate()


#总结
# 列表[]        有序          可变类型
# 元组()        有序          不可变类型
# 字典{}        无序          key不可变，val可变
# 集合{}        无序          可变类型（不重复）