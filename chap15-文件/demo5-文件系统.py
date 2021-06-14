# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/6/13 下午5:46

import os

"""
os模块
有了os模块，我们不需要关心什么操作系统下使用什么模块，os模块会帮你选择正确的模块并调用

我们所知道的常用操作系统有：Windows、Linux、Mac OS、Unix等，这些操作系统底层对于文件系统的访问工作原理是不一样的，
因此你可能需要针对不同的操作系统使用哪些文件系统模块。。。这样的做法是非常不友好和麻烦的，
因为这样就意味着当你的程序运行环境一改变，你就要相应的去修改大量的代码来应付
"""

"""
os.getcwd() 返回当前工作目录的绝对路径
os.chdir 改变工作目录，参数要是 字符串
os.listdir(path='.') 列出指定目录下的文件名（'.'表示当前目录，'..'表示上一级目录）
os.mkdir(path) 创建目录单层目录，如该目录已存在则抛出异常
os.mkdir('boy')  # FileExistsError: [Errno 17] File exists: 'boy'
os.makedirs(path) 创建多层目录，如该目录已存在则抛出异常
os.remove(path) 删除文件
os.rmdir(path) 删除单层目录
os.removedirs(path) 删除层级空目录
os.rename(old, new) 将文件old重命名为new
os.system(command) 运行系统的shell命令
os.curdir  指代当前目录（'.'）
os.pardir 指代上一级目录（'..'）
os.sep 输出操作系统特定的路径分隔符（Win下'\\'，Linux下'/'）
os.linesep 当前平台指定的行终止符（Win下'\r\n'，Linux下'\n'）
os.name 指代当前使用的操作系统（包括：'posix'、'nt'、'mac'、'os2'、'ce'、'java'）
"""


# os.getcwd() 返回当前工作目录的绝对路径
print(os.getcwd())

# os.chdir 改变工作目录，参数要是 字符串
os.chdir('/Users/developer/Documents/Python_Study/chap15-文件/boy')
print(os.getcwd())

# os.listdir(path='.') 列出指定目录下的文件名（'.'表示当前目录，'..'表示上一级目录）
print(os.listdir('.'))

# os.mkdir(path) 创建目录单层目录，如该目录已存在则抛出异常
os.chdir('/Users/developer/Documents/Python_Study/chap15-文件')
print(os.getcwd())
# os.mkdir('boy')  # FileExistsError: [Errno 17] File exists: 'boy'
os.mkdir('小朱')
f = open('./小朱/test.txt', 'w')
f.close()

# os.makedirs(path) 创建多层目录，如该目录已存在则抛出异常
os.makedirs('小猪/🐷')

# os.remove(path) 删除文件
os.remove('./小朱/test.txt')

# os.rmdir(path) 删除单层目录
os.rmdir('./小朱')

# os.removedirs(path) 删除层级空目录
os.removedirs('小猪/🐷')

# os.rename(old, new) 将文件old重命名为new


# os.system(command) 运行系统的shell命令
os.system('expr 2 + 3')
os.system('pwd')

# os.curdir  指代当前目录（'.'）
print(os.curdir)
print(os.listdir(os.curdir))  # 查看当前目录下有哪些文件和目录

# os.pardir 指代上一级目录（'..'）
print(os.pardir)

# os.sep 输出操作系统特定的路径分隔符（Win下'\\'，Linux下'/'）
print(os.sep)

# os.linesep 当前平台指定的行终止符（Win下'\r\n'，Linux下'\n'）
print(os.linesep)

# os.name 指代当前使用的操作系统（包括：'posix'、'nt'、'mac'、'os2'、'ce'、'java'）
print(os.name)
