# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/5/10 下午1:05

# 两个列表
items = ['Fruits', 'Books', 'Others']
prices = [96, 87, 86]

# 将上面两个列表转变成下面的字典格式
# {'Fruits': 96,'Books': 87, 'Others': 86}

# 怎样才能完成上面的操作呢？
# 可以使用python的内置函数 zip()
    # 用于将可迭代的对象作为参数，将对象中对应的元素打包成一个元组，然后返回由这些元组组成的列表

# 实现
lst = zip(items, prices)
print(list(lst))

dict_1 = {item: price for item, price in zip(items, prices)}
print(dict_1)

# items和prices的元素数量不一致
items = ['Fruits', 'Books', 'Others']
prices = [96, 87, 86, 100, 56]

dict_1 = {item: price for item, price in zip(items, prices)}
print(dict_1)
