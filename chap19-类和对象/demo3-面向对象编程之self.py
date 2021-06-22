# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/6/22 下午4:34

"""
OOA：面向对象分析
OOP：面向对象编程
OOD：面向对象设计
"""

"""
self是什么？
    类是房子图纸，通过类实例化的对象才是能够住人的房子
    根据一张房子图纸，可以设计出成千上万的房子，房子都是一样的，但是他们有不同的主人
    self就是一样的道理，由同一个类可以生成无数个对象， 对象都很相似，因为都来自同样的属性和方法
    当一个对象的方法被调用的时候，对象会将自身作为第一个参数传给self，接收到self的时候，python就知道是哪个对象在调用方法
"""


class Ball:
    def setName(self, name):
        self.name = name

    def click(self):
        print("我叫%s，该死的，谁踢我..." % self.name)


a = Ball()
a.setName('球A')
b = Ball()
b.setName("球B")
c = Ball()
c.setName("土豆")
a.click()
b.click()
c.click()