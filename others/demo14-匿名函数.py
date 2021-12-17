# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/8/7 下午7:23

# 匿名函数 lambda 表达式
"""
匿名函数的意思就是说 可以不用使用 def 定义，并且这个函数也没有名字
在python中可以使用 lambda 表达式来定义匿名函数
注意：lambda 表达式仅仅是一个表达式，不是一个代码块，所以 lambda 又成为一行代码的函数
lambda 表达式也有形参，并且不能访问除了自己的形参之外的任何数据包括全局变量
"""

"""
语法：
    lambda [参数列表]:返回值 [分支结构]
    参数列表可以不写
    
特点：
    lambda 是一个表达式，因为不能写太复杂的逻辑，功能相对单一
    lambda 可以写简单的分支结构
"""


# 封装一个函数做加法运算
# 普通函数
def jiafa(x, y):
    return x+y


print(jiafa(1, 2))  # 3

# 改成 lambda 表达式来封装
res = lambda x, y: x+y
print(res(2, 3))  # 5

# lambda 写分支结构
res = lambda sex: "很man" if sex == '男' else '很 nice'
print(res('女'))