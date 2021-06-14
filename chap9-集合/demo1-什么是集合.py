# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/5/15 下午11:40

"""
集合是python提供的一个内置数据结构
与列表、字典一样都是属于可变序列
集合是没有value的字典，也是用 {} 进行存储数据
"""

"""集合的第一种创建方式，使用{}"""
s = {2, 3, 4, 5, 6, 7, 8, 9}  # 集合中的元素不允许重复
print(s, type(s))

"""
第二种创建方式，使用内置函数 set()
set()函数将 列表、元组、字符串、集合 的元素转成集合， 并且把重复元素去掉，即有去重功能
"""
s1 = set(range(6))
print(s1, type(s1))

s2 = set([1, 1, 2, 3, 4, 5, 6, 6, 8])
print(s2, type(s2))

s3 = set((1, 2, 3, 4, 65, 2))  # 集合中的元素是无序的
print(s3, type(s3))

s4 = set('python')
print(s4, type(s4))

s5 = set({12, 23, 45, 12, 120})
print(s5, type(s5))

# 定义一个空集合
s6 = set()
print(s6, type(s6))

# 定义一个不可变的集合，使用frozenset()方法
num = frozenset([1, 2, 3, 4, 5, 5])
print(num)