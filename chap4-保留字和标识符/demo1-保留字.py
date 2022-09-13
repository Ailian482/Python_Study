# -*- coding:utf-8 -*-
# 作    者：Ailian
# 开发时间：2022/9/13 14:04

"""
保留字
    - 保留字区分大小写
    - 保留字的查看
保留字不能用作变量名称，即不能进行赋值
"""

import keyword

print(keyword.kwlist)
"""
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 
'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 
'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

"""
true = '真'
# True = '真' # SyntaxError: cannot assign to True
