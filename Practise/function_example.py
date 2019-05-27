#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2019/5/13 7:15
@Author  : luocai
@file    : function_example.py
@concat  : 429546420@qq.com
@site    : 
@software: PyCharm Community Edition 
@desc    :

"""


# 定义函数和调用函数例子
def hello():
    print("Hello, world!")


# 计算面积的函数
def area(width, height):
    return width * height


hello()
width = 2
height = 3
# print('width={}, height={}, area={}'.format(width, height, area(width, height)))

# 判断类型是否可变
a = 5
# print('a id:{}, val={}'.format(id(a), a))
a = 3
# print('a id:{}, val={}'.format(id(a), a))

la = [1, 2, 3]
# print('la id:{}, val={}'.format(id(la), la))
la[2] = 5


# print('la id:{}, val={}'.format(id(la), la))


# 传递不可变对象的实例
def change_int(a):
    a = 10


b = 2
# print('origin b=', b)
change_int(b)


# print('after call function change_int(), b=', b)


# 传递可变对象的实例
def chang_list(la):
    """
    修改传入的列表参数
    :param la:
    :return:
    """
    la.append([2, 3])
    print('函数内部，la=', la)
    return


la = [10, 30]


# print('调用函数前, la=', la)
# chang_list(la)
# print('函数外取值, la=', la)


# 位置参数
def print_str(str1, n):
    """
    打印输入的字符串 n 次
    :param str1: 打印的字符串内容
    :param n: 打印的次数
    :return:
    """
    for i in range(n):
        print(str1)


strs = 'python '
n = 3


# 正确调用
# print_str(strs, n)


# 错误例子1
# print_str()
# 错误例子2
# print_str(n, strs)

# 默认参数
def print_info(name, age=18):
    '''
    打印信息
    :param name:
    :param age:
    :return:
    '''
    print('name: ', name)
    print('age: ', age)


# print_info('jack')
# print_info('robin', age=30)


# 可变参数
def print_info2(name, age=18, height=178, *args):
    '''
    打印信息函数2
    :param name:
    :param age:
    :param args:
    :return:
    '''
    print('name: ', name)
    print('age: ', age)
    print('height: ', height)
    print(args)
    for language in args:
        print('language: ', language)


# print_info2('robin', 20, 180, 'c', 'javascript')
# languages = ('python', 'java', 'c++', 'go', 'php')
# print_info2('jack', 30, 175, *languages)


# 关键字参数
def print_info3(name, age=18, height=178, *args, **kwargs):
    '''
    打印信息函数3，带有关键字参数
    :param name:
    :param age:
    :param height:
    :param args:
    :param kwargs:
    :return:
    '''
    print('name: ', name)
    print('age: ', age)
    print('height: ', height)

    for language in args:
        print('language: ', language)
    print('keyword: ', kwargs)


# 不传入关键字参数的情况
print_info3('robin', 20, 180, 'c', 'javascript')
# 传入任意关键字参数
print_info3('robin', 20, 180, 'c', 'javascript', birth='2000/02/02')
print_info3('robin', 20, 180, 'c', 'javascript', birth='2000/02/02', weight=125)
# 用字典传入关键字参数
keys = {'birth': '2000/02/02', 'weight': 125, 'province': 'Beijing'}
print_info3('robin', 20, 180, 'c', 'javascript', **keys)


# 命名关键字参数
def print_info4(name, age=18, height=178, *, weight, **kwargs):
    '''
    打印信息函数4，加入命名关键字参数
    :param name:
    :param age:
    :param height:
    :param weight:
    :param kwargs:
    :return:
    '''
    print('name: ', name)
    print('age: ', age)
    print('height: ', height)

    print('keyword: ', kwargs)
    print('weight: ', weight)


print_info4('robin', 20, 180, birth='2000/02/02', weight=125)

# 匿名函数
sum = lambda x, y: x + y

print('sum(1,3)=', sum(1, 3))

# 作用域解释
g_count = 0  # 全局作用域


def outer():
    o_count = 1  # 闭包函数外的函数中

    # 闭包函数 inner()
    def inner():
        i_count = 2  # 局部作用域


import builtins

print(dir(builtins))

if 1:
    sa = 2
else:
    sa = 3
print('sa=', sa)
# print('o_count=', o_count)

# 局部变量和全局变量
total = 3  # 全局变量


def sum_nums(arg1, arg2):
    total = arg1 + arg2  # total在这里是局部变量.
    print("函数内是局部变量 : ", total)
    return total


# 调用 sum_nums 函数
sum_nums(10, 20)
print("函数外是全局变量 : ", total)

# 函数内部修改全局变量
a = 1


def print_a():
    global a
    print('全局变量 a=', a)
    a = 3
    print('修改全局变量 a=', a)


print_a()
print('调用函数 print_a() 后, a=', a)


# 修改闭包作用域中的变量
def outer():
    num = 10

    def inner():
        nonlocal num  # nonlocal关键字声明
        num = 100
        print('闭包函数中 num=', num)

    inner()
    print('调用函数 inner() 后, num=',num)


outer()
