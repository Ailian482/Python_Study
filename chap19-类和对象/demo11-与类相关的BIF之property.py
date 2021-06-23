# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/6/23 下午2:16

"""
x = property(fget=None, fset=None, fdel=None, doc=None)
第一个参数：获取属性的方法
    至于如何获取属性，由我们自己去定义
第二个参数：设置属性的方法
    至于如何设置属性，由我们自己去定义
第三个参数：删除属性的方法
    至于如何删除属性，由我们自己去定义
第四个参数：


之后获取属性的方法：
    实例对象名.x

property的作用：
    程序慢慢写的非常复杂，不断的把它完善起来，有一天突然心血来潮，突然想对这个程序进行大改，去加多一些东西，
    或者把一些方法名getSize、setSize、delSize修改了，原本没有的东西，提供给用户的话，需要给用户提供新的接口，这样用户可能不开心
    但是如果有了 property函数，这个问题就很好解决了，原本提供给用户的只是 x，你的函数大改了也没有关系，只要property里面的参数名跟着改就OK了
    用户只需要调用 x 来设置，获取等操作属性
"""


class C:
    def __init__(self, size=10):
        self.size = size

    def getSize(self):
        return self.size

    def setSize(self, value):
        self.size = value

    def delSize(self):
        del self.size

    x = property(getSize, setSize, delSize)



c1 = C()
print(c1.getSize())
print(c1.x)
c1.x = 18
print(c1.size)
print(c1.getSize())
del c1.x
print(c1.size)  # AttributeError: 'C' object has no attribute 'size'

