# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/6/17 下午5:29

import easygui as g
import sys

while 1:
    g.msgbox("嗨，欢迎进入第一个界面小游戏!")
    msg = "请问你想知道学霸是如何养成的吗？"
    title = "小游戏互动"
    choices = ['琴', '棋', '书', '画']

    choice = g.choicebox(msg=msg, title=title, choices=choices)
    # note that we convert choice to string, in case
    # the user cancelled the choice, and we got none
    g.msgbox('你的选择是：' + str(choice), '结果')

    msg1 = '你希望小游戏重新开始吗？'
    title1 = '请选择'

    if g.ccbox(msg1, title1):
        pass
    else:
        sys.exit(0)  # user choice Cancel

