# -*- coding: utf-8 -*-

import numpy as np

A1 = np.array([1, 2, 3])
A2 = np.array(['S', 'M', 'L'])
Y = np.array([-1, 1])
class_data = np.array([2, 'S'])

training_set = np.array([[[1, 'S'], -1], [[1, 'M'], -1], [[1, 'M'], 1], [[1, 'S'], 1], [[1, 'S'], -1], [[2, 'S'], -1], [[2, 'M'], -1], [[2, 'M'], 1], [[2, 'L'], 1], [[2, 'L'], 1], [[3, 'L'], 1], [[3, 'M'], 1], [[3, 'M'], 1], [[3, 'L'], 1], [[3, 'L'], -1]])


def bayes(data, data_set):
    p = {}
    size = len(data_set)
    for item in data_set:
        p[item[1]] = p.get(item[1], 0) + 1
    for key, value in p.items():
        p[key] = value/size
    pp1 = {}    # 存Y=1
    pp2 = {}
    for item in data_set:
        if item[1] == 1:
            pp1[item[0][0]] = pp1.get(item[0][0], 0) + 1
            pp1[item[0][1]] = pp1.get(item[0][1], 0) + 1
        else:
            pp2[item[0][0]] = pp2.get(item[0][0], 0) + 1
            pp2[item[0][1]] = pp2.get(item[0][1], 0) + 1
    ppp1 = p[1]
    for key, value in pp1.items():
        pp1[key] = value / (p[1]*size)
        if key == data[0] or key == data[1]:
            ppp1 *= pp1[key]
    ppp2 = p[-1]
    for key, value in pp2.items():
        pp2[key] = value / (p[-1]*size)
        if key == data[0] or key == data[1]:
            ppp2 *= pp2[key]
    print(ppp1, ppp2)
    if ppp1 > ppp2:
        print('class 1')
    else:
        print('class -1')

if __name__ == '__main__':
    bayes(class_data, training_set)