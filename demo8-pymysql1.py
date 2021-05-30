# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/5/12 下午6:34

import pymysql

# 数据库连接设置
conn = pymysql.connect('localhost', user='root', password='@12345678', db='test_UI', charset='utf8')
# 生成游标，用来执行SQL语句
cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
"""
# 编写SQL语句
sql0 = 'insert into user (id, name) values (%s, %s)'
data = [(2, "小黑"), (3, "小黄"), (4, "小朱"), (5, "小林")]
# sql2 = 'drop table user_1'  # 删除表user_1
# 执行SQL语句
for i in data:
    cur.execute(sql0, i)
# cur.execute(sql2)
# 提交事务
conn.commit()
"""

# 执行查询语句
sql1 = 'select * from user'
cur.execute(sql1)
# 获取数据
data = cur.fetchall()
print(data)
# 把结果转成 json格式

import json
jsonData = json.dumps(data, indent=4, ensure_ascii=False)
print(jsonData)

# 关闭游标
cur.close()
# 关闭连接
conn.close()


"""
execute()：执行单条语句
executemany()：执行多条语句
fetchone()：获取第一条
fetchall()：获取所有行
fetchmany(size)：获取几(size)行
scroll(num,mode)：移动游标
rowcount：计算corsor的行数
description：返回字段的信息
close()：关闭游标
"""
