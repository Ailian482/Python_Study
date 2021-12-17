# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/5/12 下午5:39

# 导入 mysql驱动
import mysql.connector

# 把password设置为你的 root 口令
conn = mysql.connector.connect(user='root', password="@12345678", database='test_UI')
"""
cursor = conn.cursor()
# 创建 user 表
# cursor.execute("create table user_1(id int(11) primary key, name varchar(20))")
# 插入一行记录，注意mysql的占位符是%s
cursor.execute('insert into user (id, name) values (%s, %s)', [1, 'Ailian'])

# 如果运行程序报下面这个错误，是因为主键不能重复
# raise errors.get_exception(packet)    mysql.connector.errors.IntegrityError: 1062 (23000): Duplicate entry '1' for key 'user.PRIMARY'

cursor.rowcount

# 提交事务
conn.commit()   # 执行insert into等操作需要 调用提交事务，但是执行 查询语句是不需要调用提交事务的
cursor.close()
"""

# 运行查询
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', (1,))
values = cursor.fetchall()
print(values)

# 关闭游标
cursor.close()
# 关闭mysql驱动
conn.close()
