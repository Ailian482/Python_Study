# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/6/23 上午10:49


"""
类定义          C
类对象          C
实例对象    a   b   c

为了避免名字上的冲突，应该遵守一些约定成俗的规定：
    1. 不要试图在一个类里面定义出所有能想到的特性和方法，应该利用继承和组合机制来进行扩展
    2. 用不同的词性命名，如属性名用名词，方法名用动词

python的绑定：
    python严格要求方法需要有实例才能被调用，这种限制其实就是python所谓的绑定概念

类中定义的属性和方法都是静态变量，就算类对象 CC() 被删除了，他们依然是存放在内存当中的，只有当程序退出的时候，变量才会被释放

"""


class C:
    count = 0


a = C()
b = C()
c = C()

print(a.count)
print(b.count)
print(c.count)

c.count += 10  # 实例属性把类属性覆盖了
print(c.count)
print(a.count)
print(b.count)

print(C.count)
C.count += 100
print(a.count)
print(b.count)
print(c.count)

# 如果属性的名字跟方法的名字相同，属性会把方法覆盖掉
class A:
    def x(self):
        print('x-man！')


a = A()
a.x()
a.x = 1  # 属性 x 把 类方法 x 覆盖了
print(a.x)
# a.x()  # 报错：TypeError: 'int' object is not callable

# 绑定例子
class BB:
    def printBB():
        print("no zuo no die")


BB.printBB()
bb = BB()
# bb.printBB()  # TypeError: printBB() takes 0 positional arguments but 1 was given
# bb.printBB(bb)  # 实例化调用机制，会把实例化对象 bb 传给类方法 printBB()


# 绑定例子2
class CC:
    def setXY(self, x, y):
        self.x = x  # self 是dd
        self.y = y  # self 是dd

    def printXY(self):
        print(self.x, self.y)


dd = CC()
print(dd.__dict__)
print(CC.__dict__)  # __dict__可以查看对象所拥有的属性，以字典的形式返回，没有返回魔法方法

dd.setXY(4, 5)  # 4, 5是仅属于实例对象 dd 的
# dd.seXY(dd, 4, 5)  # 传参机制，dd 是自动传的，不需要我们自己添加上去
print(dd.__dict__)
print(CC.__dict__)

# del CC
# ee = CC()  # NameError: name 'CC' is not defined

dd.printXY()
