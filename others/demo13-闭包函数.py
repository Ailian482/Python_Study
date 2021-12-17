# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/8/5 下午10:52

# 闭包函数
# 既然可以把函数作为一个形参进行传参，作为回调函数，那么如果在一个函数中，返回了一个函数呢？
# 在一个函数内部返回了一个内函数，并且这个返回的内函数还使用了外函数中局部变量，这就是闭包函数
# 其实就是 在函数内部 定义了一个 使用了外函数中局部变量的 内函数

"""
闭包函数的特点
    1. 在外函数中定义了局部变量，并且在内部函数中使用了这个局部变量
    2. 外函数中返回了 内函数，返回的内函数就是闭包函数
    3. 主要在于保护了外函数中的局部变量，既可以被使用，又不会被破坏
闭包函数的作用
    保护了函数中的变量不受外部的影响，但是又能够不影响使用
"""

money = 0


# 工作
def work():
    global money
    money += 100


def overtime():
    global money
    money += 200


def buy():
    global money
    money -= 50


# work()
# work()
# work()
# overtime()
# buy()
# # 银行垮台了，没钱了...
# money = 0
# work()
# print(money)

# 对程序进行改造 成 闭包函数，如果传入工作、加班，则 总金额增加，如果是购物则 总金额减少

def person():
    per_money = 0
    while True:
        per_type = input("请输入一个类型(工作、加班、购物)：")
        # 工作
        if per_type == "工作":
            def work():
                # 在内函数中使用了外函数的临时变量
                nonlocal per_money
                per_money += 100
                print(per_money)

            # 在外函数中返回了内函数，这个函数就是闭包函数
            return work

        # 加班
        elif per_type == "加班":
            def overtime():
                nonlocal per_money
                per_money += 200
                print(per_money)
            return overtime

        # 购物
        elif per_type == "购物":
            def buy():
                nonlocal per_money
                per_money -= 50
                print(per_money)
            return buy

        # 其他 报错
        else:
            print("请重新输入正确的类型！")
            continue


res = person()  # return work res=work
res()
res()
res()
# 此时，就不能在全局中对money这个局部变量进行任何操作

# 如何检测一个函数是否为闭包函数 函数名.__closure__
# 如果是闭包函数返回 cell; 如果不是闭包函数返回 None

print(res.__closure__)  # (<cell at 0x7fabc4cfffd0: int object at 0x7fabc4989510>,)