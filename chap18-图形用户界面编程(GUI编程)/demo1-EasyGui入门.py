# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/6/16 上午9:45


"""
图形用户界面：EasyGUI
EasyGUI官网：
    - http://easygui.sourceforge.net/

官方的教学文档：
    - easygui-docs-0.96_docs/tutorial/index.html
    - http://easygui.sourceforge.net/sourceforge_site_as_of_2014_11_21/download/version_0.96/index.html  # 下载地址
    - http://bbs.fishc.com/thread-46069-1-1.html
查看easygui的源代码和所有的 方法
    - easygui-docs-0.96_docs/epydoc/index.html


建议：
    不要在 IDLE 上运行 EasyGui
    EasyGui是运行在 Tkinter 上并拥有自身的事件循环，而 IDLE 也是 Tkinter 写的一个应用程序并也拥有自身的事件循环
    因此当两者同时运行的时候，有可能会发生冲突，并且带来不可预测的结果，因此如果你发现你的 EasyGui 程序有这样的问题，请尝试在 IDLE 外去运行你的程序
"""

# import easygui   # 这种方法导入进来调用函数的时候需要写很长的名字
# easygui.msgbox("嗨，小白猪")


# 把 easygui所有的包都导进来

# from easygui import *   # 使用这种方法导入会有一个问题，如果原本有同名函数，那么就会有可能同名函数之间会相互覆盖
# msgbox("嗨，小白猪！")

import easygui as e   # 建议使用这种方法，给包名起别名
e.msgbox("嗨，小白猪！")

