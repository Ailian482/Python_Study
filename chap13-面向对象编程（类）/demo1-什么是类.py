# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/5/19 下午1:37


"""
从实例方法、静态方法和类方法的调用规则可以得出以下结论：

通过实例定义的变量只能被实例方法访问，而直接在类中定义的静态变量(如本例的name变量)即可以被实例方法访问，也可以被静态方法和类方法访问。
实例方法不能被静态方法和类方法访问，但静态方法和类方法可以被实例方法访问。

"""
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


"""
结果：
-------------初始化属性--------------
小舞
20
id： 140515772442272 类型： <class '__main__.Student'>
<__main__.Student object at 0x7fcc60b3a6a0>
id： 140515773065152 类型： <class '__main__.Student'>
<__main__.Student object at 0x7fcc60bd27c0>
"""