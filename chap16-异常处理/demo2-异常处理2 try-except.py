# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/6/15 上午10:12

"""
让编程改变世界
异常检测可以使用 Try 语句来检测

try语句一旦出现异常，如果except语句没有对该类型异常进行处理的话，程序会正常报错，不能往下走流程了
try语句一旦出现异常，且except语句对该类型异常进行了处理，那么程序会走except语句里面的代码块，之后不会再走try语句里面的代码块，而且不会印象整个程序的运行

两种形式：
第一种形式
    try:
        检测范围
    except Exception[as reason]      # 备注：as reason，是加上一个 出错的原因
        出现异常后（Exception）的代码

第二种形式
    try:
        检测范围
    except:
        出现异常后（Exception）的代码

第三种形式：
    可以用多种exception来组合
"""

# 案例1
"""
打开一个不存在的文件，python会报错

"""

# f = open('小白猪.txt')
# print(f.read())
# f.close()  # FileNotFoundError: [Errno 2] No such file or directory: '小白猪.txt'

# 使用异常处理机制来处理这段程序，这样对用户来说也会比较的友好
try:
    f = open('小白猪.txt')
    print(f.read())
    f.close()
except OSError:
    print('文件出错啦！🤡')

"""
使用上面那段优化代码还是有不足的地方，因为文件出错有很多种可能（文件不存在，文件被毁坏，等等）
因此使用下面的代码会更加的详细
"""
try:
    sum = 1 + '1'   #
    f = open('小白猪.txt')
    # f = open('../chap15-文件/my_list.pkl')
    print(f.read())
    f.close()
except OSError as reason:
    print('文件出错啦！🤡\n错误的原因是：' + str(reason))
except TypeError as reason:
    print('类型出错啦！🤡\n错误的原因是：' + str(reason))

"""
将所有的异常类型都统一起来，不管try语句里面报了哪种类型都可以直接走except语句代码块
"""
try:
    sum = 1 + '1'   #
    f = open('小白猪.txt')
    # f = open('../chap15-文件/my_list.pkl')
    print(f.read())
    f.close()
except (OSError, TypeError):
    print('文件出错啦！🤡')