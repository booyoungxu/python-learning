# -*- coding: utf-8 -*-

from collections import namedtuple
from collections import deque
from collections import defaultdict
from collections import OrderedDict
from collections import Counter

# create a tuple named Point
Points = namedtuple('Point', ['x', 'y'])
p = Points(1, 2)
print(p, p.x, p.y)
# Point(x=1, y=2) 1 2
print(isinstance(p, Points))
# True


# two directory append and pop element of list
dq = deque([1, 2, 3])
dq.append(4)
dq.appendleft(0)
dq.pop()
dq.popleft()
print(dq)
# deque([0, 1, 2, 3, 4])

# return default value for empty key
dct = defaultdict(lambda: 'defaultKey')
dct['key'] = 'value'
print(dct['key'], dct['key1'])
# value defaultKey

# sorted by input order
od = OrderedDict()
od[2] = 2
od[1] = 1
od[3] = 3
print(od.keys(), od.values())
# odict_keys([2, 1, 3]) odict_values([2, 1, 3])

# count
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)
# Counter({'m': 2, 'r': 2, 'g': 2, 'a': 1, 'p': 1, 'i': 1, 'n': 1, 'o': 1})
