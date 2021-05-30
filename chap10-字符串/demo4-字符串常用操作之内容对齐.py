# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/5/16 下午5:27

"""
center(): 居中对齐，第1个参数指定宽度，第2个参数指定填充符，第2个参数是可选的，默认是空格，如果设置宽度小于实际宽度则返回原字符串
ljust(): 左中对齐，第1个参数指定宽度，第2个参数指定填充符，第2个参数是可选的，默认是空格，如果设置宽度小于实际宽度则返回原字符串
rjust(): 右中对齐，第1个参数指定宽度，第2个参数指定填充符，第2个参数是可选的，默认是空格，如果设置宽度小于实际宽度则返回原字符串
zfill(): 右对齐，左边用0填充，该方法只接收一个参数，用于指定字符串的宽度，如果指定的长度小于等于字符串本身的长度，则返回字符串本身

"""
s = 'hello,Python'
print(s.center(20, '*'))
print(s.center(13, '*'))
print(s.center(12, '*'))
print(s.center(10, '*'))

print(s.ljust(20, '*'))
print(s.ljust(13, '*'))
print(s.ljust(12, '*'))
print(s.ljust(10, '*'))

print(s.rjust(20, '*'))
print(s.rjust(13, '*'))
print(s.rjust(12, '*'))
print(s.rjust(10, '*'))

print(s.zfill(20))
print(s.zfill(13))
print(s.zfill(12))
print(s.zfill(10))
