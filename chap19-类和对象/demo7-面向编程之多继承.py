# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/6/23 上午9:28

"""
多重继承
    看起来很牛逼，但是很容易导致代码混乱

定义类的时候，把要继承的父类写在 括号里面，用逗号隔开即可
例如：
    class A:
        pass
    class B:
        pass
    class C(A, B):  # 多重继承
        pass
"""


class Base1:
    def foo1(self):
        print("我是foo1，我为Base1代言......")


class Base2:
    def foo2(self):
        print("我是foo2，我为Base2代言......")


class Base3(Base1, Base2):
    pass


c = Base3()
c.foo1()
c.foo2()