# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/10/28 下午4:27

# 导入
import xlrd


# xlrd 读取文件
"""可以读取 .xls 和 .xlsx"""
xlrd_path = r"/Users/developer/Desktop/副本技术部-团建人数姓名+身份证统计表(1).xlsx"
xlrd_open = xlrd.open_workbook(xlrd_path)

# 获取工作表
# xlrd_get_sheets = xlrd_open.sheets()
# 通过 sheet 表名
xlrd_get_sheet_by_name = xlrd_open.sheet_by_name("团建人数统计表")
# 通过 sheet 表的下标
xlrd_get_sheet_by_index = xlrd_open.sheet_by_index(0)

# 获取单元格的值
unit_value = xlrd_get_sheet_by_name.cell_value(4, 1)

# 获取某一行的所有值，并且组成一个列表
row_values = xlrd_get_sheet_by_name.row_values(4)

# 获取某一列的所有值，并且组成一个列表
col_values = xlrd_get_sheet_by_name.col_values(0)

for cell in row_values:
    print(cell)

print(row_values)
print(col_values)