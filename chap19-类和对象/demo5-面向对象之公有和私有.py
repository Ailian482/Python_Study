# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/6/22 下午5:06

"""
Python中如何定义私有变量？
    只需要在变量名或函数名前加上"__"两个下划线，那么这个变量或者函数就会变为私有的
Python中的私有变量其实是 伪私有
"""


class Person:
    # python 会自动将 双下划线开头 的变量改名为 _类名__变量名
    __name = "小白猪"  # 从类的外部是访问不了这个变量的，需要从类函数内部获取

    def getName(self):  #
        return self.__name


p = Person()
# print(p.name)  # 获取不到name属性
p_name = p.getName()  # 通过这个方法获取name属性
print(p_name)
p_name1 = p._Person__name  # 可以通过 实例对象._类名__变量名
print(p_name1)

