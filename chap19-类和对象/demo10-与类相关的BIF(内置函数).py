# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/6/23 上午11:45

"""
issubclass(class, classinfo)
    如果第一个参数 class，是第二个参数 classinfo 的一个子类，那么就返回 True
    这种检查是非严格性的检查
    1. 一个类被认为是其自身的子类
    2. classinfo可以是类对象组成的元组，只要 class 是其中任何一个候选类的子类，则返回True，
       第二个参数如果不是类对象，或者不是类对象组成的元组，那么就会报 TypeError

isinstance(object, classinfo)
    检查一个实例化对象是否属于某个类的
    如果第一个参数object(实例对象)是第二个参数classinfo(类)的一个实例，则返回True
    classinfo可以是类对象组成的元组，只要 object 是其中任何一个候选类的 实例对象，则返回True
    第二个参数如果不是类对象，或者不是类对象组成的元组，那么就会报 TypeError

hasattr(object, name)
    attr = attribute：属性
    测试一个对象（object）是否有指定的属性（name--属性名）
    注意：name 要用引号括起来，作为一个字符串

getattr(object, name[, default])
    default参数是可选参数
    返回对象指定的属性值，如果指定的属性不存在，且有设置default值，那么就会返回 default 值，否则会抛出 AttributeError异常

setattr(object, name, value)
    给对象设置一个指定属性的值，如果指定的属性不存在，则会新建一个新的属性；如果指定的属性存在，那么就会覆盖原本的属性值

delattr(object, name)
    删除对象中指定的属性，如果属性不存在，则抛出 AttributeError异常
"""


class A:
    pass


class B(A):
    pass


class C:
    pass


print(issubclass(B, A))
print(issubclass(B, B))  # True，类本身也是也被认为是其自身的子类
print(issubclass(B, C))  # False
print(issubclass(B, (A, C)))
# print(issubclass(B, "A"))  # TypeError: issubclass() arg 2 must be a class or tuple of classes
print(issubclass(B, object))


class D:
    def __init__(self, x=0):
        self.x = x


d = D()
print(hasattr(d, "x"))  # 需要把属性名 变成字符串
print(getattr(d, 'x'))
print(getattr(d, 'y', '您访问的属性不存在...'))

setattr(d, 'y', 1)  # 设置好后需要用，getattr()获取
print(getattr(d, 'y'))
setattr(d, 'x', 10)
print(getattr(d, 'x'))

delattr(d, 'y')
# delattr(d, 'y')  # AttributeError: y
