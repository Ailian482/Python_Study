# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2022/5/16 下午5:36

"""
面向对象的三大特征
    封装：提高程序的安全性
        1. 将数据（属性）和行为（方法）包装到类对象中。在方法内部对属性进行操作，在类对象的外部调用方法。
        这样无需关心方法内部的具体实现细节，从而隔离了复杂度
        2. 在python中没有专门的修饰符用于属性的私有，如果该属性不希望在类对象外部被访问，
        那么变量名用两个下划线来定义：__name = "小白猪"，但是还是可以被使用
    继承：提高代码的复用性
    多态：提高程序的可扩展性和可维护性
"""

class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print("汽车已启动...")


car = Car('宝马X5')
car.start()  # 汽车已启动...
print(car.brand)  # 宝马X5


class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # 年龄不希望在类的外部使用，所以使用两个下划线 _

    def show(self):
        print(self.name, self.__age)


stu = Student('张三',20)
stu.show()  # 张三 20
# 在类的外部使用 name 和 age
print(stu.name)  # 张三
# print(stu.__age)  # AttributeError: 'Student' object has no attribute '__age'

print(dir(stu))  # 可以查看该类对象都有哪些属性和方法
"""
['_Student__age', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', 
'__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', 
'__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__',
 '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
  '__str__', '__subclasshook__', '__weakref__', 'name', 'show']
"""
# 在类的外部可以通过 _Student__age 进行访问私用属性
print(stu._Student__age)  # 20


