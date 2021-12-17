# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/11/25 下午4:14

"""
python中处理时间的模块有：time、datetime、calendar
在python中表示时间的方式：
    时间戳：10位整数位和乳沟小数位，例如 1637828282.0633159
    元组（struct_time)：含有9个元素的元组，例如
    格式化字符串：格式化的时间字符串，例如 "2021-11-25 16:21:50"
time模块：
    以元组(struct_time)为核心实现时间戳和格式化时间字符串的相互转换
    time模块是通过调用C库实现的，所以在有些平台上面是无法使用的，大部分接口和C标准库的time.h一致

datetime模块：
    以datetime类实例对象为核心时间时间戳和格式化时间字符串的相互转换

"""


import time
import datetime

# 一、time 模块
# 1. 时间戳转换为 格式化字符串
# ① 获取当前时间的 时间戳
stamp_time = time.time()

# ② 将时间戳转换为 元组（struct_time)
struct_time = time.localtime(time.time())

# ③ 将时间戳转换为 格式化时间字符
strf_time = time.strftime("%Y-%m-%d %H:%M:%S %w %y %I", time.localtime(time.time()))

# 2. 将格式化字符串转换为时间戳
# ① 将时间字符串转换为 元组（struct_time），元组格式要与 时间字符串的相同
time_str = '2021-11-25 17:08:58'
time_strf = time.strptime(time_str, '%Y-%m-%d %H:%M:%S')
# 结果：time.struct_time(tm_year=2021, tm_mon=11, tm_mday=25, tm_hour=17, tm_min=8, tm_sec=58, tm_wday=3, tm_yday=329, tm_isdst=-1)

# ② 将元组（struct_time）转换为 时间戳
time_samp = time.mktime(time.strptime(time_str, '%Y-%m-%d %H:%M:%S'))
# 结果：1637831338.0

# 3. 使用 time 模块获取当前日期和时间
# ① 获取当前日期（使用当前时间的 struct_time 作为缺省参数）
data_time = time.strftime("%Y-%m-%d")

# ② 获取当前时间（使用当前时间的 struct_time 作为缺省参数） time.localtime(time.time())
now_time = time.strftime("%H:%M:%S")


# 二、datetime 模块
"""
和 time 模块相比，datetime 模块是提供更直接易用的接口，功能更强大
datetime 模块提供了处理日期和时间的类，既有简单的方式，也有复杂的方式。虽然支持日期和时间算法，但其实重点是输出的格式化操作和更加有效的属性提取功能
"""
# 1. datetime 模块中定义的类
"""
datetime模块中定义的类（这些类的对象都是不可变的）
    datetime.date: 表示日期，常用的属性有 year、month、day
    datetime.time: 表示时间，常用的属性有 hour、minute、second、microsecond
    datetime.datetime: 表示日期时间
    datetime.timedelta: 表示两个date、time 和 datetime实例之间的时间间隔，最小单位可达微秒
    datetime.tzinfo: 时区相关对象的抽象基类，由time和datetime类使用
    datetime.timezone: 表示与UTC的固定偏移量
"""

# 2. 使用datetime模块中的datetime类将时间戳转换为格式化时间字符串




print(time_samp)
print(now_time)