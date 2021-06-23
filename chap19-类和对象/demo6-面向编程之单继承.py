# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/6/22 下午5:24

"""
我们试图模拟一个场景：
    里面有一只乌龟和十条鱼，乌龟通过吃鱼来补充体力，当乌龟体力耗尽或者鱼被吃光则游戏结束
现在我们想要扩展游戏，给鱼类进行细分，有金鱼（Goldfish），鲤鱼（Carp），三文鱼（Salmon），还有鲨鱼（Shark）。


被继承的类：基类、父类或者超类
继承者：子类，可以继承父类的任何属性和方法

如果子类中定义与父类同名的方法或者属性，则会覆盖父类对应的方法或属性，只有子类会被覆盖
"""


# class Parent:
#     def hello(self):
#         print("正在调用父类的方法......")
#
#
# class Child(Parent):
#     def hello(self):
#         print("正在调用子类的方法......")
#
#
# p = Parent()
# p.hello()
#
# c = Child()
# c.hello()


import random as r


# 定义一个鱼类，初始位置，以及他的移动方式
# 初始位置是随机的，之后都是每次往左移动一个单位
class Fish:
    def __init__(self):
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)

    def move(self):
        self.x -= 1
        # return self.x
        print("我的位置是：", self.x, self.y)


# 定义一个金鱼
class GoldFish(Fish):  # 继承Fish类
    pass


# 定义一个鲤鱼
class Carp(Fish):
    pass


# 定义一个三文鱼
class Salmon(Fish):
    pass


# 定义一个鲨鱼
class Shark(Fish):
    # def __init__(self):  # 重写 __init__(self) 方法，那么Fish的 __init__(self) 方法就会被覆盖
    #     self.hungry = True
    # 解决这类问题的方法
    # # 第一种方法：调用未绑定的父类方法
    # def __init__(self):
    #     Fish.__init__(self)
    #     self.hungry = True

    # 第二种：使用super()函数
    def __init__(self):
        super().__init__()  # 超级之处，不用给出任何基类的名字，不管是有多重继承还是，super()会自动一层层找出所有基类对应的方法
        # 如果要改变继承关系，直接改定义类时，继承的父类的名字就可以了
        self.hungry = True

    def eat(self):
        if self.hungry:
            print("吃货的梦想就是天天有的吃^_^")
            self.hungry = False
        else:
            print("太撑了， 吃不下了！")


fish = Fish()
print((fish.x, fish.y))  # 初始位置
fish.move()  # 向左移动一个单位
print("====================================")

goldfish = GoldFish()  # 实例化一个金鱼类
print((goldfish.x, goldfish.y))  # 初始位置
goldfish.move()  # 向左移动一个单位
print("====================================")

shark = Shark()  # 实例化一个鲨鱼类
shark.eat()
# print((shark.x, shark.y))  # 报错：AttributeError: 'Shark' object has no attribute 'x'，变量x不存在
# shark.move()  # 报错：AttributeError: 'Shark' object has no attribute 'x'，变量x不存在
"""
报错的原因：
    Shark类虽然继承了Fish类，但是Shark类重写了 __init__(self)方法，导致继承后的Fish类的 __init__(self)方法被覆盖，
"""
# # 第三种方法
# Fish.__init__(shark)  # 没有绑定父类的__init__(self)方法
# print((shark.x, shark.y))
# shark.move()

# 第二种方法
print((shark.x, shark.y))
shark.move()

