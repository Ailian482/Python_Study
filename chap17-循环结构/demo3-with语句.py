# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/6/16 上午9:23


"""
打开文件，还要关闭文件，而且打开的文件可能还会出问题，从而加入了异常处理
但是上面这种做法显然会有限烦人

with语句抽象出文件操作中频繁使用try、except、finally等相关的细节，使用with语句可以大大的减少代码量
也不用担心文件打开后忘记关掉的烦恼，with会自动去考虑文件关闭的问题，当你的文件不再需要用到的时候，with语句会自动帮你关闭文件


"""

# 案例
try:
    f = open('小白猪.txt', 'w')
    for i in range(6):
        f.write('{0}. 我是一个王者！\n'.format(i+1))
    for each_line in f:
        print(each_line)
except OSError as reason:
    print('出错啦：' + str(reason))  # 出错啦：not readable
finally:
    f.close()  # 如果小白猪.txt文件不存在，那么这里就会试图去关闭一个不存在的文件


# 代码优化
try:
    with open('小白猪.txt', 'w') as f:  # with会自动调用 文件的 close()方法，也不需要用到 finally 语句了
        for i in range(6):
            f.write('{0}. 我是一个王者！\n'.format(i + 1))
        for each_line in f:
            print(each_line)
except OSError as reason:
    print('出错啦：' + str(reason))

