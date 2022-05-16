# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2022/5/16 上午9:28

"""
斐波那契数列
1,1,2,3,5,8...
第三项开始，前面两项之后，例如 第 3 项是 第1、2项之和，第 4 项是 第2、3项之后...
"""


def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        res = fib(n-1) + fib(n-2)
        return res


# 斐波那契数列 第 6 位上的数字
print(fib(6))

# 输出这个数列的前 6 位上的数字
for i in range(1,7):
    print(fib(i))