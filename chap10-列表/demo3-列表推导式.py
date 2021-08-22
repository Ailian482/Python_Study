# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/8/22 下午4:25


"""
列表推导式的结构是由一个 方括号 所包含的一下内容：一个表达式，后面跟着一个 for 句子，然后是 零个或者多个 for 或 if 子句。
其结果是一个新列表，由对表达式依据后面的 for 和 if 子句的内容进行求值计算而得出。
"""
# 1. 基本的列表推导式使用方式
# 变量 = [变量或者变量结果 for 变量 in 容器类型数据]
# '1234' --> [2, 4, 6, 8]
# 普通方法
var = '1234'
new_list = []
for i in var:
    new_list.append(int(i) * 2)

print(new_list)  # [2, 4, 6, 8]

# 使用列表推导式
new_list = [int(i) * 2 for i in var]
print(new_list)  # [2, 4, 6, 8]

# 使用列表推导式+位运算
new_list = [int(i) << 1 for i in var]
print(new_list)  # [2, 4, 6, 8]

# 2. 带有判断条件的推导式
# 变量 = [变量或变量的处理结果 for 变量 in 容器类型数据 条件表达式]
# 0-9 求所有的偶数，==> []
new_list = []
for i in range(10):
    if i % 2 == 0:
        new_list.append(i)
print(new_list) # [0, 2, 4, 6, 8]

# 列表推导式
new_list = [i for i in range(10) if i % 2 == 0]
print(new_list)  # [0, 2, 4, 6, 8]

# 3. 带有条件判断的多循环的推导式
# [1, 2, 3], [3, 1, 4] ==> 把列表中的元素两两组合，要求组合的元素不能重复
# 常规方法
new_list = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            new_list.append((x, y))
print(new_list)  # [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

# 列表推导式
new_list = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(new_list)  # [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

# 4. 对于嵌套循环的列表推导式
"""
把下面这个 3x4 的矩阵，它由3个长度为4的列表组成，交换其行列
[
 [1, 2, 3, 4],
 [5, 6, 7, 8],
 [9, 10, 11, 12]
]
"""
arr = [
 [1, 2, 3, 4],
 [5, 6, 7, 8],
 [9, 10, 11, 12]
]

# 常规方法
new_list = []
for i in range(4):
    res_list = []
    for row in arr:
        res_list.append(row[i])
    new_list.append(res_list)
    print(res_list)
print(new_list)  # [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

# 列表推导式
new_list = [[row[i] for row in arr] for i in range(4)]
print(new_list)  # [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

