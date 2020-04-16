#-*- coding = utf-8 -*-
#@Time      : 2020/4/16 20:27
#@Author    : Shanhe.Tan
#@File      : char.py
#@Software  : PyCharm

'''
word = '字符串'
sentence = "这是一个句子"
paragraph = """
            这是一个段落
"""

print(word)
print(sentence)
print(paragraph)
'''

'''
# my_str = "I'm a student"
#my_str = 'I'm a student'   #worng
my_str = 'I\'m a student'
print(my_str)
'''


str = "chengdu"
'''
print(str)
print(str[2:4])     #[起始位置:结束位置:步进值]
print(str[1:7:2])
'''
print(str[::2])
print(str[5:])

print(str + ",Hello")   #字符串连接使用+
print(str + ",Hi" *3)   #r取消转义功能