# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/6/23 下午6:07


# 鱼池里有一只乌龟和10条鱼
# 乌龟靠吃鱼来补充体力
"""
游戏规则：
    中央位置为：(0, 0)，最大范围x(0，10)，y(0, 10)
    每条鱼都有一个初始化的位置，每次向左或者向右移动一个单位
    每条鱼和乌龟最多移动15次，如果移动15次乌龟还没有吃掉所有的鱼，那么游戏结束，如果游动15次以内把所有鱼都吃完，游戏也结束
"""

import random as r


class Fish:  # 定义一个鱼类
    def __init__(self):
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)

    def move(self):
        if self.x == 0:
            self.x += 1
        elif self.x > 0:
            self.x -= 1
        return (self.x, self.y)

    def getPosition(self):
        return (self.x, self.y)


class Turtle(Fish):  # 定义一个乌龟类
    def move(self):
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)

    def getPosition(self):
        return (self.x, self.y)


class GoldFish(Fish):
    pass


class Salmon(Fish):
    pass


num = 10
count = 0
g = GoldFish()
print(g.getPosition())
s = Salmon()
t = Turtle()
while count < 15:
    for p_fish in range(10):
        fish_p = g.getPosition()
        if g.getPosition() == t.getPosition():
            num -= 1
        else:
            g.move()
    count += 1



