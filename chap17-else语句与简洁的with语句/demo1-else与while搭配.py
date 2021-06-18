# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/6/15 下午5:50


def showMaxFactor(num):
    count = num // 2  # 11->5
    while count > 1:
        if num % count == 0:
            print('%d最大的约数是%d' % (num, count))
            break  # 使用break语句，就会终止循环，不会运行else语句；不使用break语句，就会运行else语句
        count -= 1
    else:
        print('%d是素数！' % num)


num = int(input('请输入一个数字：'))
showMaxFactor(num)

