# -*- coding: utf-8 -*-

from math import log
import operator
import numpy as np

#     outlook     temperature    humidity    windy          result
#     ---------------------------------------------------------
#     sunny       hot            high         false         N
#     sunny       hot            normal       true          N
#     overcast    hot            high         false         Y
#     rain        mild           high         false         Y
#     rain        cool           high         false         Y
#     rain        cool           normal       true          N
#     overcast    cool           normal       true          Y


def create_training_set():
    """
    sunny => 0, overcast => 1, rain => 2
    hot => 1, mild => 1, cool => 2
    high => 0, normal => 1
    false => 0, true => 1
    :return: training_set and feat_labels
    """
    training_set = [[0, 0, 0, 0, 'N'],
                    [0, 0, 0, 1, 'N'],
                    [1, 0, 0, 0, 'Y'],
                    [2, 1, 0, 0, 'Y'],
                    [2, 2, 1, 0, 'Y'],
                    [2, 2, 1, 1, 'N'],
                    [1, 2, 1, 1, 'Y']]

    feat_labels = ['outlook', 'temperature', 'humidity', 'windy']
    return training_set, feat_labels

    # outlook    temperature    humidity    windy
    # ---------------------------------------------------------
    # sunny       mild           high         false
    # sunny       cool           normal       false
    # rain        mild           normal       false
    # sunny       mild           normal       true
    # overcast    mild           high         true
    # overcast    hot            normal       false
    # rain        mild           high         true


def create_test_set():
    test_set = [[0, 1, 0, 0],
                [0, 2, 1, 0],
                [2, 1, 1, 0],
                [0, 1, 1, 1],
                [1, 1, 0, 1],
                [1, 0, 1, 0],
                [2, 1, 0, 1]]
    return test_set


def split_data(data_set, axis, value):
    """
    计算data_set中第axis特征的值为value的数据
     :param data_set: 训练数据集
     :param axis: 特征
     :param value: 特征值
     :return: 数据集中特征axis的值为value的数据
    """
    res = []
    for feat_vec in data_set:
        if feat_vec[axis] == value:
            res.append(feat_vec)
    return res


def split_fecture(data_set):
    """
    根据特征值的Gini指数找到当前数据集中的最优划分值
    :param data_set: 训练集
    :return:最优特征
    """
    feat_size = len(data_set[0]) - 1    # 包含了类别结果
    min_gini = 999999.0
    feat_choose = -1
    for i in range(feat_size):  # 分别列举每个特征
        feat_list = [data[i] for data in data_set]  # 所有数据的某一特征
        gini = 0.
        for value in set(feat_list):    # 对特征中的每一个取值
            sub_data = split_data(data_set, i, value)  # all data whose ith feature is value
            tmp1 = len(sub_data) / len(data_set)
            p1 = len(split_data(sub_data, feat_size, 'N'))/len(sub_data)  # value and N
            gini_sub_data1 = 2 * p1 * (1-p1)
            p2 = len(split_data(sub_data, feat_size, 'Y'))/len(sub_data)
            gini_sub_data2 = 2 * p2 * (1-p2)
            gini += tmp1*gini_sub_data1 + (1-tmp1)*gini_sub_data2
        if gini < min_gini:
            min_gini = gini
            feat_choose = i
    return feat_choose


def classify_res(class_list):
    class_count = {}
    for key in class_list:
        class_count[key] = class_count.get(key, 0) + 1
    sorted_count = sorted(class_count.items(), key=lambda d: d[1], reverse=True)
    return sorted_count[0][0]


def create_tree(data_set, labels):
    """
    根据特征和数训练集创建决策树
    :param data_set: 数据集
    :param labels: 特征
    :return: 决策树
    """
    class_list = [data[-1] for data in data_set]    # 训练集的类别结果
    if class_list.count(class_list[0]) == len(class_list):  # 均为同一类别
        return class_list[0]
    if len(data_set[0]) == 1:   # 只有一个特征
        return classify_res(class_list)
    best_feat = split_fecture(data_set)
    best_label = labels[best_feat]
    tree = {best_label: {}}
    feat_values = [data[best_feat] for data in data_set]
    for value in set(feat_values):
        tree[best_label][value] = create_tree(split_data(data_set, best_feat, value), labels)
    return tree


def classify(input_tree, labels, test_data):
    first = list(input_tree.keys())[0]
    second = input_tree[first]
    feat_index = labels.index(first)
    res = 'N'
    for key in second.keys():
        if test_data[feat_index] == key:
            if type(second[key]).__name__ == 'dict':
                res = classify(second[key], labels, test_data)
            else:
                res = second[key]
    return res


def classify_all(input_tree, labels, test_data):
    res = []
    for test_vec in test_data:
        res.append(classify(input_tree, labels, test_vec))
    return res

def main():
    training_set, labels = create_training_set()
    labels_tmp = labels[:]
    decision_tree = create_tree(training_set, labels_tmp)
    print('decision_tree', decision_tree)
    test_set = create_test_set()
    print('class_result', classify_all(decision_tree, labels, test_set))

if __name__ == '__main__':
    main()
