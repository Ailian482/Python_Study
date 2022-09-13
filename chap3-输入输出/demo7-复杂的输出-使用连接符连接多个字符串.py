# -*- coding:utf-8 -*-
# 作    者：Ailian
# 开发时间：2022/9/13 12:36

print(1234)  # 直接输出整数
print(3.14)  # 直接输出浮点数（带小数点的数）
print(1, 2, 3, 4)  # 使用逗号连接要输出的数字，之间使用空格连接：1 2 3 4
print(192, 168, 1, 1, sep='.')  # 使用间隔符 . 进行连接，数值之间用 . 进行分隔：192.168.1.1
# print('北京欢迎你' + 2022)  # TypeError: can only concatenate str (not "int") to str
print('北京欢迎你' + '2022')  # 北京欢迎你2022
