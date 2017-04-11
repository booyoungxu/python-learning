# -*- coding: utf-8 -*-

from functools import reduce

def power(x):
    return x*x

# power 作用于list的每一个元素,返回的值为Iterator对象
ml = map(power, list(range(10)))
# print(list(ml))

def fn(x, y):
    return x*10+y

print(reduce(fn, [1, 3, 5, 7]))
