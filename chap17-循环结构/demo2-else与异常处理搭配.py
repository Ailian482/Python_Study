# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/6/16 上午9:15


"""
要么怎样，要么不怎样
干完了能怎样，干不完就别想怎样
没有问题那就干吧

else与try语句搭配时：
    如果try语句里面有代码出错了，那么就会走except语句，不会再走else语句
    如果try语句里面代码没有出错，那么就不会走 except 语句，而是直接走 else语句


"""

try:
    # int('zbc')  # 异常
    int('123')  # 正常
except ValueError as reason:
    print('出错啦:' + str(reason))
else:
    print('没有任何异常')