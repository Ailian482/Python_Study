# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2022/5/16 下午3:16

"""
类属性：类中方法外的变量称为类属性，被该类的所有对象所共享
类方法：使用 @ classmethod 修饰的方法，没有 self 参数，使用类名直接访问的方法（无需实例化，可直接调用）
静态放发：使用 @ staticmethod 修饰的方法，没有 self 参数，使用类名直接访问的方法（无需实例化，可直接调用）
"""

class Student:  # Student 为类的名称（类名），由一个或多个单词组成，每个单词的首字母要大写，其余小写

    native_place = '广东'  # 直接写在类里面的变量，称为类属性

    def __init__(self, name, age):  # 类初始化方法
        # 类的初始化属性，可以类实例可以设置相同的属性，也可以设置不同的属性
        self.name = name  # self.name 称为实体属性，进行了一个赋值操作，将局部变量 name 的值赋给实体属性
        self.age = age

    # 实例方法
    def eat(self):  # 在类外面定义的称为函数，在类里面定义的称为方法
        print('学生在吃饭...')

    # 静态方法
    @ staticmethod
    def sm(age):
        print('我是一个静态方法，因为使用了staticmethod修饰', age)

    # 类方法
    @ classmethod
    def cm(cls, arg):  # 要求要传 cls 参数
        print('我是一个类方法，因为使用了classmethod修饰', arg)


# 类属性的使用方式
print(Student.native_place)  # 广东
stu1 = Student('小舞', 20)  # 类实例1
stu2 = Student('小三', 21)  # 类实例2
print(stu1.native_place)  # 广东
print(stu2.native_place)  # 广东
Student.native_place = '希格拉'
print(Student.native_place)  # 希格拉
print(stu1.native_place)  # 希格拉
print(stu2.native_place)  # 希格拉


# 类方法的使用方式，调用类方法
Student.cm("小白猪")  # 我是一个类方法，因为使用了classmethod修饰 小白猪


# 静态方法的使用方式，调用静态方法
Student.sm(12)  # 我是一个静态方法，因为使用了staticmethod修饰 12
