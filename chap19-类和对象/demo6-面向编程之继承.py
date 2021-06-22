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


class Parent:
    def hello(self):
        print("正在调用父类的方法......")


class Child(Parent):
    def hello(self):
        print("正在调用子类的方法......")


p = Parent()
p.hello()

c = Child()
c.hello()
