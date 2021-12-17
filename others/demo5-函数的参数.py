# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/5/8 上午10:02

# 可变参数
def add(*nums):
    s = 0
    for n in nums:
        s = s + n
    return s


list1 = [1, 2, 3, 4]
print(add(*list1))

