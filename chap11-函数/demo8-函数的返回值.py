# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2022/4/28 上午11:01

print(bool(0))  # False
print(bool(8))  # 非 0 的布尔值为 True


def fun(num):
    odd = []  # 存奇数
    even = []  # 存偶数
    for i in num:
        if i % 2:  # 如果 i % 2 为 True，就是 i % 2 不为 0
            odd.append(i)
        else:
            even.append(i)
    return odd, even


# 函数的调用
lst = [10, 29, 34, 23, 44, 53, 55]
print(fun(lst))  # ([29, 23, 53, 55], [10, 34, 44])

"""总结：
函数的返回值
    1. 如果函数没有返回值【函数执行完毕之后，不需要给调用处提供值数据】，return 可以省略不写
    2. 函数的返回值，如果是 1 个，直接返回 原类型
    3. 函数的返回值，如果是多个，返回的结果为 元组
    
函数在定义时，是否需要返回值，视情况而定
"""


def fun1():
    print("hello")
    # return


fun1()


def fun2():
    return "hello"


print(fun2())


def fun3():
    return "hello", "world"


print(fun3())

