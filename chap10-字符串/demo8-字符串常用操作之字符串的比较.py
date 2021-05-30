# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/5/19 上午9:30

"""
ord()：可以输出字符的 原始值
chr()：可以得到指定 原始值 对应的字符
"""

print('apple' > 'app')
print('apple' > 'banana')

print(ord('a'), ord('b'))
print(chr(97), chr(98))

print(ord('朱'))
print(chr(26417))

"""
== 与 is 的区别
== 比较的是值
is 比较的是 id（内存地址） 是否想等
"""
# pycharm中字符串有驻留机制，同一个字符串只会储存一次，所以 a,b,c都指向同一个"Python"
a = b = "Python"
c = "Python"

print(a == b)
print(a == c)

print(a is b)
print(a is c)

print(id(a))
print(id(b))
print(id(c))

# 列表没有驻留机制，创建了多少个相同列表，就会保存多少个。所以 a,b 指向同一个"Python"，而 c 执行另一个"Python"
a = b = [1, 2]
c = [1, 2]
print(a == b == c)
print(a is b)
print(a is c)
print(id(a))
print(id(b))
print(id(c))
