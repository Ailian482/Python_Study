# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2022/4/28 上午10:09

"""
什么函数：
    函数就是执行特定任何以完成特定功能的一段代码

为什么需要函数：
    复用代码
    隐藏实现细节
    提高可维护性
    提高可读性便于调试

函数的创建：
    def 函数名([输入参数]):
        函数体
        [return xxx]
"""


# # 函数的创建
# def calc(a, b):  # a,b称为形式参数，简称形参，参数的位置是在函数的定义处
#     c = a + b
#     return c
#
#
# result = calc(10, 20)  # 10,20称为实际参数，简称实参，实参的位置是在函数调用处
# print(result)  # 30
#
# # 函数的参数传递
# # 1. 位置参数：根据形参对应的位置进行实参传递
# re_position = calc(10, 20)  # 第 1 个实参 10 传给第 1 个形参 a，第 2 个实参 20 传给第 2 个形参 b，即一个萝卜一个坑
#
# # 2. 关键字参数：
# re_keys = calc(b=20, a=10)  # 根据 = 左侧的变量名称去传，= 左侧的变量名称称为 关键字参数，关键字参数名称一定是 形参里面存在的


# 函数调用的参数传递内存分析
def fun(arg1, arg2):
    print("arg1:", arg1)
    print("arg2:", arg2)
    arg1 = 100
    arg2.append(10)
    print("arg1_1:", arg1)
    print("arg2_2:", arg2)


n1 = 11
n2 = [22, 33, 44]
print(n1)
print(n2)
fun(n1, n2)  # 将位置传参， arg1, arg2 是函数定义处的形参，n1,n2 是函数调用处的实参，所以，实参名称可以和形参名称不一致
print("====================")
print(n1)
print(n2)

"""
在函数调用过程中，进行参数的传递
    如果是不可变对象，在函数体的修改不会影响实参的值，arg1的修改 100，不会影响n1的值
    如果是可变对象，在函数体的修改会影响到实参的值，arg2的修改，append(10)，会影响n2的值
"""
