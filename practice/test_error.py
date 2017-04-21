# -*- coding: utf-8 -*-
import logging
logging.basicConfig(level=logging.INFO)

def func(val):
    try:
        res = 100/val
    except ZeroDivisionError as e:
        print(e)
    finally:
        print('end')

# func(0)

# 断言, 可以用-o来关闭断言， python -o err.py
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero' #断言n!=0是True，否则就抛出断言错误
    return 10/n

# foo(10)
# foo(0)

s = 0
logging.info('s = %d' % s)
# print(10/0)

# 编写单元测试、文档测试