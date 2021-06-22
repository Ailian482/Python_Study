# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/6/22 下午4:14


"""
OO = Object Oriented （面向对象）
特征1：封装
    封装了属性（变量）和 方法（函数）
    信息隐蔽技术
特征2：继承
    子类自动共享父类之间的数据和方法的机制
特征3：多态
    不同对象对同一方法响应不同的行动
    例如：移动的方法
        老虎是快速奔跑移动
        袋鼠是快速的跳跃移动
        乌龟是慢慢爬
        小甲鱼是一步一个脚印自信的往前走👣

"""

list1 = [4, 5, 6, 1, 7, 3, 0, 9]
list1.sort()
print(list1)
list1.append(5)
print(list1)


class MyList(list):  # MyList继承list
    pass


list2 = MyList()
list2.append(6)
list2.append(8)
list2.append(3)
print(list2)
list2.sort(reverse=True)
print(list2)


class A:
    def fun(self):
        print("我是小A...")


class B:
    def fun(self):
        print("我是小B...")


a = A()
b = B()
a.fun()  # 同样的方法，但是结果不一样
b.fun()
