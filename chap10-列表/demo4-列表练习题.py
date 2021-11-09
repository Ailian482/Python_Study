# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/8/22 下午10:07

# 1. 使用列表推导式完成 把字典中的键值对转换成 a = b 的数据格式
"""
字典 {'user':'admin', 'age':20, 'phone':'133'}
列表 ['user=admin', 'age=20', 'phone=133']
"""
var_dict = {'user': 'admin', 'age': 20, 'phone': '133'}
for i in var_dict:
    print(var_dict[i])


from selenium import webdriver
# Chrome 浏览器
driver = webdriver.Chrome()
driver.get("https://www.csdn.net/")

# 不自动关闭浏览器
option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)

# 将option作为参数添加到 Chrome 中
driver = webdriver.Chrome(options=option)
driver.get("https://www.csdn.net/")