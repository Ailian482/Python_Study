# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/11/24 下午6:00


import random

def create_random_num(n):
    num_str = ""
    num = num_str.join(random.choice("0123456789") for i in range(n))
    return num

# c_n = create_random_num(16)
# print(c_n)


def triangles(max_num):
    n = 1
    num_list = [1]
    yield num_list
    while n < max_num:
        n_list = []
        for i in range(n):
            i_list = n_list.append(i)




