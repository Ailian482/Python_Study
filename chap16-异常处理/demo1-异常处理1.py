# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/6/14 下午2:27

"""
你不可能总是对的
作为一个合格的程序员，在编程的时候要意识到：永远不要太相信的你用户，要把他们想象成是小孩子，把他们想象成是黑客，他们无时无刻都想要搞掉你的程序
这样你写出的代码、程序才会更加的安全稳定
出现问题就要想办法去解决问题，程序出现逻辑错误或者用户输入不合法都可能引发程序的错误
然而这些错误并非是致命的，不会导致程序崩掉，所以可以使用python的异常处理机制，在错误出现的时候，程序内部的方式自我消化

什么是异常？
exception

python标注异常
    AssertionError：断言语句（assert）失败
    AttributeError：尝试访问未知的对象方法或属性
    EOFError：input()读取到EOF却没有接收任何数据
    FloatingPointError：浮点计算错误
    GeneratorExit：generator.close()方法被调用的时候
    ImportError：导入模块失败的时候
    IndexError：所以超出序列的范围
    KeyError：字典中查找一个不存在的关键字
    KeyboardInterrupt：用户输入中断键（Ctrl+C）
    MemoryError：内存溢出（可通过删除对象释放内存）
    NameError：尝试访问一个不存在的变量
    NotImplementedError：尚未实现的方法
    OSError：操作系统产生的异常（例如打开一个不存在的文件）
    FileNotFoundError：文件不存在
    OverflowError：数值运算超出最大限制
    ReferenceError：弱引用（weak reference）试图访问一个已经被垃圾回收机制回收了的对象
    SyntaxError：python的语法错误
    RuntimeError：一般的运行时错误
    IndentationError：缩进问题
    TabError：Tab和空格混合使用
    SystemError：Python编译器系统错误
    SystemExit：Python编译器进程被关闭
    TypeError：不同类型间的无效操作
    UnboundLocalError：访问一个未初始化的本地变量（NameError的子类）
    UnicodeError：Unicode相关的错误（ValueError的子类）
    UnicodeEncodeError：Unicode编码时的错误（UnicodeError的子类）
    UnicodeDecodeError：Unicode解码时的错误（UnicodeError的子类）
    UnicodeRTranslateError：Unicode转换时的错误（UnicodeError的子类）
    ValueError：传入参数无效
    ZeroivisionError：除数为0
"""

# file_name = input('请输入需要打开的文件名：')
# f = open(file_name)
# print('文件的内容是：')
# for each_line in f:
#     print(each_line)

my_list = ['小白猪是最强王者！', 1, 2]
assert len(my_list) > 0
ele = my_list.pop()
print(ele)

# assert len(my_list) > 0  # AssertionError

# my_list.fishc  # AttributeError: 'list' object has no attribute 'fishc'

# print(my_list[3])  # IndexError: list index out of range

my_dict = {'one': 1, 'two': 2, 'three': 3}
# my_dict['four']  # KeyError: 'four'
my_dict.get('four')  # 字典的 get() 方法比使用 索引好


# print(1 + '1')  # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# print(3/0)  # ZeroDivisionError: division by zero


def cunzai(a, b):
    try:
        n = a / b
    except:
        return False
    return True


for i in range(11):
    if cunzai(1, i) is True:
        print("chucuole")
        continue
    else:
        break
