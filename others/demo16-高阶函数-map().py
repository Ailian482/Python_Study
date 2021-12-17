# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/8/8 下午3:49

"""
对传入的可迭代数据中的每个元素进行处理，返回一个新的迭代器
map(func, *iterables)
功能：
    对传入的可迭代数据中的每个元素进行处理，返回一个新的迭代器
参数：
    func：自定义函数或者内置函数
    iterable：可迭代数据
返回值：迭代器

"""

# 案例1：把一个字符串数字的列表转为 整型的数字列表
# 普通的处理方法
varlist = ['1', '2', '3', '4']  # ==> [1, 2, 3, 4]
newlist = []
for i in varlist:
    # print(i, type(i))
    newlist.append(int(i))
print(newlist)  # [1, 2, 3, 4]


# 使用 map() 函数
varlist = ['1', '2', '3', '4']
res = map(int, varlist)  # <map object at 0x7fbad1bfff70>
print(list(res))  # [1, 2, 3, 4]


# 案例2：[1, 2, 3, 4] ==> [1, 4, 9, 16]
def myfunc(x):
    return x ** 2


varlist = [1, 2, 3, 4]
ret = map(myfunc, varlist)
print(list(ret))  # [1, 4, 9, 16]

# 优化程序
ret1 = map(lambda x: x ** 2, varlist)
print(list(ret1))  # [1, 4, 9, 16]
