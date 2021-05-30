# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/5/15 下午11:59

"""
1. 集合元素的判断
    in 或者 not in
"""
s = {10, 30, 56, 68, 120}
print(10 in s)  # True
print(100 in s)  # False
print(10 not in s)  # False
print(100 not in s)  # True

"""
2. 集合元素的新增操作
    调用 add()方法，一次添加一个元素
    调用update()方法，一次至少添加一个元素
"""
s.add(80)
print(s)
s.update({200, 300, 400})  # 可以将集合里的元素添加到集合里面
print(s)
s.update([1, 2, 3])  # 可以将列表的元素添加到集合里面
print(s)
s.update((12, 13, 16, 15))  # 可以将元组的元素添加到集合里面
print(s)

"""
3. 集合元素的删除操作
    调用remove()方法，一次删除一个指定的元素，如果指定的元素不存在抛出 KeyError 异常
    调用discard()方法，一次删除一个指定的元素，如果指定的元素不存在不抛出异常
    调用pop()方法，一次只删除任意一个元素
    调用clear()方法，清空集合
"""
s.remove(30)
print(s)
# s.remove(500)  # 删不存在的元素，报错：KeyError: 500

s.discard(120)
print(s)
s.discard(100)
print(s)  # 删不存在的元素，不会报错

s.pop()
s.pop()
s.pop()
print(s)

s.clear()
print(s)
