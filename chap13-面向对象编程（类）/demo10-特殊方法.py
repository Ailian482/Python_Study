# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/5/30 下午3:27

"""
特殊方法：
    __len__()：通过重写__len__()方法，让内置函数len()的参数可以是自定义类型
    __add__()：通过重写__add__()方法，可使用自定义对象具有"+"功能
    __new__()：用于创建对象
    __init__()：对创建的对象进行初始化

"""

a = 20
b = 100
c = a + b  # 两个整数类型的对象的相加操作
d = a.__add__(b)  # 相当于：a+b

print(c)  # 120
print(d)  # 120


class Student:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):  # 这个方法可以 实现了两个对象的加法运算
        return self.name + other.name

    def __len__(self):  # 没有重写这个特殊方法，则 Student 类是不能都输出 实例对象的长度的
        return len(self.name)


stu1 = Student("Jack and Bank")
print(type(stu1), stu1)  # <class '__main__.Student'> <__main__.Student object at 0x7f84c8b95fa0>
stu2 = Student("李四")

# 如果要实现两个对象（原本不能直接相加）执行相加操作，那么一定是写过 __add__() 特殊方法
s = stu1 + stu2  # 实现了两个对象的加法运算（因为在Student类中 编写了 __add__()特殊方法）
print(s)  # Jack and Bank李四
print("--------------------")
s = stu1.__add__(stu2)
print(s)  # Jack and Bank李四

print("---------------------------------")
lst = [11, 22, 33, 44]
print(len(lst))  # 4
print(lst.__len__())  # 4
print(len(stu1))  # 13


"""
结果：
120
120
Jack and Bank李四
--------------------
Jack and Bank李四
---------------------------------
4
4
13
"""