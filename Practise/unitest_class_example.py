#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2019/7/10 8:20
@Author  : luocai
@file    : unitest_class_example.py
@concat  : 429546420@qq.com
@site    : 
@software: PyCharm Community Edition 
@desc    :

"""
import unittest


class AnonymousSurvey():
    '''
    收集匿名调查问卷的答案
    '''

    def __init__(self, question):
        '''

        :param question:
        '''
        self.question = question
        self.responses = []

    def show_question(self):
        '''
        显示问卷
        :return:
        '''
        print(self.question)

    def store_response(self, new_response):
        '''
        存储单份调查问卷
        :param new_response:
        :return:
        '''
        self.responses.append(new_response)

    def show_results(self):
        '''
        显示所有答卷
        :return:
        '''
        print('Survey results:')
        for response in self.responses:
            print('- ' + response)


class TestAnonmyousSurvey(unittest.TestCase):

    def setUp(self):
        '''
        创建一个调查对象和一组答案
        :return:
        '''
        question = "世上最好的语言是？"
        self.language_survey = AnonymousSurvey(question)
        self.responses = ['c++', 'php', 'python']

    def test_store_single_response(self):
        '''
        测试保存单份问卷的方法
        :return:
        '''
        self.language_survey.store_response(self.responses[1])

        self.assertIn('php', self.language_survey.responses)

    def test_store_three_response(self):
        for response in self.responses:
            self.language_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.language_survey.responses)


def use_anonymous_survey():
    question = "世上最好的语言是？"
    language_survey = AnonymousSurvey(question)
    # 显示问题
    language_survey.show_question()
    # 添加问卷
    language_survey.store_response('php')
    language_survey.store_response('python')
    language_survey.store_response('c++')
    language_survey.store_response('java')
    language_survey.store_response('go')
    # 展示所有问卷
    language_survey.show_results()


if __name__ == '__main__':
    # use_anonymous_survey()

    unittest.main()
