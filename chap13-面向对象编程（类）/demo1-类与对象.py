# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/5/19 下午1:37


"""
类
    类别，分门别类，物以类聚，人类，鸟类，动物类，植物类...
    类是多个类似事物组成的群体的统称，能够帮助我们快速理解和判断事物的性质
对象
    类别下面一个具体的内容，就叫做对象或者实例
例如：张三、李四都是人类，张三、李四就是人类的一个实例或对象

从实例方法、静态方法和类方法的调用规则可以得出以下结论：

通过实例定义的变量只能被实例方法访问，而直接在类中定义的静态变量(如本例的name变量)即可以被实例方法访问，也可以被静态方法和类方法访问。
实例方法不能被静态方法和类方法访问，但静态方法和类方法可以被实例方法访问。

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
    def sm():
        print('我是一个静态方法，因为使用了staticmethod修饰')

    # 类方法
    @ classmethod
    def cm(cls):  # 要求要传 cls 参数
        print('我是一个类方法，因为使用了classmethod修饰')


# Python 中一切皆对象，Student也是对象，有对象的三大特性，id(开辟了内存空间)、类型、值，所以Student是类对象
print(id(Student))   # 140287397753424，有内存空间，
print(type(Student))  # <class 'type'>
print(Student)  # <class '__main__.Student'>

# 创建Student类的对象
stu = Student('Ailian', 25)   # stu 是Student类的一个实例
print(id(stu))   # 140357893971728
print(type(stu))  # <class '__main__.Student'>
print(stu)  # <__main__.Student object at 0x7fa79e695f10>


stu.eat()  # 类方法调用方式1：对象.方法名
Student.eat(stu)  # 类方法调用方式2：类名.方法(类的对象)-->该对象就是类方法里面的 self

# print('-------------初始化属性--------------')
stu1 = Student('小舞', 20)  # 类实例1
stu2 = Student('小三', 21)  # 类实例2
print(stu1.name)  # 小舞
print(stu1.age)  # 20
print('id：', id(stu1), '类型：', type(stu1))  # id： 140467020324240 类型： <class '__main__.Student'>，创建实例就开辟了新的内存空间去存储实例对象
print(stu1)  # <__main__.Student object at 0x7fc106d95d90>
print('id：', id(stu2), '类型：', type(stu2))  # id： 140467020324096 类型： <class '__main__.Student'>
print(stu2)  # <__main__.Student object at 0x7fc106d95d00>


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