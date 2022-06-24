# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2022/5/16 下午4:02


"""
Python是动态语言，在创建对象后，可以动态的绑定属性和方法

一个类可以创建 n 多个类的实例对象，每个实例对象的属性值可以不同
"""

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + '在吃饭')

stu1 = Student('小舞', 20)  # 类实例1
stu2 = Student('小三', 21)  # 类实例2
print(id(stu1))
print(id(stu2))
print('>>>>>>>>> 为 stu2 动态绑定性别属性 >>>>>>>>>>>>')
stu2.gender = '男'  # 这个属性只适用于 stu2 实例对象
print(stu1.name, stu1.age)  # 小舞 20
print(stu2.name, stu2.age, stu2.gender)  # 小三 21 男

print('>>>>>>>>> 为 stu2 动态绑定show()方法 >>>>>>>>>>>>')
stu1.eat()
stu2.eat()


def show():
    print('定义在类之外的，称函数')


stu1.show_method = show  # show 是绑定的方法
stu1.show_method()  # 定义在类之外的，称函数