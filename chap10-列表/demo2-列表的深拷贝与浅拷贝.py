# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/8/22 下午3:38

"""
使用copy函数的时候，只能拷贝 列表的第一层元素
"""
var_list = [1, 2, 3]

# 1. 浅拷贝，可以把列表复制一份
new_list = var_list.copy()
print(var_list, id(var_list))  # [1, 2, 3] 140520997205440
print(new_list, id(new_list))  # [1, 2, 3] 140520968230656

# 对新拷贝的列表进行操作，也是独立的
del new_list[1]
print(new_list, id(new_list))  # [1, 3] 140537049192000
print(var_list, id(var_list))  # [1, 2, 3] 140537062438208

var_list = [1, 2, 3, ['a', 'b', 'c']]  # 多维列表

# 使用copy拷贝一个多维列表
new_list = var_list.copy()
print(var_list, id(var_list))  # [1, 2, 3, ['a', 'b', 'c']] 140570199535872
print(new_list, id(new_list))  # [1, 2, 3, ['a', 'b', 'c']] 140570199536960

# 如果是一个被拷贝的列表，对它的多维列表元素进行操作时，会导致原列表中的多维列表也发生了变化
del new_list[3][1]
print(new_list, id(new_list))  # [1, 2, 3, ['a', 'c']] 140516711675328
print(var_list, id(var_list))  # [1, 2, 3, ['a', 'c']] 140601294003904
print(new_list[3], id(new_list[3]))  # ['a', 'c'] 140304526445312
print(var_list[3], id(var_list[3]))  # ['a', 'c'] 140304526445312


# ============================================
# 深拷贝，就是不光拷贝了当前的列表，同时把列表中的多维元素也拷贝了一份
import copy

var_list = [1, 2, 3, ['a', 'b', 'c']]  # 多维列表

# 使用 copy 模块中 深拷贝方法 deepcopy
new_list = copy.deepcopy(var_list)
del new_list[3][1]

print(new_list)  # [1, 2, 3, ['a', 'c']]
print(var_list)  # [1, 2, 3, ['a', 'b', 'c']]

