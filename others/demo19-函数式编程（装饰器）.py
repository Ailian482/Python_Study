# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/11/25 下午2:47


import time, functools


"""
装饰器：就是把函数装饰一下，为函数添加一些附加功能，装饰器就是一个函数，参数为被包装的函数，返回包装后的函数

需要在函数运行前后打印一条日志，但是又不希望或者没有权限修改函数内部的结构，就可以用到装饰器（decorator）

"""


def metric(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        start_time = time.time()
        ans = func(*args, **kw)
        end_time = time.time()
        print('%s executed in %.2f ms' % (func.__name__, (end_time-start_time)*1000))
        return ans
    return wrapper


@metric
def fast(x, y):
    sleep_time = time.strftime('%H:%M:%S')
    print(sleep_time)
    return x + y
# 函数的执行步骤：metric(fast)


@metric
def slow(x, y):
    sleep_time = time.strftime('%H:%M:%S')
    print(sleep_time)
    return x + y


print(fast(1, 2))
print(slow(3, 4))

print(time.time())