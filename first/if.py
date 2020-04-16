#-*- coding = utf-8 -*-
#@Time      : 2020/4/15 22:21
#@Author    : Shanhe.Tan
#@File      : if.py
#@Software  : PyCharm

'''
if True:
    print("True")
else :
    print("False")

if 0:
    print("True")
else:
    print("False")

if 0:
    print("True")
  print("True") # IndentationError: unindent does not match any outer indentation level
else:
  print("False")
'''

'''
score = 77

if score >= 90:
    print("A")
elif score < 90 and score >= 60:
    print("B")
else :
    print("C")
'''

'''
xingbie = 1
danshen = 1

if xingbie == 1 :
    print("Boy")
    if danshen == 1:
        print("introduce to you")
    else:
        print("introduce for me")
else:
    print("girl")
    if danshen == 1:
        print()
    else:
        print()
'''

import random

x = random.randint(0,2)

a = input("0,1,2:")

if a == "0" or a == "1" or a == "2":
    a = int(a)
    if a - x == 0:
        print("equal")
    elif a - x == -1 or a - x == 2:
        print("lose")
    else:
        print("win")
else:
    print("Wrong input")

print("random:%d"%x)
