# -*- coding:utf-8 -*-
# 作    者：Ailian
# 开发时间：2022/9/13 17:25

"""
eval()函数
    - eval(s)函数去掉字符串s最外层的引号，并按照Python语句方式执行去掉引号后的字符串
    - 语法格式
        变量 = eval(字符串)
    - eval()函数经常跟input()函数一起使用，用来获取用户输入的数值型

不能用于字符串是非数字
"""

s = "3.14+3"
print(s, type(s))
x = eval(s)
print(x, type(x))

age = eval(input("请输入您的年龄："))  # 将字符串类型转换成了int类型，相当于 int(age)
print(age, type(age))
"""
结果：
    请输入您的年龄：18
    18 <class 'int'>
"""

height = eval(input("请输入您的身高："))  # 将字符串类型转换成了float类型，相当于 float(height)
print(height, type(height))
"""
结果：
    请输入您的身高：188.9
    188.9 <class 'float'>
"""

# 使用 eval() 报错的情况
# h = eval("hello") # 去掉引号后，hello变成一个标识符了
# print(eval("hello"))  # NameError: name 'hello' is not defined. Did you mean: 'help'?

hello = "北京欢迎你"
print(hello)  # 北京欢迎你
l = eval("hello")
print(l)  # 北京欢迎你
