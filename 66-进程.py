# 进程：每次创建一个进程操作系统会给这个进程分配对应的运行资源，一个进程里面默认有一个线程
# 真正干活的是线程，进程只提供资源

# 使用多进程也可以完成多任务
import multiprocessing
import time


def add_data(queue):
    for i in range(3):
        print(i)
        queue.put(i)
        time.sleep(0.3)


def read_data(queue):
    while True:
        # 判断队列是否为空
        if queue.empty():
            break
        value = queue.get()
        print(value)


if __name__ == '__main__':
    # 创建子进程
    # 默认时队列可以放入任意多个数据
    # 3：表示队列中最多有三个数据
    queue = multiprocessing.Queue(3)
    add_process = multiprocessing.Process(target=add_data, args=(queue, ))
    read_process = multiprocessing.Process(target=read_data, args=(queue, ))

    # 启动进程执行任务
    # 设置守护进程
    # add_process.daemon = True
    add_process.start()
    # 进程等待，主进程等待子进程执行完再让后面的代码执行
    add_process.join()
    read_process.start()
    # 主进程也会等待子进程完成后再退出
    # 让子进程终止，销毁
    # first.terminate()


# 两个进程之间的全局变量不共享

# 多任务：使用线程和进程
# 从资源角度来说线程更加节省资源
# 进程销毁的资源比较多

# 从代码稳定性来说,多进程要比多线程稳定性好，因为一个进程挂掉不会影响其他进程
iter()