# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/5/19 下午1:37

class Student:

    native_place = '广东'  # 类属性

    def __init__(self, name, age):  # 类初始化方法
        # 类的初始化属性，可以类实例可以设置相同的属性，也可以设置不同的属性
        self.name = name
        self.age = age

    def eat(self):
        print('我是一个方法')

    @ staticmethod
    def sm():  #
        print('我是一个静态方法，因为使用了staticmethod修饰')

    @ classmethod
    def cm(cls):
        print('我是一个类方法，因为使用了classmethod修饰')



# stu = Student()
# stu.eat()  # 类方法调用方式1：对象.方法名
# Student.eat(stu)  # 类方法调用方式2：类名.方法(类的对象)-->该对象就是类方法里面的 self

print('-------------初始化属性--------------')
stu1 = Student('小舞', 20)  # 类实例1
stu2 = Student('小三', 21)  # 类实例2
print(stu1.name)
print(stu1.age)
print('id：', id(stu1), '类型：', type(stu1))  # 创建实例就开辟了新的内存空间去存储实例对象
print(stu1)
print('id：', id(stu2), '类型：', type(stu2))
print(stu2)
