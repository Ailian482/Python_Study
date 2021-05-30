# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/5/16 下午7:10

"""
split(): 从字符串的左边开始劈分，默认的劈分字符是空格字符串，返回的值都是一个 列表。
    以通过参数sep指定劈分字符串是劈分符
    通过参数maxsplit指定劈分字符串时的最大劈分次数，在经过最大次劈分次数之后，剩下的子串会单独做为一部分
rsplit(): 从字符串的右边开始劈分，默认的劈分字符是空格字符串，返回的值都是一个 列表。
    以通过参数sep指定劈分字符串是劈分符
    通过参数maxsplit指定劈分字符串时的最大劈分次数，在经过最大次劈分次数之后，剩下的子串会单独做为一部分
"""

s = 'hello world Python'
lst = s.split()
print(lst)

s1 = 'hello|world|Python'
lst1 = s1.split(sep='|')
print(lst1)
print(s1.split(sep='|', maxsplit=1))
print(s1.split(sep='|', maxsplit=3))

print(s1.rsplit(sep='|', maxsplit=1))


