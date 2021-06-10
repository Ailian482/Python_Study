# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/5/31 下午3:57

"""
lambda函数又名匿名函数
lambda表达式语法格式（省略了函数名）：
    lambda 参数:表达式
返回一个没有名字的函数对象，用一个变量来接
调用方法：跟正常函数那样调用，变量名就相当于函数名

lambda函数的使用：
    1. python在写一些执行脚本的时候，使用lambda函数可以省下定义函数的时间
        比如说写一个简单的脚本来管理服务器时间，不需要定义一个函数，然后再调用，使用lambda函数会使代码更加的精简
    2. 对于一些比较抽象并且整个程序执行下来只需要调用一两次的函数，使用lambda函数就可以省去给函数起名字的时间
        毕竟给函数起名字是一件比较麻烦的事，要有意义而且不能重复
    3. 简化代码的可读性，普通的屌丝函数，阅读经常需要跳到开头def定义部分，

"""
func = lambda x: x**2
print(func(6))

funct1 = lambda x, y: x+y
print(funct1(1, 2))

def new_func(x):
    return(lambda y: x+y)


t = new_func(3)
u = new_func(2)
print(t(3))
print(u(3))


class DataBase:
    '''Python 3 中的类'''

    def __init__(self, id, address):
        '''初始化方法'''
        self.id = id
        self.address = address
        self.d = {self.id: 1,
                  self.address: "192.168.1.1",
                  }

    def __getitem__(self, item):
        # return self.__dict__.get(key, "100")
        return self.d.get(item, "default")


# 当实例对象通过[] 运算符取值时，会调用它的方法__getitem__，并且返回return值
data = DataBase(1, "192.168.2.11")  # 实例化对象
print(data.d)
print(data['hi'])  # 通过[]取值，会调用__getitem__方法
print(data[data.address])
