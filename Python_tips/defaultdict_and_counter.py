#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2019/6/7 18:45
@Author  : luocai
@file    : defaultdict_and_counter.py
@concat  : 429546420@qq.com
@site    : 
@software: PyCharm Community Edition 
@desc    :


using defaultdict and counter in place of dictionary
https://towardsdatascience.com/python-pro-tip-start-using-python-defaultdict-and-counter-in-place-of-dictionary-d1922513f747
"""
from collections import defaultdict, Counter
import timeit

# count the number of word occurrences in a piece of text
text = "I need to count the number of word occurrences in a piece of text. How could I do that? " \
       "Python provides us with multiple ways to do the same thing. But only one way I find beautiful."

# Method 1--using dict
t1 = timeit.default_timer()
word_count_dict = {}
for w in text.split(" "):
    if w in word_count_dict:
        word_count_dict[w] += 1
    else:
        word_count_dict[w] = 1
t1_end = timeit.default_timer()
print('cost time: ', str(t1_end - t1))
# print('dict: ', word_count_dict)

# Method 2--using defaultdict
t2 = timeit.default_timer()
word_count_dict = defaultdict(int)
for w in text.split(" "):
    word_count_dict[w] += 1
t2_end = timeit.default_timer()
print('cost time: ', str(t2_end - t2))
print('defaultdict: ', word_count_dict)

# Method 3--using Counter
t3 = timeit.default_timer()
word_count_dict = Counter()
for w in text.split(" "):
    word_count_dict[w] += 1
t3_end = timeit.default_timer()
print('cost time: ', str(t3_end - t3))
print('Counter: ', word_count_dict)
# get the most common word
print('most common word: ', word_count_dict.most_common(10))
# Second method using Counter
word_counter = Counter(text.split(" "))
print('Counter: ', word_counter)
# Count Characters
print(Counter('abccccccddddd'))  # Output: Counter({'a': 1, 'b': 1, 'c': 6, 'd': 5})
# Count List elements
print(Counter([1, 2, 3, 4, 5, 1, 2]))  # Output: Counter({1: 2, 2: 2, 3: 1, 4: 1, 5: 1})

# more defaultdict examples
s = [('color', 'blue'), ('color', 'orange'), ('color', 'yellow'), ('fruit', 'banana'), ('fruit', 'orange'),
     ('fruit', 'banana')]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)
print(
    d)  # Output: defaultdict(<class 'list'>, {'color': ['blue', 'orange', 'yellow'], 'fruit': ['banana', 'orange', 'banana']})

# using set instead of list
s = [('color', 'blue'), ('color', 'orange'), ('color', 'yellow'), ('fruit', 'banana'), ('fruit', 'orange'),
     ('fruit', 'banana')]
d = defaultdict(set)
for k, v in s:
    d[k].add(v)
print(d)  # Output: defaultdict(<class 'set'>, {'fruit': {'banana', 'orange'}, 'color': {'blue', 'orange', 'yellow'}})
