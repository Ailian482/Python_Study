# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/5/16 上午12:36

"""两个集合是否相等（元素相同，就相等"""
s = {10, 20, 30, 40}
s1 = {20, 30, 10, 40}
print(s == s1)  # True
print(s != s1)  # False

"""一个集合是否是另一个集合的子集"""
s2 = {10, 20, 30, 40, 50, 60}
s3 = {10, 20, 40, 30}
s4 = {10, 20, 80}
print(s3.issubset(s2))  # True
print(s4.issubset(s2))  # False

"""一个集合是否是另一个集合的超集"""
print(s2.issuperset(s3))  # True
print(s2.issuperset(s4))  # False

"""两个集合是否没有交集"""
print(s3.isdisjoint(s4))  # False
s5 = {100, 200, 300}
print(s3.isdisjoint(s5))  # True
