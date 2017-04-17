# -*- coding: utf-8 -*-

import functools

# 用于扩展一个函数，可以传入参数
def log(func):
    def wrapper(*args, **kw):
        print('call %s(): '% func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('hello word!');

# now()

def logg(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s()' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@logg('excute')
def hello():
    print('haha~')

# hello()

# 由于用了装饰器，原函数的名字已经变成了wrapper, 所以需要将原始函数的名字复制到wrapper下

def loggg(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('excute %s:' % func.__name__)
        return func(*args, **kw)
    return wrapper

@loggg
def haha():
    print('abc')

# print(haha.__name__) # haha

def logggg(text):
    if isinstance(text,str):
        def decorator(f):
            @functools.wraps(f)
            def wrap(*arg,**kw):
                print ("befor call ")
                print ('%s,funcname=%s'%(text,f.__name__))
                f(*arg,**kw)
                print ("after call")
                return None
            return wrap
        return decorator
    @functools.wraps(text)
    def wrap(*arg,**kw):
        print ('before call')
        text(*arg,**kw)
        print('after call')
        return None
    return wrap

@logggg('excute')
def wawa():
    print('wawa')


# wawa()