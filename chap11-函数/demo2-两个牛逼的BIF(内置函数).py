# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/6/4 上午9:48

"""
1. filter()：过滤函数
    filter(function or None, iterable)
    有两个参数：第一个参数是函数或者为None，第二个参数是一个可迭代序列
        如果第一个参数是函数，那么就会将第二个参数的可迭代序列作为函数的参数计算出来，返回True的值筛选出来
        如果第一个参数为None，那么就把第二参数结果为True的值筛选出来

2. map()：是映射函数
    有两个参数：第一个参数是函数，第二个参数是一个可迭代序列
        将第二个参数的可迭代序列作为第一个参数——函数的参数进行运算加工，直到可迭代序列的所有元素都加工完，构成一个新的序列

"""

# help(filter)

# 第一个参数为None
f = filter(None, [1, 0, False, True])
print(list(f))  # [1, True]


# 第一个参数为函数
def odd(x):
    return x % 2


temp = range(10)
print(list(filter(odd, temp)))  # [1, 3, 5, 7, 9]

# 使用lambda函数与filter配合使用
f1 = filter(lambda x: x % 2, range(10))
print(list(f1))  # [1, 3, 5, 7, 9]

print(list(map(lambda x: x*2, range(10))))
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]


