# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/6/15 下午5:20

"""
try:
    检测范围
except Exception[as reason]:
    出现异常后（Exception）的处理代码
finally:
    无论如何都会被执行的代码

机制解释：
    如果 try 语句没有出现异常，那么会跳过 except 语句，执行 finally 语句
    如果 try 语句出现了异常，那么会执行 except 语句，执行完后，再执行 finally 语句
    因此 finally 语句是要放一些绝对会被执行的代码，不管 程序会不会错误 都会执行
"""

# 案例
"""
如果异常是发生在文件成功打开之后，那么python就会跳到except语句，那么try语句里面的 .close()语句没有被执行，
文件打开了但是并没有关闭，如果有对文件进行写入的话，但是没有执行关闭文件，程序崩溃了，这些数据只会保存在缓存区里面，不会写入到文件里面，这样肯定会不好

"""

try:
    f = open('../chap15-文件/小白猪.txt', 'w')
    print(f.write('我是一个王者！'))
    sum = 1 + '1'  #
    f.close()
except (OSError, TypeError):
    print('文件出错啦！🤡')