# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/6/4 上午10:12


"""
递归是什么？
    按照一定的原理分解出来，递归更能体现数学原理
    递归出结果比较慢

迭代是什么？
    后面的值等于前面两个数之和
    迭代出结果比较快

"""
"""
兔子繁殖：兔子出生两个月之后，就有繁殖能力，之后每个月能生下一对兔子，一年之后，会有多少对兔子
    1  2  3  4  5  6  7   8   9   10  11  12
    1  1  2  3  5  8  13  21  34  55  89  144
    n1 n2 n3
        
    1, n=1
    1, n=2
    F(n-1)+F(n-2), n>2
          
"""


def fab(n):  # 迭代
    n1 = 1
    n2 = 1
    n3 = 1
    if n < 0:
        print("输入错误！")
        return -1
    while n-2 > 0:  # 5-2=3  4-2=2
        n3 = n2 + n1  # 1+1=2  1+2=3
        n1 = n2  # 1  2
        n2 = n3  # 2  3
        n -= 1
    return n3


result = fab(35)
if result != -1:
    print('总共有%d对小兔崽子！' % result)


def fab_2(n):  # 递归
    if n < 1:
        print("输入错误！")
        return -1
    if n == 1 or n == 2:
        return 1
    else:
        return fab_2(n-1)+fab_2(n-2)


result_1 = fab_2(45)
if result_1 != -1:
    print('总共有%d对小兔崽子！' % result_1)



