# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/6/22 下午3:57

"""
对象 = 属性 + 方法

类对象：看上去是怎样，会做什么

属性：静态的特征（变量）
方法：动态的动作（函数）
"""


class Turtle:  # python中约定类名以大写字母开头，大驼峰命名
    """关于类一个简单的例子"""
    # 属性
    color = "green"
    weight = 10
    legs = 4
    shell = True
    mouth = "大嘴"

    # 方法
    def climb(self):
        print("我正在努力的向前爬......")

    def run(self):
        print("我正在飞快的向前跑......")

    def bite(self):
        print("咬死你咬死你.....")

    def eat(self):
        print("有得吃，真满足^_^")

    def sleep(self):
        print("困了，睡了，晚安，Zzzz")


turtle = Turtle()
print(turtle)
print(Turtle())  # python有一个垃圾处理机制，把Turtle()类对象创建出来，随即又把它删除掉
print(type(Turtle()), id(Turtle()))
print(turtle.color)
turtle.eat()
turtle.bite()
turtle.sleep()
