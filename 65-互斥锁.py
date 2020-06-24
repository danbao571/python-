# 创建互斥锁，保证同一时刻只能有一个线程去执行代码，这样全局变量就不会出现资源竞争的问题
import threading
import time

lock = threading.Lock()
g_num = 0


def AA():
    # 上锁
    lock.acquire()
    global g_num
    for i in range(10000):
        g_num += 1

    print('AA', g_num)
    # 释放
    lock.release()


def BB():
    # 上锁
    lock.acquire()
    global g_num
    for i in range(10000):
        g_num += 1
    time.sleep(3)
    print('BB', g_num)

    # 释放
    lock.release()


if __name__ == '__main__':
    # 创建两个线程
    first_thread = threading.Thread(target=AA)
    second_thread = threading.Thread(target=BB)

    first_thread.start()
    second_thread.start()