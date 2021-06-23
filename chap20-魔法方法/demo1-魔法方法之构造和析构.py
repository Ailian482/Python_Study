# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/6/23 下午2:56

"""
魔法方法：
    1. 总是被双下划线包围，例如 __init__
    2. 是面向对象的Python的一切，如果你不知道魔法方法，说明你还没有意识到面向对象的Python的强大
    3. 魔法方法的"魔力"体现在他们总能够在适当的时候被自动调用

__init__(self[, ...]) 方法
    问题：我看你有时候在类定义的时候有写__init__方法，有时候却没有，这是为什么呢？
    要有需求，一般是给对象做初始化操作，才会重写 __init__(self) 方法
    注意：不能在 __init__(self)方法内试图做返回，即在 __init__(self)内添加一个 return 返回值

__new__(cls[, ...])方法
    这个是第一个被调用的方法
    如果cls 后面还有其他参数，则会原封不动的传给 __init__(self)方法
    需要一个实例对象作为返回值，需要返回一个对象，通常是返回cls这个类对象，也可以返回其他类的对象
    这个方法一般是极少去重写的
    有一种情况必须要去重写它，当继承不可变类型的时候，有需要进行修改的时候

__del__(self)方法
    析构器
    当一个对象将要被销毁的时候，这个方法就会被自动调用
    是当垃圾回收机制的，当没有任何变量去引用这个对象的时候，这个垃圾回收机制就会自动把它销毁，这时候才会调用 __del__方法
    del x != x.__del__()

"""


class Rectangle:  # 定义一个矩形，需要长和宽，所以实例化的时候需要传入两个参数，实例化的时候会自动调用__init__(self)方法
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getPeri(self):
        return (self.x + self.y) * 2

    def getArea(self):
        return self.x * self.y


rec = Rectangle(5, 6)
print(rec.getPeri())
print(rec.getArea())


"""
实例化一个CapStr对象时，不管传入的字符串是有 小写还是大写字母，都会自动转成大写
"""


class CapStr(str):  # 继承了一个不可改变的 str 类型，那么就不能在 __init__(self)方法进行修改
    def __new__(cls, string):
        string = string.upper()  # 在 __new__() 的时候，把传入的参数进行替换
        return str.__new__(cls, string)


a = CapStr('Ailain No WORld!')
print(a)


class C:
    def __init__(self):
        print("我是__init__方法，我被调用了...")

    # def __del__(self):
    #     print("我是__del__方法，我被调用了...")


c1 = C()
c2 = c1
print(c2)


"""
>>> class C:
...     def __init__(self):
...             print('我是__init__方法, 我被调用了...')
...     def __del__(self):
...             print('我是__del__方法, 我被调用了...')
... 
>>> c1 = C()
我是__init__方法, 我被调用了...
>>> c2 = c1
>>> c3 = c2
>>> 
>>> del c1
>>> del c2
>>> del c3
我是__del__方法, 我被调用了...
"""