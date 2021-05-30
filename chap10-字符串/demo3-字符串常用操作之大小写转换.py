# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/5/16 下午3:35

"""
upper(): 把字符串中所有字母都转成大写字母
lower(): 把字符串中所有字母都转成小写字母
swapcase(): 把字符串中所有的大写字母转成小写字母，把所有小写字母转成大写
capitalize(): 把第一个字母转换为大写，把其余的字母转换成小写
    如果首字符不是字母，那么首字母不会转换成大写
title(): 把每个单词的第一个字符转换成大写，
"""

s = '你好hello ailIan'
a = s.upper()  # 转成大写之后，会产生一个新的对象，开辟一个新的内存去存储它
print(a, id(a))
print(s, id(s))

b = s.lower()  # 转成小写之后，会产生一个新的对象，开辟一个新的内存去存储它
print(b, id(b))
print(s, id(s))

c = s.swapcase()  # 会产生一个新的对象，开辟一个新的内存去存储它
print(c, id(c))
print(s, id(s))

d = s.title()  # 会产生一个新的对象，开辟一个新的内存去存储它
print(d, id(d))
print(s, id(s))

s1 = 'hello, python'
e = s.capitalize()  # 会产生一个新的对象，开辟一个新的内存去存储它
print(e, id(e))  # 如果首字符不是字母，那么首字母不会转换成大写
print(s, id(s))
f = s1.capitalize()
print(f, id(f))
