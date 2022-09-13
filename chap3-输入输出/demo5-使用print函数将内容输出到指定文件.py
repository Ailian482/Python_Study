# -*- coding:utf-8 -*-
# 作    者：Ailian
# 开发时间：2022/9/13 11:21


fp = open('node.txt', 'w')  # 打开文件，w-->write
print("北京欢迎你！", file=fp)  # 输出到文件
fp.close()  # 关闭文件
