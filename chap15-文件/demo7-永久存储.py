# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/6/14 下午1:53

"""
从文件中读取字符串是很简单的，但是要读取数值是很难的
python有一个标准模块 pickle 模块，泡菜的意思，可以将列表、字典等复杂的数据类型转换成二进制
几乎可以把python所有的对象转换成 二进制形式去存放，这个过程称之为 pickling （存放）
从二进制的形式转换成对象的过程，称之为 unpickling （读取）

存储之后，随时随地都可以用

使用场景：
    当固定的数据量很小的时候没有多大必要写到 磁盘中
    当固定的数据量很大的时候，把它写到磁盘中就会显得代码很简洁，而且也不会占用很大的内存

"""

import pickle

my_list = [12, 3.14, '小白猪', ['another list']]
# 将 my_list 永久保存起来，即写入磁盘中
pickle_file = open('my_list.pkl', 'wb')  # wb 以二进制的形式写入
pickle.dump(my_list, pickle_file)  # 把my_list 倒到 pickle_file 里面
pickle_file.close()  # 关闭文件，否则文件会一直在缓存区打开

pickle_file = open('my_list.pkl', 'rb')  # rb 以二进制形式读取
my_list2 = pickle.load(pickle_file)
print(my_list2)
pickle_file.close()
