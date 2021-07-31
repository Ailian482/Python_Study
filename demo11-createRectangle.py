# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/7/27 上午10:02

"""
创建一个矩形
    如果传入参数为 0 则打印一个实心矩形
    如果传入参数为 1 则打印一个空心矩形
"""

# 1. 先实现创建一个矩形（10行，每一行10个 "#"）
# 分析：循环打印，循环 100 次，每次打印 10个 "#"
# cycle_solid = range(1, 101)


def print_rectangle(a=0):
    cycle = range(1, 101)
    if a == 0:
        """打印实心矩形"""
        for i in cycle:
            print("#", end=' ')
            if i % 10 == 0:
                print()

    elif a == 1:
        """打印空心矩形"""
        for i in cycle:
            if i <= 10 or 91 <= i <= 100:
                print("#", end=" ")
                if i % 10 == 0:
                    print()
            if 10 < i < 91:
                if i % 10 == 1 or i % 10 == 0:
                    print("#", end=" ")
                else:
                    print(" ", end=" ")
                if i % 10 == 0:
                    print()


input_type = input("请输入0或者1，0代表打印实心矩形，1代表打印打印空心矩形：")
while True:
    if int(input_type) == 1 or int(input_type) == 0:
        print_rectangle(int(input_type))
        break
    else:
        """输入错误的情况"""
        print("输入错误，请输入0或者1！")
        input_type = input("请输入0或者1，0代表打印实心矩形，1代表打印打印空心矩形：")


# cycle_hollow = range(99, -1, -1)
# cycle_hollow = range(1, 101)
# for i in cycle_hollow:
    # if i <= 10 or 91 <= i <= 100:
    #     print("#", end=" ")
    #     if i % 10 == 0:
    #         print()
    # if 10 < i < 91:
    #     if i % 10 == 1 or i % 10 == 0:
    #         print("#", end=" ")
    #     else:
    #         print(" ", end=" ")
    #     if i % 10 == 0:
    #         print()



