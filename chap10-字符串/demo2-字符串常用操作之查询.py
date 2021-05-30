# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/5/16 下午2:44

"""
index()：查找子串substr第一次出现的位置，返回下标索引，没有找到报 ValueError
rindex()：查找子串substr最后一次出现的位置，返回下标索引，没有找到报 ValueError
find()：查找子串substr第一次出现的位置，返回下标索引，没有找到返回 -1
rfind()：查找子串substr最后一次出现的位置，返回下标索引，没有找到返回 -1
"""

a = "hello , python"
print(a.index('o'))
print(a.rindex('o'))
print(a.find('o'))
print(a.rfind('o'))
# print(a.index('i'))  # ValueError: substring not found
# print(a.rindex('i'))  # ValueError: substring not found
print(a.find('i'))  # -1
print(a.rfind('i'))  # -1
