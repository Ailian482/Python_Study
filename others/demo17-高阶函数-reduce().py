# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/8/8 下午3:49

"""
reduce(func, iterable)
功能：
    每次从 iterable 拿出两个元素，放到 func 函数中进行处理，得出一个计算结果，
    然后把这个计算结果和 iterable 中的第三个元素，放入到 func 函数中继续计算，
    得出的结果和 iterable 中的第四个元素，加入到 func 函数中进行计算，以此类推，直到最后的元素都参与了运算
参数：
    func：内置函数或者自定义函数
    iterable：可迭代的数据
返回值：最终运算处理结果
注意：使用 reduce() 函数时，需要导入 from functools import reduce

"""

from functools import reduce

# 实例1：将列表中的元素转换成 数字
# [5, 2, 1, 1] ==> 5211
# 普通方法
varlist = [5, 2, 1, 1]
res = ''
for i in varlist:
    res += str(i)
res = int(res)
print(res, type(res))  # 5211 <class 'int'>

"""
分析：
    5 2 1 1
    5 * 10 + 2 = 52
    52 * 10 + 1 = 521
    521 * 10 + 1 = 5211
"""


# 使用 reduce() 函数实现
# 定义一个函数，对可迭代数据进行运算
def myfunc(x, y):
    return x * 10 + y


varlist = [5, 2, 1, 1]
ret = reduce(myfunc, varlist)
print(ret, type(ret))  # 5211 <class 'int'>

# 优化程序
ret1 = reduce(lambda x, y: x * 10 + y, varlist)
print(ret1, type(ret1))  # 5211 <class 'int'>


# 实例2：把字符串 '456' ==> 456
# 要求不能使用 int 方法进行类型的转换时，如何解决上面的问题
# 1. 定义一个函数，给定一个字符串的数字，返回一个整型的数字
def myfuncs(s):
    vardict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return vardict[s]


# 2. 先使用 map() 函数，把数字字符串，转成整型的数字 列表迭代器
iter1 = map(myfuncs, '456')  # 返回一个迭代器
# print(iter1, list(iter1))  # <map object at 0x7ff37c700f40> [4, 5, 6]

# 3. 把数字列表中的值，使用 lambda 表达式进行二次处理
iter2 = reduce(lambda x, y: x * 10 + y, iter1)
print(iter2, type(iter2))  # 456 <class 'int'>