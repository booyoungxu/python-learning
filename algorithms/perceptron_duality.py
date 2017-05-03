# -*- coding: utf-8 -*-

import numpy as np

training_set = np.array([[[3, 3], 1], [[4, 3], 1], [[1, 1], -1]])
a = np.zeros(len(training_set), np.int)
b = 0
Gram = None


def cal_gram():
    """
    calculate Gram matrix
    :return: Gram
    """
    g = np.empty((len(training_set), len(training_set)), np.int)
    for i in range(len(training_set)):
        for j in range(len(training_set)):
            g[i][j] = np.dot(training_set[i][0], training_set[j][0])
    return g


def dis(i):
    """
    calculate ith item condition
    :param i:
    :return: loss value
    """
    global a, b
    res = np.dot(a * training_set[:, 1], Gram[i])
    res = (res + b) * training_set[i][1]
    return res


def update(i):
    global a, b
    a[i] += 1
    b += 1 * training_set[i][1]
    print(a, b)


def check():
    flag = True
    for i in range(len(training_set)):
        if dis(i) <= 0:
            flag = False
            update(i)
    if flag:
        w = np.dot(a*training_set[:, 1], training_set[:, 0])
        print('w is %s, b is %s' % (str(w), str(b)))
        return True
    return False

if __name__ == '__main__':
    Gram = cal_gram()
    for i in range(10000):
        if check():
            break

