# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/6/15 下午5:38


"""
自己引出一个异常

"""

try:
    f = open('../chap15-文件/小白猪.txt', 'w')
    print(f.write('我是一个王者！'))
    # sum = 1 + '1'  #

    f.close()
except (OSError, TypeError):
    print('文件出错啦！🤡')

try:
    m = 3/0
except:
    raise ZeroDivisionError('除数为零的异常！')