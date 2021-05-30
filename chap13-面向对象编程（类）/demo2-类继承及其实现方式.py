# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/5/20 上午9:03

"""
语法格式：
class 子类类名(父类1,父类2...):
    pass

如果一个类灭有继承任何类，则默认继承object
python支持多继承，即一个子类可以继承多个父类，定义子类时，必须在其构造函数中调用父类的构造函数
"""

# 继承的代码实现
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print('姓名:{0}, 年龄:{1}'.format(self.name, self.age))


# 定义子类1
class Student(Person):
    def __init__(self, name, age, score):
        super().__init__(name, age)  # 调用父类（Person类的__init__()方法的属性）
        self.score = score  # Student类自己的属性

# 定义子类2
class Teacher(Person):
    def __init__(self, name, age, teachofyear):
         super().__init__(name, age)
         self.teachofyear = teachofyear



# 测试
stu = Student('Ailian', 20, '1001')
teacher = Teacher('lisi', 34, 10)
stu.info()  # 这个info()方法是从父类继承过来的
teacher.info()




lst = ['a', 'b', 's', 'w', 'w', 'a', 1, 2, 2, 1, 2]
new_lst = list(set(lst))
print(new_lst)

