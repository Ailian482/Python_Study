# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/5/19 上午9:08

"""
替换replace()：
    第一个参数指定要替换的子串，第二个参数指定替换子串的字符串，该方法返回替换后得到的字符串，
    替换后原字符串不发生变化，调用该方法时可以通过第3个参数指定最大替换次数
合并join()：
    将列表或者元组或字符串的元素合并成一个字符串，前面需要一个字符串将列表或者元组或字符串里面的元素拼接起来
"""

s = 'hello,Python'
print(s.replace('Python', 'Java'))
print(s)  # 替换后原字符串不变

s1 = 'hello,Python,Python,Python,Python,Python'
print(s1.replace('Python', 'Java', 3))  # 3 指定最大替换次数

lst = ['hello', 'python', 'I', 'love', 'Python']
print('|'.join(lst))
print(' '.join(lst))

lst1 = ('hello', 'python', 'I', 'love', 'Python')
print('|'.join(lst))
print(' '.join(lst))

lst3 = 'Python'
print('*'.join(lst3))

lst2 = ['hello,',  'python', 'I', 'love', 'Python']
print(' '.join(lst2).title())
