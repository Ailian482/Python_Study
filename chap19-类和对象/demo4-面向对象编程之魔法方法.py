# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/6/22 下午4:47

"""
Python的对象天生拥有一些神奇的方法，他们是面向对象的Python的一切
他们是可以给你的类增加魔力的特殊方法
如果你的对象实现了这些方法中的某一个方法，那么这个方法会在特殊的情况下被Python调用，而这一切都是自动发生的

这些魔法方法都是 用双下划线命名，例如 __init__(self)方法
"""

"""
__init__(self)：构造方法
只要实例化一个对象，这个方法就会在对象被常创建的时候自动调用
实例化对象的时候可以传入一些参数，这些参数会自动的传入到 __init__() 方法中
可以通过重写这个方法来自定义对象的初始化操作
"""

class Ball:
    def __init__(self, name):
        self.name = name

    def click(self):
        print("我叫%s，该死的，谁踢我..." % self.name)


b = Ball("土豆")
b.click()