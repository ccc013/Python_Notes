#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2019/8/25 11:53
@Author  : luocai
@file    : multi_threading.py
@concat  : 429546420@qq.com
@site    : 
@software: PyCharm Community Edition 
@desc    :

多线程例子

"""
from random import randint
from threading import Thread, current_thread, Lock, local
from time import time, sleep

# 假定这是你的银行存款:
balance = 0
lock = Lock()


def download(filename):
    print('thread %s is running...' % current_thread().name)
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))


def download_multi_threading():
    print('thread %s is running...' % current_thread().name)
    start = time()
    t1 = Thread(target=download, args=('Python.pdf',), name='subthread-1')
    t1.start()
    t2 = Thread(target=download, args=('nazha.mkv',), name='subthread-2')
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('总共耗费了%.3f秒' % (end - start))
    print('thread %s is running...' % current_thread().name)


def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):
    for i in range(100000):
        change_it(n)


def run_thread_lock(n):
    for i in range(100000):
        # 先要获取锁:
        lock.acquire()
        try:
            # 放心地改吧:
            change_it(n)
        finally:
            # 改完了一定要释放锁:
            lock.release()


def nolock_multi_thread():
    t1 = Thread(target=run_thread_lock, args=(5,))
    t2 = Thread(target=run_thread_lock, args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(balance)


# 创建全局ThreadLocal对象:
local_school = local()


def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std, current_thread().name))


def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()


def thread_local():
    t1 = Thread(target=process_thread, args=('Alice',), name='Thread-A')
    t2 = Thread(target=process_thread, args=('Bob',), name='Thread-B')
    t1.start()
    t2.start()
    t1.join()
    t2.join()


if __name__ == '__main__':
    # download_multi_threading()
    # nolock_multi_thread()
    thread_local()
