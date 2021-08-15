# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/8/15 下午3:05

"""
filter(func, iterable)
功能：
    过滤数据，把 iterable 中的每一个元素拿到 func 函数中进行处理，
    如果函数返回 True 则保留这个数据，返回 False 则丢弃这个数据
参数：
    func：自定义函数
    iterable：可迭代的数据
返回值：
    保留下来的数据组成的 迭代器
"""

# 案例1：要求保留所有的偶数，丢弃所有的奇数
var_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 普通方法
new_list = []
for i in var_list:
    if i % 2 == 0:
        new_list.append(i)

print(new_list)


# 使用 filter() 进行处理
# 定义一个函数，判断当前数字是否为偶数，偶数返回 True，奇数返回 False
def my_func(num):
    if num % 2 == 0:
        return True
    else:
        return False


# 调用 过滤器 函数进行处理
it = filter(my_func, var_list)
print(it, type(it), list(it))