import datetime
# from datetime import timedelta
from datetime import datetime, timedelta

# # 定义日期时间字符串
# date_str = "2021-10-01 12:00:00"
# 1.指定日期转时间戳
# # 将字符串转换为日期时间对象
# date = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
#
# # 转换为时间戳（以秒为单位）
# timestamp = int(date.timestamp())
# print("日期转时间戳:", timestamp)
#
# # 3.当前日期转时间戳
# # 获取当前日期时间
# now = datetime.datetime.now()
# print(now)
#
# # 转换为时间戳
# timestamp = int(now.timestamp())
# print("当前日期转时间戳:", timestamp)
#
# # 4.当前时间戳转换成日期
# # 获取当前时间戳
# current_timestamp = datetime.datetime.now().timestamp()
#
# # 转换为日期时间对象
# date = datetime.datetime.fromtimestamp(current_timestamp)
#
# # 格式化输出
# formatted_date = date.strftime("%Y-%m-%d %H:%M:%S")
# print("当前时间戳转日期:", formatted_date)

# 5.指定日期加减天数
# 定义初始日期
date_str = "2025-02-28"
initial_date = datetime.strptime(date_str, "%Y-%m-%d")

# 加 10 天
new_date_after_addition = initial_date + timedelta(days=180)

# 减 5 天
new_date_after_subtraction = initial_date - timedelta(days=5)

print("初始日期:", initial_date.strftime("%Y-%m-%d"))
print("加 10 天:", new_date_after_addition.strftime("%Y-%m-%d"))
print("减 5 天:", new_date_after_subtraction.strftime("%Y-%m-%d"))

# def