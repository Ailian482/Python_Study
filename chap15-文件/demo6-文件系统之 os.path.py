# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/6/14 上午2:22


"""
os.path.basename(path)  去掉目录路径，单独返回文件名，没有文件，会把最后一个目录当作文件名返回
os.path.dirname(path)  去掉文件名，单独返回目录路径
os.path.join(path1[path2[, ...]])  将path1，path2等组合成一个路径名
os.path.split(path)  分割文件名与路径，返回（f_path, f_name)元组，如果完全使用目录，他会将最后一个目录作为文件名分割，且不会判断文件或者目录是否存在
os.path.splitext(path)  分离文件名与扩展名，返回（f_name, f_extension）元组
os.path.getsize(file)  返回指定文件的尺寸，单位是字节，如果没有指定路径，那么默认是当前路径
os.path.getatime(file)  返回指定文件最近的访问时间的时间戳（浮点型秒数，可用time模块的gmtime()或者localtime()换算）
os.path.getctime(file)  返回指定文件的创建时间（浮点型秒数，可用time模块的gmtime()或者localtime()换算）
os.path.getmtime(file)  返回指定文件最新的修改时间（浮点型秒数，可用time模块的gmtime()或者localtime()换算）
os.path.exists(path)  判断指定路径（目录或者文件）是否存在，返回 True或者False
os.path.isabs(path)  判断指定路径是否为绝对路径，返回 True或者False
os.path.isdir(path)  判断指定的路径是否存在且是一个目录
os.path.isfile(path)  判断指定的路径是否存在且是一个文件
os.path.islink(path)  判断指定的路径是否存在且是一个符号链接
os.path.ismount(path)  判断指定的路径是否存在且是一个挂载点（windows的C盘，E盘，D盘等这些就是挂载点）
os.path.samefile(path1, path2)  判断path1和path2是否指向同一个文件
"""

import os
import time


# os.path.basename(path)  去掉目录路径，单独返回文件名，没有文件，会把最后一个目录当作文件名返回
print(os.path.basename('chap15-文件/demo1-什么是文件？.py'))

# os.path.dirname(path)  去掉文件名，单独返回目录路径
print(os.path.dirname('chap15-文件/demo1-什么是文件？.py'))

# 获取指定路径下所有子文件的名称
print(os.listdir(os.path.dirname('/Users/tehang/Python_Study/chap15-文件/demo1-什么是文件？.py')))

# os.path.join(path1[path2[, ...]])  将path1，path2等组合成一个路径名
print(os.path.join('A', 'B', 'C'))

# os.path.split(path)
# 分割文件名与路径，返回（f_path, f_name)元组，如果完全使用目录，他会将最后一个目录作为文件名分割，且不会判断文件或者目录是否存在
# 返回的 f_name 永远都不会包含斜杠「/」，如果这个路径是以 斜杠「/」结尾，那么返回 f_name 为空。
print(os.path.split('A/B/sexy.py'))
print(os.path.split('A/B/'))
print(os.path.split(__file__))  # 返回当前目录下的 目录和文件名（f_path, f_name）

# os.path.splitext(path)  分离文件名与扩展名，返回（f_name, f_extension）元组
print(os.path.splitext('A/B/C/sexy.avi'))

# os.path.getsize(file)  返回指定文件的尺寸，单位是字节，如果没有指定路径，那么默认是当前路径
print(os.getcwd())
print(os.path.getsize('boy/boy_1.txt'))

# os.path.getatime(file)  返回指定文件最近的访问时间的时间戳（浮点型秒数，可用time模块的gmtime()或者localtime()换算）
print(time.gmtime(os.path.getatime('boy/boy_1.txt')))
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getatime('boy/boy_1.txt'))))

# os.path.getctime(file)  返回指定文件的创建时间（浮点型秒数，可用time模块的gmtime()或者localtime()换算）
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getctime('boy/boy_1.txt'))))

# os.path.getmtime(file)  返回指定文件最新的修改时间（浮点型秒数，可用time模块的gmtime()或者localtime()换算）
# f = open('boy/boy_1.txt', 'a')
# print(f.write('a'))
# print(f.write(''))
# f.close()
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime('boy/boy_1.txt'))))

# os.path.exists(path)  判断指定路径（目录或者文件）是否存在，返回 True或者False


# os.path.isabs(path)  判断指定路径是否为绝对路径，返回 True或者False
print(os.path.isabs('./boy'))  # False
print(os.path.isabs('/Users/developer/Documents/Python_Study/chap15-文件/demo1-什么是文件？.py'))  # True

# os.path.isdir(path)  判断指定的路径是否存在且是一个目录
print(os.path.isdir('./boy'))  # True
print(os.path.isdir('./boy/boy_1.txt'))  # False
print(os.path.isdir('./boy1'))  # False

# os.path.isfile(path)  判断指定的路径是否存在且是一个文件
print(os.path.isfile('./boy/boy_1.txt'))  # True
print(os.path.isfile('./boy'))  # False

# os.path.islink(path)  判断指定的路径是否存在且是一个符号链接


# os.path.ismount(path)  判断指定的路径是否存在且是一个挂载点（windows的C盘，E盘，D盘等这些就是挂载点，Mac的是 '/'）
print(os.path.ismount('/'))  # True
print(os.path.ismount('/Users'))  # False

# os.path.samefile(path1, path2)  判断path1和path2是否指向同一个文件

import pickle

pickle_file = open('my_list.pkl', 'rb')
my_list = pickle.load(pickle_file)
print(my_list)
pickle_file.close()
