# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/6/18 上午9:12

import easygui as g

# 进入游戏
# g.msgbox(msg="嗨，欢迎来到小白猪的游戏世界！", title='小白猪的游戏世界')
# g.msgbox(msg="这是一个双人游戏，考验你们之间的默契度", title='小白猪的游戏世界')

# 猜数字游戏，考验朋友间的默契
"""
1. 两个人轮流输入一个数字（100以内的正整数），程序会自动判断你们两个人输入的数字是否相同
如果相同，则默契度为100%
如果两个数字相差的绝对值为 1，那么默契度为 90%
如果两个数字相差的绝对值为 [2,10]，那么默契度为 80%
如果两个数字相差的绝对值为 [11, 20]，那么默契值为 50%
如果两个数字相差的绝对值 大于 20， 那么默契值为 0
"""
# count = 0
# while count < 3:
# while 1:
#     try:
#         input_num1 = int(input("请输入第一个数字："))
#         if type(input_num1) == type(1):
#             while 1:
#                 try:
#                     input_num2 = int(input("请输入第一个数字："))
#                     if type(input_num2) == type(1):
#                         break
#                 except:
#                     print('输入错误，请重新输入！')
#             break
#     except:
#         print('输入错误，请重新输入！')
#     # count += 1
#
# # 判断两人之间的契合度
# if input_num1 == input_num2:
#     print('恭喜你们的默契度达到 100%，真是天造地设的一对！')
# elif abs(input_num1-input_num2) == 1:
#     print('恭喜你们的默契度达到 90%，真是难得知己！')
# elif 2 < abs(input_num1-input_num2) < 10:
#     print('恭喜你们的默契度达到 80%，真是不错的知己！')
# elif 11 < abs(input_num1-input_num2) < 20:
#     print('恭喜你们的默契度达到 50%，契合度有待提升呀！')
# elif abs(input_num1-input_num2) > 20:
#     print('恭喜你们的默契度达到 0%，你们的契合度几乎为零')


a = g.integerbox(msg="请输入第一个数字：", title='小白猪的游戏世界')
b = g.integerbox(msg="请输入第二个数字：", title='小白猪的游戏世界')

# 判断两人之间的契合度
if a == b:
    g.textbox('恭喜你们的默契度达到 100%，真是天造地设的一对！')
elif abs(a-b) == 1:
    g.textbox('恭喜你们的默契度达到 90%，真是难得知己！')
elif 2 <= abs(a-b) <= 10:
    g.textbox('恭喜你们的默契度达到 80%，真是不错的知己！')
elif 11 <= abs(a-b) <= 20:
    g.textbox('恭喜你们的默契度达到 50%，契合度有待提升呀！')
elif abs(a-b) > 20:
    g.textbox('恭喜你们的默契度达到 0%，你们的契合度几乎为零')
