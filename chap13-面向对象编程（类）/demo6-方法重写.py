# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/5/30 下午1:15

"""
如果子类对继承父类的某个属性或者方法不满意，可以在子类中对其（方法体）进行重新编写
子类重写后的方法中可以通过super().xxx()调用弗雷中被重写的方法

"""

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print('姓名：{0}, 年龄{1}'.format(self.name, self.age))


class Student(Person):
    def __init__(self, name, age, stu_no):
        super().__init__(name, age)
        self.stu_no = stu_no

    def info(self):
        super().info()  # 调用父类的 info() 方法
        print('学号：{}'.format(self.stu_no))


class Teacher(Person):
    def __init__(self, name, age, teach_of_year):
        super().__init__(name, age)
        self.teach_of_year = teach_of_year

    def info(self):
        super().info()  # 调用父类的 info() 方法，执行程序先执行这个
        print('教龄：{0}'.format(self.teach_of_year))


# test
stu = Student('公孙离', 18, '1001')
teacher = Teacher('亚瑟', 30, 10)
stu.info()
print("---------------------------")
teacher.info()


"""
结果：
姓名：公孙离, 年龄18
学号：1001
---------------------------
姓名：亚瑟, 年龄30
教龄：10
"""
