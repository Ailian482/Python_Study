# -*- coding:utf-8 -*-
# 作    者：Ailian
# 开发时间：2022/9/13 12:44


"""
- 语法结构：
    variable = input()
- 注意事项
    无论用户输入的数字或是字符，input()函数统一按照字符串类型输出
    想要接收整型的数字并保存到变量num中，代码如下
    num = int(input('请输入您的幸运数字：'))
"""

name = input('请输入您的姓名:')
print('我的姓名是:' + name)

num = int(input('请输入您的幸运数字：'))
print('您的幸运数字为：', num)