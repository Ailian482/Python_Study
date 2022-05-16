# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2022/4/27 下午4:24


import queue
'''
同步和异步的概念：
    同步：一个一个步骤往下执行。只有在上一个步骤完成之后，程序才会进入下一个步骤。例子：批量处理程序、命令行程序
    异步：系统不会等执行步骤按成后再继续执行下一个步骤
    
异步的优势：
    
'''


# 同步程序
def task(name, work_queue):
    if work_queue.empty():
        count = work_queue.get()
        total = 0
        print(f"Task {name} running")
        for x in range(count):
            total += 1
        print(f"Task {name} total: {total}")


def main():
    """
    this is the main entry point for the program
    :return:
    """
    # create some work in the queue
    work_queue = queue.Queue()

    # put some work in the queue
    for work in [15, 10, 5, 2]:
        work_queue.put(work)

    # create some synchronous tasks
    tasks = [(task, "One", work_queue), (task, "Tow", work_queue)]

    # run the tasks
    for t, n, q in tasks:
        t(n, q)

if __name__ == "__main__":
    main()