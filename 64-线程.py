# 线程：执行代码的分支，默认程序中只有一个线程
import time
import threading


def AA(count):
    for i in range(count):
        print('aa')
        time.sleep(0.2)


def BB(count):
    for i in range(count):
        print('bb')
        time.sleep(0.2)


if __name__ == '__main__':
    # 创建子线程执行对应的代码
    # target表示目标函数
    # args:表示以元组方式传参
    # kwargs:表示以字典方式传参
    # sub_thread = threading.Thread(target=aa, args=(3,))
    sub_thread = threading.Thread(target=AA, kwargs={'count': 3})
    three_thread = threading.Thread(target=BB, args=(2,), daemon=True )
    # 设置守护线程，主线程退出子线程会直接销毁不再执行对应代码
    # sub_thread.setDaemon(True)
    sub_thread.start()
    three_thread.start()

    time.sleep(2)
    print('over')

    # 主线程执行bb
    # 主线程会等所有子线程代码执行完再退出
    # BB()
    # 线程执行是无序的，由cpu调度决定
