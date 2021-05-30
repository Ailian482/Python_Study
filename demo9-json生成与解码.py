# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/5/13 下午4:02

import json

data = [{'a': 1, 'c': 2, 'd': 3, 'b': 4, 'l': 5}, {'name': '小白', 'age': 18, 'grade': 6}]

shengcheng = json.dumps(data, ensure_ascii=True)
shengcheng1 = json.dumps(data, indent=4, sort_keys=True, separators=(',', ':'), ensure_ascii=False)
"""
dumps方法及相关参数说明：
    dumps是将一个Python数据结构转换成一个 json编码的字符串（即json格式的数据）
    第一个参数（data），是要序列化的对象
    indent：缩进的位数
    sort_keys：字典 key 按照从小到大排序输出
    separators：去掉逗号","和冒号":"后面的空格，使数据更加精准的输出，这里只能传入两个值 (',', ':')
    ensure_ascii：为False，中文原样输出；为True，输出ascii码
"""
print(shengcheng)
print(shengcheng1)

jsonData = '{"a":1,"b":4,"c":2,"d":3,"l":5}'
# jsonData = "{'a': 1, 'c': 2, 'd': 3, 'b': 4, 'l': 5}"  # 注意：要解码的json数据，其逗号和冒号后面不能有空格
# 报错：
    # obj, end = self.scan_once(s, idx)
    # json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)

jiema = json.loads(jsonData)   # 解码json格式文本
print(jiema)

