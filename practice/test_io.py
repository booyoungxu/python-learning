# -*- coding: utf-8 -*-

from io import StringIO
from io import BytesIO
import os # 操作目录
import shutil # 对os的扩展
import pickle # 实现序列化
import json # json序列化

# 文件读写，请求操作系统打开一个文件对象，通过调用改文件对象，对文件进行操作
f = open('/Users/r3t/python-learning/practice/test_list_tuple.py', 'r')
f.close()

# 用with可以自动调用文件对象的close方法
with open('/Users/r3t/python-learning/practice/test_list_tuple.py', 'r') as f:
    pass
    # print(f.read())

# 在python中，有read方法的对象称为file-like Object

# python打开的文档对象默认是utf-8编码的文本文件，读取二进制文件，需要指定模式

f1 = open('/Users/r3t/python-learning/practice/test_list_tuple.py', 'r', encoding='utf-8')
# print(f1.read())
f1.close()

# 在写文件时一定要调用close方法，write之后。os并不会立刻将数据写入磁盘，而是放到内存缓存起来

# 内存中读写str
f2 = StringIO()
f2.write('hello word')
# print(f2.getvalue())

# 读取内存str，可以先初始化
f3 = StringIO('hello\n world\n')
# print(f3.readline())
# print(f3.read())

# 操作二进制数据
f4 = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
# print(f4.read())

#操作文件和目录
# print(os.name)
# print(os.environ.get('PATH')) # 环境变量

# print(os.path.abspath('.')) # 当前目录的绝对路径，不包括文件名
# print(os.path.join('/Users/r3t/python-learning', 'testdir')) #表示新建的目录路径
# os.makedirs(os.path.join('/Users/r3t/python-learning', 'testdir')) # 新建目录
# os.rmdir(os.path.join('/Users/r3t/python-learning', 'testdir')) # 删除目录
# print(os.path.split('/Users/r3t/python-learning/practice/test_io.py')) # 将文件名和路径拆开
# print(os.path.splitext('/Users/r3t/python-learning/practice/test_io.py')) # 将文件扩展名和其他拆开

# os.rename('test.txt', 'test.py') # 对当前目录下的文件重命名
# os.remove('test.py') # 删除当前目录下的文件
# shutil.copyfile('test1.txt', 'text2.txt') #将文件1复制到文件而

# print([x for x in os.listdir('.')])

# pickle序列化，将变量从内存中变成可存储或传输的过程
# d = dict(name = 'blob', age = 20, score = 99)
# print(pickle.dumps(d)) # dump将任意对象序列化为bytes
# f5 = open('dump.txt', 'wb')
# pickle.dump(d, f5) # 将对行直接写入文件
# f5.close()
#
# f6 = open('dump.txt', 'rb')
# d1 = pickle.load(f6)
# print(d1)
# f6.close()

# json序列化

# d2 = dict(name = 'Lisa', age = 18, score = 99)
# dumps = json.dumps(d2)
# print(dumps) # 序列化成json
# print(json.loads(dumps))

# 对类实例进行序列化
class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age

stu = Student('Tom', '100')
# print(json.dumps(stu)) # 直接序列化会报错，需要知道序列化规则
dd = json.dumps(stu, default=lambda obj: obj.__dict__)
print(dd) # 用default定制好规则后，序列化成功

def dict2student(d):
    return Student(d['name'], d['age'])

print(json.loads(dd, object_hook=dict2student))