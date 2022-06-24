# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/5/30 下午1:12


"""
类的继承
语法格式：
    class 子类类名(父类1, 父类2):
        pass

如果一个类没有继承任何类，则默认继承 object
Python支持多继承
定义子类时，必须在其构造函数中调用父类的构造函数
"""


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(self.name, self.age)


class Student(Person):
    def __init__(self, name, age, stu_no):
        super().__init__(name, age)  # 父类有 __init__() 方法，子类要定义 __init__() 方法，必须要调用父类的 __init__() 方法
        self.stu_no = stu_no


class Teacher(Person):
    def __init__(self, name, age, teach_of_years):
        super().__init__(name, age)
        self.teacher_years = teach_of_years


stu = Student('小舞', 18, '1001')
teacher = Teacher('小三', 19, 3)
stu.info()  # 小舞 18
teacher.info()  # 小三 19


# 多继承
class A(object):
    pass


class B(A):
    pass


class C(A, B):
    pass
