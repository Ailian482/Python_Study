# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/5/19 上午9:48

"""
字符串是不可变序列，
    不具备增、删、改等操作
    切片操作将产生新的对象
"""

# s = 'hello,Python'
# s1 = s[:5]
# s2 = s[6:]
# s3 = '!'
# newstr = s1 + s3 + s2
# print(newstr)
#
# print('-----------------')
# print(id(s))
# print(id(s1))
# print(id(s2))
# print(id(s3))
# print(id(newstr))
#
# print('--------切片[start:end:step]---------')
# print('--------切片[开始:结束:步长]---------')


# while True:
#     try:
#         a = input()
#         while(len(a) >= 8):
#             print(a[:8])
#             a = a[8:]
#         if len(a) > 0:
#             print(a + '0'*(8 - len(a)))
#     except:
#         break


while True:
    try:
        l = input()
        for i in range(0, len(l), 8):
            print("{0:0<8s}".format(l[i:i+8]))
    except:
        break
