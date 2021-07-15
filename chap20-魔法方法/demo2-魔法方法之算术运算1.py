# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/6/24 上午9:11


"""

"""
"""
__add__(self, other)：定义加法的行为：+
__sub__(self, other)：定义减法的行为：-
__mul__(self, other)：定义乘法的行为：*
__truediv__(self, other)：定义真除法的行为：/
__floordiv__(self, other)：定义整数除法的行为：//  （地板除）
__mod__(self, other)：定义取模算法的行为：%
__divmod__(self, other)：定义当被 divmod() 调用时的行为
__pow__(self, other)：定义当被 power() 调用或 ** 运算时的行为
__lshift__(self, other)：定义按位左移的行为：<<
__rshift__(self, other)：定义按位右移的行为：>>
__and__(self, other)：定义按位与操作的行为：&
__xor__(self, other)：定义按位异或操作的行为：^
__or__(self, other)：定义按位或操作的行为：|

"""


class New_int(int):
    def __add__(self, other):  # 重写 加法
        return int.__sub__(self, other)  # 返回减法运算

    def __sub__(self, other):  # 重写 减法
        return int.__add__(self, other)  # 返回加法运算


a = New_int(3)
b = New_int(5)
print(a + b)
print(a - b)


# import sys
#
# sys.setrecursionlimit(10000)  # 可以修改递归深度的值，让递归深度变大

class Try_int(int):
    def __add__(self, other):
        return self + other

    def __sub__(self, other):
        return self - other


a = Try_int(3)
b = Try_int(5)
print(a + b)
