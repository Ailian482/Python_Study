# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/5/16 上午12:51

"""集合的数学操作"""
# ① 输出交集的集合
s1 = {10, 20, 30, 40}
s2 = {20, 30, 40, 50, 60}
print(s1.intersection(s2))
print(s1 & s2)  # intersection() 与 & 等价，交集操作

# ② 输出并集的集合
print(s1.union(s2))
print(s1 | s2)  # union() 与 | 等价，并集操作

# ③ 输出差集的集合
print(s1.difference(s2))  # difference() 与 - 等价，差集操作
print(s1 - s2)  # s1 有而 s2 没有的元素
print(s2 - s1)  # s2 有而 s1 没有的元素

# 思 输出对称差集的集合
print(s1.symmetric_difference(s2))  # s1 有而 s2 没有的元素 加上 s2 有而 s1 没有的元素
print(s1 ^ s2)  # symmetric_difference() 与 ^ 等价，对称差集操作
