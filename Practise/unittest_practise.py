#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2019/7/9 8:12
@Author  : luocai
@file    : unittest_practise.py
@concat  : 429546420@qq.com
@site    : 
@software: PyCharm Community Edition 
@desc    :

"""
import unittest


def get_formatted_name(first, last, middle=''):
    '''
    接收姓和名然后返回完整的姓名
    :param first:
    :param last:
    :return:
    '''
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()


class NamesTestCase(unittest.TestCase):
    '''
    测试生成名字函数的类
    '''

    def test_first_last_name(self):
        formatted_name = get_formatted_name('kobe', 'bryant')
        self.assertEqual(formatted_name, 'Kobe Bryant')

    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name('kobe', 'bryant', 'snake')
        self.assertEqual(formatted_name, 'Kobe Snake Bryant')


if __name__ == '__main__':
    first = 'kobe'
    last = 'bryant'
    # print(get_formatted_name(first, last))

    unittest.main()
