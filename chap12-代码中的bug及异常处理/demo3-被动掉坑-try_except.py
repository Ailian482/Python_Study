# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2022/5/16 上午10:36

"""
被动掉坑：程序代码逻辑没有错，只是因为用户错误操作或者一些"例外情况"而导致程序崩溃
"""

# 输入两个整数并进行除法运算
try:
    a = int(input('请输入第一个整数：'))
    b = int(input('请输入第二个整数：'))
    result = a/b
    print('结果为：', result)
except ZeroDivisionError:
    print('对不起，除数不允许为 0')
except ValueError:
    print('只能输入数字串')

print('程序结束')