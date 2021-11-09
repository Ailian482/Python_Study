> 为了进一步带大家了解各个库的异同，从而在不同场景下可以灵活使用，本文将横向比较7个可以操作 Excel 文件的常用模块，在比较各模块常用操作的同时进行巩固学习！

## 首先整体把握一下不同库的特点
- 1. xlrd、xlwt、xlutils各自的功能有局限性，但三者互为补充，覆盖了 Excel 尤其是 .xls 文件的操作。
     xlwt 可以生成 .xls 文件，xlrd 可以读取已存在的 .xls 文件，xlutils 连接 xlrd 和 xlwt 两个模块，使用户可以同时读写一个 .xls 文件。
     简单来说，xlrd 负责读、xlwt 负责写、xlutils 负责辅助和衔接。
- 2. xlwings 能够非常方便的读写 Excel 文件中的数据，并且能够进行单元格格式的修改
- 3. XlsxWriter 是一个用来写 .xls文件格式的模块。可以写文本、数字、公式并且支持单元格格式化、图片、图表、文档配置、自动过滤等特性。但是不能用来读取和修改Excel文件
- 4. openpyxl "通过工作簿 workbook - 工作表 sheet - 单元格 cell"的模式对.xlsx文件进行读、写、改，并且可以调整样式。
- 5. pandas 是进行数据处理和分析的强大模块，有时可以用来自动化处理Excel

## 一、安装
``` bash
pip3 install xlrd
pip3 install xlwt
pip3 install xluitls
pip3 install xlwings
pip3 install xlsxwriter
pip3 install openpyxl
pip3 install pandas
```

## 二、导入模块
- 多数模块可以直接通过名字导入，有些模块约定成俗会使用缩写
```bash
import xlrd
import xlwt
import xlutils
import xlwings
import xlsxwriter
import openpyxl
import pandas
```
- xlutils模块是 xlrd 和 xlwt 之间的桥梁，最核心的作用是拷贝一份通过xlrd 读取到内存的 .xls对象，然后再拷贝对象上通过 xlwt 修改 .xls 表格的内容。xlutils 可以将xlrd 的Book对象复制转换为 xlwt 的Workbook对象，具体使用时通常导入的是模块中的copy子模块

## 三、读取Excel文件
### 3.1 获取文件
- 并不是所有的7个模块都可以读取 Excel 文件，而即使能读取Excel文件也要分不同后缀名进行讨论，具体如下
```
1. xlwt、xlutils、XlsxWriter 不能读取文件
2. xlrd 可以读取 .xls 和 .xlsx 文件
3. openpyxl 可以读取 .xlsx 文件
4. pandas 可以读取 .xls 和 .xlsx 文件
5. xlwings 可以读取 .xls 和 .xlsx 文件
```
下面使用两个大小均为 16 KB 的 .xls 和 .xlsx 文件进行测试