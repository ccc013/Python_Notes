#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2019/8/21 23:43
@Author  : luocai
@file    : concurrent_futures_tutorial.py
@concat  : 429546420@qq.com
@site    : 
@software: PyCharm Community Edition 
@desc    :

concurrent.futures 介绍
官方文档：https://docs.python.org/3/library/concurrent.futures.html
原文：http://masnun.com/2016/03/29/python-a-quick-introduction-to-the-concurrent-futures-module.html
"""
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, wait, as_completed
from random import randint
from time import sleep
import concurrent.futures
import urllib.request
import math


# 定义需要执行的任务--休眠5秒后返回传入的信息
def return_after_5_secs(message):
    sleep(5)
    return message


# 多线程
def thread_pool_example():
    # 建立一个线程池，大小为 3
    pool = ThreadPoolExecutor(3)

    future = pool.submit(return_after_5_secs, ("hello"))
    print(future.done())
    sleep(5)
    print(future.done())
    print(future.result())


# 多进程
def process_pool_example():
    # 建立进程池
    pool = ProcessPoolExecutor(3)

    future = pool.submit(return_after_5_secs, ("hello"))
    print(future.done())
    sleep(5)
    print(future.done())
    print("Result: " + future.result())


# 调用 map() 方法
def thread_pool_map():
    URLS = ['http://www.baidu.com/',
            'http://www.163.com/',
            'http://www.126.com/',
            'http://www.jianshu.com/',
            'http://news.sohu.com/']

    # 访问一个网站并返回读取的内容
    def load_url(url, timeout):
        with urllib.request.urlopen(url, timeout=timeout) as conn:
            return conn.read()

    # We can use a with statement to ensure threads are cleaned up promptly
    # 采用 with 语句保证线程使用完成后完全关闭
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        # Start the load operations and mark each future with its URL
        future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                data = future.result()
            except Exception as exc:
                print('%r generated an exception: %s' % (url, exc))
            else:
                print('%r page is %d bytes' % (url, len(data)))


def is_prime(n):
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


def process_pool_map():
    # 判断给定的数是否素数


    PRIMES = [
        112272535095293,
        112582705942171,
        112272535095293,
        115280095190773,
        115797848077099,
        1099726899285419]

    with concurrent.futures.ProcessPoolExecutor() as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print('%d is prime: %s' % (number, prime))


def return_after_5_secs(num):
    sleep(randint(1, 5))
    return "Return of {}".format(num)


def thread_pool_as_completed():
    pool = ThreadPoolExecutor(5)
    futures = []
    for x in range(5):
        futures.append(pool.submit(return_after_5_secs, x))

    for x in as_completed(futures):
        print(x.result())


def thread_pool_wait():
    pool = ThreadPoolExecutor(5)
    futures = []
    for x in range(5):
        futures.append(pool.submit(return_after_5_secs, x))

    print(wait(futures))


if __name__ == '__main__':
    # thread_pool_example()
    # process_pool_example()
    # thread_pool_map()
    # process_pool_map()
    # thread_pool_as_completed()
    thread_pool_wait()
