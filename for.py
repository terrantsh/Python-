#-*- coding = utf-8 -*-
#@Time      : 2020/4/16 19:32
#@Author    : Shanhe.Tan
#@File      : for.py
#@Software  : PyCharm

'''
for in
'''

'''
for i in range(5):
    print(i)
'''

'''
for i in range(0,10,2):
    print(i)
'''

'''
for i in range(-10,-100,-30):
    print(i)
'''

'''
name = "shanhe"

for x in name:
    print(x,end="\t")
'''

'''
a = ["aa","bb","cc","dd"]
for i in range(len(a)):
    print(i,a[i])
'''

'''
while
'''

'''
i = 0
while i < 5:
    print("%d"%(i+1))
    print("i = %d"%i)
    i += 1
'''

'''
#1-100
i = 1
j = 0
while i < 101:
    k = i + j
    j = k
    i += 1
print(k)

n = 100
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1
print("sum is %d"%sum)
'''


count = 0
while count < 5:
    print(count, "less than 5")
    count += 1
else:
    print(count, "not less than 5")