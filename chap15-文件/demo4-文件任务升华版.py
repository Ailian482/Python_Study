# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/6/13 下午5:26

"""
把保存对话内容封装成一个函数

"""


def save_file(boy, girl, count):
    file_name_boy = '/Users/developer/Documents/Python_Study/chap15-文件/boy/boy_' + str(count) + '.txt'
    file_name_girl = '/Users/developer/Documents/Python_Study/chap15-文件/girl/girl_' + str(count) + '.txt'
    # 新建文件，打开文件
    boy_file = open(file_name_boy, 'w')
    girl_file = open(file_name_girl, 'w')
    # 把对话内容保存到文件
    boy_file.writelines(boy)
    girl_file.writelines(girl)


# 分割文件
def split_file(file_name):
    f = open(file_name)
    boy = []
    girl = []
    count = 1
    for each_line in f:
        if each_line[:6] != '======':
            # 我们这里进行字符串分割操作
            (role, line_spoken) = each_line.split("：", 1)
            if role == '小甲鱼':
                boy.append(line_spoken)
            if role == '小客服':
                girl.append(line_spoken)
        else:
            save_file(boy, girl, count)
            # 初始化 boy和girl 列表，不然会保存有上一次的对话内容
            boy = []
            girl = []
            count += 1
    save_file(boy, girl, count)
    f.close()


split_file('test.txt')

