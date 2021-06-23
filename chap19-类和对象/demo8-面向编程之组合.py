# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/6/23 上午10:35


"""
里面有一只乌龟和十条鱼，乌龟通过吃鱼来补充体力，当乌龟体力耗尽或者鱼被吃光则游戏结束
现在我们想要扩展游戏，给鱼类进行细分，有金鱼（Goldfish），鲤鱼（Carp），三文鱼（Salmon），还有鲨鱼（Shark）。

什么是组合？
    把类的实例化放到新类里面，就会把旧类组合进去了，这样就不用继承了，没有什么风险
    把不是很有继承关系的类，没有直线关系、没有横向关系的类，放到一起
    要实现纵向关系，就使用继承

python的另一个编程机制：
    Mix-in

"""


class Turtle:
    def __init__(self, x):
        self.num = x


class Fish:
    def __init__(self, x):
        self.num = x


class Pool:
    def __init__(self, x, y):
        self.turtle = Turtle(x)
        self.fish = Fish(y)

    def print_num(self):
        print("水池里总共有乌龟%d只，小鱼%d条！" % (self.turtle.num, self.fish.num))


pool = Pool(1, 10)
pool.print_num()