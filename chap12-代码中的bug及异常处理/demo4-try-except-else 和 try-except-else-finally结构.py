# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2022/5/16 上午10:51

"""
try...except...else 结构
    如果 try 块没有抛出异常，则执行 else 块，如果 try 中出现异常，在执行 except 块
try...except...else...finally 结构
    finally 块，无论程序是否出错都会被执行，能用来释放 try 块中申请的资源
"""

try:
    a = int(input('请输入第一个整数：'))
    b = int(input('请输入第二个整数：'))
    result = a/b
except BaseException as e:
    print('出错了！')
    print(e)
else:
    print('结果为：', result)
finally:
    print('谢谢你的使用！')
print('程序结束')