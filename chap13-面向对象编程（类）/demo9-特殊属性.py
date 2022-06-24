# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/5/30 下午3:06

"""
特殊属性：
    __dict__：获得对象或实例对象所绑定的所有属性和方法的字典

"""
# print(dir(object))


class A:
    pass


class B:
    pass


class C(B, A):
    def __init__(self, name, age):
        self.name = name
        self.age = age


class D(A):
    pass


# 创建C类对象
x = C('Bank', 20)
print(x.__dict__)  # 实例对象的属性字典
print(C.__dict__)  # 看到类的属性和方法的字典
print("----------------")
print(x.__class__)  # <class '__main__.C'> 输出对象所属的类
print(C.__bases__)  # C类的父类类型的元素 (<class '__main__.A'>, <class '__main__.B'>)
print(C.__base__)  # 输出继承的第一个父类类型的元素 <class '__main__.B'>
print(C.__mro__)  # 查看类的层次结构
print(A.__subclasses__())  # 查看A的子类

"""
结果
{'name': 'Bank', 'age': 20}
{'__module__': '__main__', '__init__': <function C.__init__ at 0x7fc191721820>, '__doc__': None}
----------------
<class '__main__.C'>
(<class '__main__.B'>, <class '__main__.A'>)
<class '__main__.B'>
(<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
[<class '__main__.C'>, <class '__main__.D'>]
"""