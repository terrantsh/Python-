#-*- coding = utf-8 -*-
#@Time      : 2020/4/15 22:21
#@Author    : Shanhe.Tan
#@File      : if.py
#@Software  : PyCharm

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