# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2022/4/27 下午3:42

# python 参数分两种参数：一种是 形参，一种是 实参


def my_argument(a, b):  # a, b 就是形参
    print(a + b)


my_argument(10, 18)  # 10, 18 就是实参


# python函数的传参方式有四种：位置参数、默认参数、关键字参数
def chuancan(**kwargs):
    print("小明的家{}".format(kwargs))
    print(kwargs)


chuancan(a=12, b=13)