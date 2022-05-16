# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2022/5/16 上午10:00
lst = [
    {'rating': [9.7, 206], 'id': '2052', 'type': ['犯罪', '剧情'], 'title': '肖申克的救赎', 'actors': ['蒂姆·罗宾斯','摩根·弗里曼']},
    {'rating': [9.6, 152], 'id': '1546', 'type': ['爱情', '剧情', '同性'], 'title': '霸王别姬', 'actors': ['张国荣','张丰毅', '葛优', '巩俐']},
    {'rating': [9.5, 155], 'id': '2720', 'type': ['爱情', '剧情'], 'title': '阿甘正传', 'actors': ['汤姆·汉克斯','罗宾·怀特']}
]

name = input('请输入你要查询的演员：')
for item in lst:  # 遍历列表 --> {}  item 是一个又一个的字典
    act_list = item['actors']  # 得到演员的一个列表
    # print(act_list)

    # for movie in item:  # 遍历字典，得到的 movie 是一个字典中的 key
    #     print(movie)

    # for actor in act_list:
    #     # print(actor)
    #     if name in actor:
    #         print(name,'出演了', item['title'])

    if name in act_list:
        print(name, '出演了', item['title'])
    # print('>>>>>>>>>>>>>>>>>>>>>>>>>>')
