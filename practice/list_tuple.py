# -*- coding: utf-8 -*-
from collections import Iterable
import os

l = list(range(100))
# print(l[-10:])

for ll in l:
    pass
    # print(ll)

d = {'a': 1, 'b':2, 'c': 3}

for key in d:
    pass
    # print(key)

for value in d.values():
    pass
    # print(value)

for k, v in d.items():
    pass
    # print(k, v)

# print(isinstance('abc', Iterable))

# print(isinstance(123, Iterable))

for i, val in enumerate(['A', 'B', 'C']):
    pass
    # print(i, val)

for x, y in [(1,1), (2,2), (3,3)]:
    pass
    # print(x, y)

# print([x * x for x in range(1, 11)])

# print([x * x for x in range(1, 11) if x*x % 2 == 0])

# print([m+n for m in 'ABC' for n in 'XYZ'])

# print([d for d in os.listdir('.')])

L1 = ['Hello', 'World', 18, 'Apple', None]
# print([ss.lower() for ss in L1 if isinstance(ss, str)])

# generator
g = (x*x for x in range(10))
print(g)

for n in g:
    pass
    # print(n)

def fib(n):
    m, a, b = 0, 0, 1
    while m < n:
        yield b
        a, b = b, a+b
        m += 1
    return 'finished'
print(fib(6))

for c in fib(6):
    print(c)