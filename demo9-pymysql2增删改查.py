# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/5/15 下午7:37

import pymysql

# 建立连接
conn = pymysql.connect(host='localhost', user='root', password='@12345678', db='test_UI', charset='utf8')

# 拿游标
cur = conn.cursor(pymysql.cursors.DictCursor)
# pymysql.cursors.DictCursor 会将查询出来的结果转成字典的格式

# 执行SQL
# 增、删、改、查
# ① 增
sql_add = 'insert into user(id, name) values(%s, %s)'
cur.execute(sql_add, (7, '小舞'))
# cur.executemany(sql_add, [(6, '小舞'), (7, '小舞1')])  # 传多个值
# 提交事务
# conn.commit()

# ② 删
sql_delete = 'delete from user where id=%s'
cur.execute(sql_delete, 7)
# 提交事务
conn.commit()

# ③ 改
sql_update = 'update user set name=%s where id=%s'
cur.execute(sql_update, ('小君', 1))
# 提交事务
conn.commit()

# ④ 查
# 查
sql_check = 'select * from user'
cur.execute(sql_check)
# data = cur.fetchall()  # 重复执行,后面的拿的数据会为空
# # data = cur.fetchall()  # []
# print(data)

# 相对绝对位置移动
cur.scroll(2, mode='absolute')  # 跳过前面2行，从第3行开始取数据
print(cur.fetchone())

# 相对当前位置移动
cur.scroll(1, mode='relative')  # 从当前位置（第3行），移动一行，从第5行开始取数据
print(cur.fetchall())

# 关闭游标
cur.close()