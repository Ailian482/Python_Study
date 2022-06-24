# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/5/30 下午3:43


# class Person(object):
#     def __new__(cls, *args, **kwargs):
#         print("__new__被调用执行了， cls的id值为{0}".format(id(cls)))
#         obj = super().__new__(cls)
#         print('创建对象的id为{0}'.format(id(obj)))
#         return obj
#
#     def __init__(self, name, age):
#         print('__init__被调用了，self的id值为：{0}'.format(id(self)))
#         self.name = name
#         self.age = age
#
#
# print('object这个类对象的id为：{0}'.format(id(object)))
# print('Person这个类的对象id为：{0}'.format(id(Person)))
#
# # 创建Person类的实例对象
# p1 = Person("张三", 20)
# print('p1这个Person类的实例对象的id：{0}'.format(id(p1)))

# st1 = input().lower()
# st2 = input().lower()
# print(st1.count(st2))
# print("1 E不".lower())
#
# a = "133 1333333 891300 0002313"
# num = a.count("13", 1, len(a))
# print(num)

# import random
#
# N = random.randint(1, 1001)  # 输入要生成的1到500的数字的个数
# print(N)
# num_list = []  # 定义一个空列表，用例放随机生成的数字
# for i in range(0, N):  # 循环 N 次
#     random_num = random.randint(1, 501)  # 随机生成 1-500之间的整数
#     # print(random_num)
#     num_list.append(random_num)  # 每生成一个随机的数字就添加到列表中

N = int(input())  # 输入要生成的1到500的数字的个数
# print(N)
num_list = []  # 定义一个空列表，用例放随机生成的数字
for i in range(0, N):  # 循环 N 次
    random_num = int(input())  # 随机生成 1-500之间的整数
    # print(random_num)
    num_list.append(random_num)  # 每生成一个随机的数字就添加到列表中

# 得到所有放着随机数的列表 num_list
# 去重方法一

"""
# 定义一个空列表，用来放不重复的数字
diff_num_list = []
for i in num_list:  # 遍历 num_list
    if i not in diff_num_list:
        diff_num_list.append(i)  # 将不存在于 diff_num_list 列表的数字追加到 diff_num_list
"""

# 去重方法二
diff_num_list = set(num_list)

# 得到不重复的随机数列表 diff_num_list
# 将列表进行升序排序
new_diff_num_list = sorted(diff_num_list)
for j in new_diff_num_list:
    print(j)


