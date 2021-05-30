# 对数据类型做检查

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError("bad operand type")
    if x >= 0:
        return x
    else:
        return -x


# 添加参数检查后，如果传入错误的参数类型，函数就会抛出一个错误
# print(my_abs(1))

import math

def quadratic(a, b, c):

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
        raise TypeError("bad operand type")
    deta = b ** 2 - 4 * a * c

    if deta >= 0:
        x1 = (-b + math.sqrt(deta)) / (2 * a)
        x2 = (-b - math.sqrt(deta)) / (2 * a)
        return x1, x2
    else:
        print("test failed!")


print(quadratic(1, 0, 4))