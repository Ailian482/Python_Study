# -*- coding:utf-8 -*-
# 作    者：Ailian
# 开发时间：2022/9/14 13:48


"""
- 语法结构
    for 循环变量 in 遍历对象:
        语句块1
    else:
        语句块2
- else语句只在循环正常结束后才执行
- 通常与break和continue语句一起使用
"""
# 计算1-10之间的累加和
s = 0
for i in range(1, 11):
    s += i  # 相当于s = s+i

print("1-10之间的累加和为：", s)
