#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2019/6/23 15:01
@Author  : luocai
@file    : class_example.py
@concat  : 429546420@qq.com
@site    : 
@software: PyCharm Community Edition 
@desc    :

"""


# 定义一个动物类别
class Animal(object):
    # 类变量
    eat = True

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    # 类方法
    def run(self):
        return 'Animal run!'


# 实例化类
anm = Animal('animal', 'male')

# 访问类的属性和方法
print("Animal 类的属性 eat 为：", anm.eat)
print("Animal 类的方法 run 输出为：", anm.run())


# 验证 self 参数代表类实例，而非类
class Test:
    def prt(self):
        print(self)
        print(self.__class__)


# 不用 self 名称
class Test2:
    def prt(sss):
        print(sss)
        print(sss.__class__)


t = Test()
t.prt()

t2 = Test2()
t2.prt()


# 类定义
class people(object):
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))


# 实例化类
p = people('runoob', 10, 30)
p.speak()


# 单继承示例
class student(people):
    grade = ''

    def __init__(self, n, a, w, g):
        # 调用父类的构造方法
        people.__init__(self, n, a, w)
        self.grade = g

    # 覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))


s = student('ken', 10, 60, 3)
s.speak()


# 另一个类，多重继承之前的准备
class speaker():
    topic = ''
    name = ''

    def __init__(self, n, t):
        self.name = n
        self.topic = t

    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s" % (self.name, self.topic))


# 多重继承
class sample(speaker, student):
    a = ''

    def __init__(self, n, a, w, g, t):
        speaker.__init__(self, n, t)
        student.__init__(self, n, a, w, g)

    # 显示调用 student 父类的 speak 方法
    def speak(self):
        super(student, self).speak()


test = sample("Tim", 25, 80, 4, "Python")
test.speak()  # 方法名同，默认调用的是在括号中排前地父类的方法


class TimeCounter:
    def __init__(self):
        print('timer')


class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0  # 公开变量

    def __init__(self):
        self.timer = TimeCounter()

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print(self.__secretCount)
        self.__count()

    def __count(self):
        print('私有方法')


counter = JustCounter()
counter.count()
counter.count()
print(counter.publicCount)

# print(counter.__secretCount)  # 报错，实例不能访问私有变量
# print(counter.__count())

from time import sleep


# 练习1：定义一个类描述数字时钟
class Clock(object):
    """数字时钟"""

    def __init__(self, hour=0, minute=0, second=0):
        '''
        初始化三个基本属性，时，分，秒
        :param hour:
        :param minute:
        :param second:
        '''
        self._hour = hour
        self._minute = minute
        self._second = second

    def run(self):
        '''
        模拟时钟的运行
        :return:
        '''
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        '''
        显示时间
        :return:
        '''
        print("{:02d}:{:02d}:{:02d}".format(self._hour, self._minute, self._second))


# 简单时钟例子
clock = Clock(23, 59, 57)
i = 0
while i < 5:
    clock.show()
    sleep(1)
    clock.run()
    i += 1

from math import sqrt


# 定义描述平面上点之间的移动和计算距离的类
class Point(object):
    def __init__(self, x=0, y=0):
        '''
        初始的坐标
        :param x:横坐标
        :param y:纵坐标
        '''
        self._x = x
        self._y = y

    def move_to(self, new_x, new_y):
        '''
        移动到新的坐标
        :param new_x:新的横坐标
        :param new_y:新的纵坐标
        :return:
        '''
        self._x = new_x
        self._y = new_y

    def move_by(self, dx, dy):
        '''
        移动指定的增量
        :param dx:横坐标的增量
        :param dy:纵坐标的增量
        :return:
        '''
        self._x += dx
        self._y += dy

    def distance(self, other):
        '''
        计算与另一个点的距离
        :param other:
        :return:
        '''
        x_dist = self._x - other._x
        y_dist = self._y - other._y
        return sqrt(x_dist ** 2 + y_dist ** 2)

    def __str__(self):
        '''
        显示当前点坐标
        :return:
        '''
        return '({},{})'.format(self._x, self._y)


# 应用例子
p1 = Point(10, 20)
p2 = Point(30, 5)
print('point1:', p1)
print('point2:', p2)
p1.move_to(15, 25)
print('after move to (15, 25), point1:', p1)
p1.move_by(20, 10)
print('move by (20, 10), point1:', p1)
dist = p1.distance(p2)
print('distance between p1 and p2: ', dist)
