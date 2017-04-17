# -*- coding: utf-8 -*-

import functools

def power(x):
    return x*x

# power 作用于list的每一个元素,返回的值为Iterator对象
ml = map(power, list(range(10)))
# print(list(ml))

def fn(x, y):
    return x*10+y

# print(reduce(fn, [1, 3, 5, 7]))

# print(sorted(['Are', 'you', 'good', 'Hello'], key=str.lower, reverse=True))
# 闭包函数的内函数可以访问外函数的变量
# 返回值为函数时，调用函数时不会执行，但会传入参数，只有调用返回的函数时才会真正执行
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
# print(f1(), f2(),f3()) # 均为9

def build(x, y):
    return lambda: x*x + y*y

ff = build(3, 4)

# print(ff())



# print(int('123')) # 123
# print(int('0123')) # 123

# 偏函数，用于固定原函数的部分情况(int)
int2 = functools.partial(int, base=2)

print(int2('100000')) # 32