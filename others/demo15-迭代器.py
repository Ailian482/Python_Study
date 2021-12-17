# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/8/7 下午7:38

"""
迭代器是python中最具特色的功能之一，是访问 集合元素 的一种方式
迭代器是一个可以记住访问遍历的位置的对象
从集合的第一个元素开始访问，直到集合中的所有元素被访问完毕
迭代器只能从前往后一个一个的遍历，不能后退
能被next()函数调用，并不断返回下一个值的对象称为迭代器（iterator）
"""

# range(0, 10) 从 0 到 9，返回一个可迭代的对象
# range(10, 3, -1)  从 10 到 4，返回一个可迭代对象
# for i in range(10, 3, -1):
#     print(i)

arr = [1, 2, 3, 4, 5, 6]
for i in arr:
    print(i, end=" ")
print()

"""
iter()
    功能：把可迭代的对象，转为一个迭代器对象
    参数：可迭代的对象 （str, list, tuple, dict, set, range...）
    返回值：迭代器对象
注意：迭代器一定是一个可迭代对象，但是可迭代对象不一定是迭代器
    
"""
# 定义一个列表，是一个可迭代对象
f4 = ['赵四', '刘能', '小沈阳', '宋小宝']

# # 可以使用 for 循环来遍历数据
# for i in f4:
#     print(i)

# 可以把可迭代对象转为迭代器使用
res = iter(f4)
# print(res, type(res))  # <list_iterator object at 0x7fc29abfff70> <class 'list_iterator'>

"""
迭代器的取值方案
    1. 使用 next() 函数，调用一次获取一次，直到数据被取完
    2. 使用 list() 函数，直接取出迭代器中的所有数据或者剩余的所有数据
    3. 使用 for 循环遍历迭代器的数据
不管使用哪种方法去取数据，取出一个少一个，即取走了就不在迭代器里面了，直到里面的数据被取完
"""
# 1. 使用 next() 函数去调用迭代器对象
# r = next(res)  # 每次获取一个迭代器里面的 数据
print(next(res))  # 赵四
print(next(res))  # 刘能
# print(next(res))  # 小沈阳
# print(next(res))  # 宋小宝
# print(next(res))  # StopIteration 超出可迭代的范围

# 2. 使用 list() 函数
# print(list(res))  # ['小沈阳', '宋小宝']
# print(list(res))  # []

# 3. 使用 for 循环
for i in res:
    print(i)  # 小沈阳  宋小宝

# print(next(res))  # StopIteration 超出可迭代的范围

# 检测迭代器和可迭代对象的方法
from collections.abc import Iterator, Iterable

varstr = '123456'
res = iter(varstr)

# type() 函数返回当前数据的类型
# isinstance() 检测一个数据是不是一个指定的数据类型
r1 = isinstance(varstr, Iterable)  # True，可迭代对象
r2 = isinstance(varstr, Iterator)  # False，不是一个迭代器
r12 = isinstance(res, Iterable)  # True，可迭代对象
r22 = isinstance(res, Iterator)  # True，是一个迭代器
print(r1, r2)
print(r12, r22)
