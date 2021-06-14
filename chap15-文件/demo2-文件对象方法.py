# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/6/13 上午11:10


"""
拿到文件对象后，可以用文件对象的一些方法对文件进行操作
    .close()：关闭文件
    .read(size=1-)：从文件读取size个字符，当未给定size或者给定负值时，读取剩余的所有字符，然后作为字符串返回
    .readline()：以写入模式打开，如果文件存在，则在文件末尾追加
    .write(str)：将字符串"str"写入文件中
    .writelines(seq)：向文件写入字符串序列seq，seq应该是一个返回字符串的可迭代对象
    .seek(offset, from)：在文件中移除文件指针，从from（0代表文件起始位置，1代表当前位置，2代表文件末尾）偏移offset个字节
    .tell()：返回当前在文件中的位置
"""

f = open('/Users/developer/Desktop/常用命令.txt', 'r')
# t = f.read()
# print(t)

# print(f.read(5))  # 按字符读，utf-8中一个中文占 3 个字节，gbk中一个中文占 2 个字节
# print(f.readline(5))  # 按一行一行读
#
# print(f.tell())
#
# print(f.seek(0, 0))
# print(f.readline(5))
# print(f.tell())

# for each_line in f: # 按行读取文件内容
#     print(each_line)

f1 = open('/Users/developer/Desktop/test.txt', 'w+')
add = f1.write('我爱玩')  # 写入字符串，此时并未真正写入文件里面，而是写入内存中
print(add)
print(f1.read())  # 此时使用read()是读取不到内容的，需要先关闭文件，然后再次打开才能读取到内容
f1.close()  # 关闭文件
f1 = open('/Users/developer/Desktop/test.txt', 'r')
print(f1.read())