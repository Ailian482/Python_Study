# -*- coding:utf-8 -*-
# 作    者：Ailian
# 开发时间：2022/9/14 14:51

# 打印一个  三行四列 的矩形
"""
****
****
****
"""
for i in range(1, 4):
    for j in range(1, 5):
        print("*", end="")
    print()  # 换行

print("---------------------------")
# 打印三角形
"""
*
**
***
****
"""
for i in range(1, 5):
    for j in range(1, i + 1):
        print("*", end="")
    print()  # 换行

print("---------------------------")
# 打印倒三角
"""
*****
****
***
**
*
"""
for i in range(1, 6):
    for j in range(1, 7 - i):
        print("*", end="")
    print()  # 换行

print("---------------------------")
# 打印梯形
"""
&&&&&*
&&&&***
&&&*****
&&*******
&*********
***********
"""
for i in range(1, 7):
    for j in range(1, 7-i):
        print("&", end="")
    for k in range(1, 2*i):
        print("*", end="")
    print()  # 换行

print("---------------------------")
# 打印等腰三角形
for i in range(1, 7):
    for j in range(1, 7-i):
        print(" ", end="")
    for k in range(1, 2*i):
        print("*", end="")
    print()  # 换行