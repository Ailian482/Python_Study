# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/5/30 下午1:34

"""
object类是所有类的父类，因此所有类都有object类的属性和方法
内置函数dir()可以查看指定对象所有属性
object有一个__str__()方法，用于返回一个对于"对象的描述"，
对应于内置函数srt()经常用于print()方法，帮我们查看对象的信息，所以我们经常会对__str__()进行重写

"""

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print('姓名：{0}, 年龄：{1}'.format(self.name, self.age))

    def __str__(self):
        # 重写前输出：<__main__.Person object at 0x7fb651a9ce20>
        return '姓名：{0}, 年龄{1}'.format(self.name, self.age)
        # 重写后，把__str__()当成一个方法调用，直接输出 return 后面的内容：姓名：Bank, 年龄20


o = object()
p = Person('Bank', 20)
print(dir(o))
print('----------------')
print(dir(p))
print(p)  # 默认会调用__str__()这样的方法
print(type(p))  # 类型还是Person类型：<class '__main__.Person'>
