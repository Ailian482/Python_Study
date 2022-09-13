# -*- coding:utf-8 -*-
# 作    者：Ailian
# 开发时间：2022/9/13 09:17

"""
基本的输出函数 print()
    - print函数的完整语法格式
      print(self, *args, sep=' ', end='\n', file=None): # known special case of print
        - *args 表示可以输入很多个值
        - sep=' ' 表示多个值之间使用 空格 进行分割
        - end='\n' 表示输出完一次之后就 换行
      print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

使用 print() 函数进行复杂输出
    · 多条 print() 输出到一行显示
        - 只需要将 end 的值设置成其他字符，例如：end=" "
    · 使用连接符连接多个字符串
        - 使用 "+" 连接数值和其他数据类型时，系统默认为加法计算，程序报错，解决方案，可将数值作为字符串来处理
"""

print('北京欢迎你！', end="--->")
print('欢迎你！')
# 输出结果：北京欢迎你！--->欢迎你！
