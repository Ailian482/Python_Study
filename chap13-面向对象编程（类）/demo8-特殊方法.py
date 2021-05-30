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

print(c)
print(d)


class Student:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):  # 这个方法可以 实现了两个对象的加法运算
        return self.name + other.name

    def __len__(self):
        return len(self.name)


stu1 = Student("Jack and Bank")
stu2 = Student("李四")

# 如果要实现两个对象（原本不能直接相加）执行相加操作，那么一定是写过 __add__() 特殊方法
s = stu1 + stu2  # 实现了两个对象的加法运算（因为在Student类中 编写了 __add__()特殊方法）
print(s)
print("--------------------")
s = stu1.__add__(stu2)
print(s)

print("---------------------------------")
lst = [11, 22, 33, 44]
print(len(lst))
print(lst.__len__())
print(len(stu1))


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