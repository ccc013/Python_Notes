#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2019/8/25 11:53
@Author  : luocai
@file    : multi_process.py
@concat  : 429546420@qq.com
@site    : 
@software: PyCharm Community Edition 
@desc    :

多进程例子

"""
import os
from multiprocessing import Process, Pool, Queue
from random import randint
import random
from time import time, sleep
import subprocess


def do_fork():
    print('Process (%s) start...' % os.getpid())
    # 只能在 Unix/Linux/Mac 上执行，Windows 上 os 模块没有 fork() 函数
    pid = os.fork()
    if pid == 0:
        print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
    else:
        print('I (%s) just created a child process (%s).' % (os.getpid(), pid))


def download_task(filename):
    '''模拟下载文件'''
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))


def download_without_multiprocess():
    '''不采用多进程'''
    start = time()
    download_task('Python.pdf')
    download_task('nazha.mkv')
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))


def download_multiprocess():
    '''采用多进程'''
    start = time()
    p1 = Process(target=download_task, args=('Python.pdf',))
    p1.start()
    p2 = Process(target=download_task, args=('nazha.mkv',))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))


def download_multiprocess_pool():
    '''采用多进程，并用 pool 管理进程池'''
    start = time()
    filenames = ['Python.pdf', 'nazha.mkv', 'something.mp4', 'lena.png', 'lol.avi']
    # 进程池
    p = Pool(5)
    for i in range(5):
        p.apply_async(download_task, args=(filenames[i],))
    print('Waiting for all subprocesses done...')
    # 关闭进程池
    p.close()
    # 等待所有进程完成任务
    p.join()
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))


def subprocess_use():
    '''
    利用 subprocess 创建和使用子进程来演示执行命令 'nslookup www.python.org'
    :return:
    '''

    print('$ nslookup www.python.org')
    r = subprocess.call(['nslookup', 'www.python.org'])
    print('Exit code:', r)


def subprocess_use2():
    '''
    subprocess 对子进程进行输入
    :return:
    '''
    print('$ nslookup')
    p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
    print(output.decode('utf-8'))
    print('Exit code:', p.returncode)


# 写数据进程执行的代码:
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        sleep(random.random())


# 读数据进程执行的代码:
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)


def ipc_queue():
    '''
    采用 Queue 实现进程间通信
    :return:
    '''
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()


if __name__ == '__main__':
    # do_fork()
    # download_without_multiprocess()
    # download_multiprocess()
    # download_multiprocess_pool()
    # subprocess_use2()
    ipc_queue()
