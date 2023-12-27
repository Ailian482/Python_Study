# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/10/28 下午4:49

import pandas as pd
from pandas import DataFrame
from pandas import ExcelWriter

# 打开Excel文件，并获取sheet表
""" 可以用来读取 .xls 和 .xlsx 文件"""
# old_file = "/Users/developer/Documents/系统相关导入导出模板/员工信息导入模板的副本.xls"
# p_path = r"/Users/developer/Desktop/技术部-团建人数姓名+身份证统计表.xlsx"
p_path = r"/Users/tehang/Desktop/pythonTest.xlsx"
p_open = pd.read_excel(p_path, sheet_name="Sheet1")  # 打开Excel表

# 创建文件
c_file = pd.DataFrame([])
c_file.to_excel(r"/Users/developer/Desktop/test.xlsx")
# 写入数据, 根据字典创建，读取CSV或者txt文件来创建

# 1. 根据字典创建
datas = {
    'name':["阿君", "阿蛮", "阿离"],
    'birthday':["1996-11-04", "1996-11-04", "1996-11-04"],
    'corp':["小白猪的游戏世界", "小黑猪的游戏世界", "王者的世界"]
}

c_file1 = pd.DataFrame(datas)

# # DataFrame的行索引是 index，列索引是 columns，我们可以在创建DataFrame时指定索引的值：
# c_file2 = pd.DataFrame(datas, index=[1, 2, 3], columns=['name', 'birthday', 'corp', 'phone'])
#
# # 使用嵌套字典也可以创建DataFrame，此时外层字典的键作为列，内层键作为索引
# d_data = {'name':{2000:'小朱', 2001:'小白'}, 'phone':{2001:13632296400, 2000:13632296401, 2002:13632296402}}
# c_file3 = pd.DataFrame(d_data)
#
# # 可以用index，columns，values来访问DataFrame的行索引，列索引以及数据值，数据值返回的是一个二维的 ndarray
# c_file2_values = c_file3.values
#
# # 读取文件
# # 读取生成DataFrame最常用的是 read_csv,read_table方法。
#
#
# print(c_file2_values)
# # 保存文件
# c_file1.to_excel(r"/Users/developer/Desktop/test1.xlsx")

# 获取单元格的值
# pandas 读取Excel文件后将它转换为数据框对象，解析内容的方法基本是 pandas 体系中的知识点，.iloc()，.loc()、.ix()等
# print(c_file1.iloc[0:4, [0]])
# print(c_file1.loc['b'])
# print(c_file1.ix['a', 'a'])  # 有些版本取消了 ix，可以用 iat


# # 新增行
# name = '阿君'
# department = '总部'
# phone = int('10162291001')
# # print(type(phone))
