# -*- coding: utf-8 -*-
import numpy as np

ma = np.arange(15).reshape(3, 5)
# dimensions = axes(info = rank)
print(ma)
# 维数 2
print(ma.ndim)
# 大小n＊m (3,5)
print(ma.shape)
# 总长度 15
print(ma.size)
# 元素的类型 int64
print(ma.dtype)
# 每个元素占的字节数 8
print(ma.itemsize)
# 存矩阵的buffer
print(ma.data)

b = np.array([6.0, 8, 10], dtype = complex)
print(type(b)) # numpy.ndarray
print(b)

# default type is float64
c = np.zeros((2, 3))
print(c)

d = np.ones((2, 3, 4), dtype = np.int64)
print(d)

# 产生依赖于内存的随机数
e = np.empty((2, 3))
print(e)

# 可能不包含末尾数字2
print(np.arange(0, 2, 0.3))

# 等分成9个数字
print(np.linspace(0, 2, 9))

# 按序依次排列
print(np.arange(24).reshape(2, 3, 4))