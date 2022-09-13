# -*- coding:utf-8 -*-
# 作    者：Ailian
# 开发时间：2022/9/13 09:52


"""
· Python3.0以 Unicode 为内部字符编码。Unicode采用双字节16位来进行编号，可编 65536 个字符，采用十六进制 4 位表示一个编码
UTF（Unicode Transformation Format 的缩写）意为 Unicode 转换格式。UTF-8 是Unicode的一种变长字符编码。
    - u4e00-u9fa5（中文）
    - x3130-x318F（韩文）
    - xAC00-xD7A3（韩文）
    - u0800-u4e00（日文）

使用 ord() 函数可以输出 字符对应的 十进制编码
"""

print(ord("北"))
print(ord("京"))
print('\u5317')  # \u 指 Unicode， 5371 是16进制编码，输出 "北"
print('\u4EAC')  # 输出 "京"
print('\u5317\u4EAC')  # 输出 "北京"
