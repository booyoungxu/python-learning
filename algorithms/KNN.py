# -*- coding: utf-8 -*-
import numpy as np
import heapq
from collections import namedtuple


training_set = np.array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
labels = np.array([['A'], ['A'], ['B'], ['B']])


def classify_common(data, data_set, label, k):
    """
    common KNN algorithm
    :param data: current data to classify
    :param data_set: training_set's data
    :param label: training_set's classes
    :param k: find k nearest neighbor
    :return: current data's classes
    """
    size = data_set.shape[0]
    diff = np.tile(data, (size, 1)) - data_set
    dis = (diff**2).sum(axis=1)**0.5
    sorted_dis = np.argsort(dis)
    class_count = {}
    for i in range(k):
        class_label = label[sorted_dis[i]][0]
        class_count[class_label] = class_count.get(class_label, 0) + 1
    sorted_count = sorted(class_count.items(), key=lambda d: d[1], reverse=True)
    return sorted_count[0][0]

# if __name__ == '__main__':
#     print(classify_common([0, 0], training_set, labels, 3))


class TreeNode:
    def __init__(self, left, right, data, split_dim):
        self.left = left
        self.right = right
        self.data = data
        self.split_dim = split_dim

kd_data = np.array([[2, 3], [5, 4], [9, 6], [4, 7], [8, 1], [7, 2]])
aim_data = [6, 1]


def build_kd_tree(data, depth, dim):
    """
    build kd tree
    :param data: data set need to build kd tree
    :param dim: data set's dimension
    :param depth: tree's current depth
    :return:kd tree
    """
    size = data.shape[0]    # 实例数目
    if size == 0:
        return None
    # 切分坐标轴
    split_dim = depth % dim
    mid = size // 2
    # 将数据按照切分轴的中位数分成2部分
    r_index = np.argpartition(data[:, split_dim], mid)
    data = data[r_index, :]
    left = data[0: mid, :]
    right = data[mid+1: size, :]
    mid_data = data[mid]
    left = build_kd_tree(left, depth+1, dim)
    right = build_kd_tree(right, depth+1, dim)
    return TreeNode(left, right, mid_data, split_dim)


def search_data(cur_node, data, heap):
    """
    search 1NN
    :param cur_node: current tree's root node
    :param data: aim data
    :param heap: k node
    :return:
    """
    if cur_node is None:
        return None
    if type(data) is not np.array:
        data = np.asarray(data)
    cur_data = cur_node.data
    left = cur_node.left
    right = cur_node.right
    distance = np.sum((data - cur_data)**2)**.5
    cur_split_dim = cur_node.split_dim
    if data[cur_split_dim] > cur_data[cur_split_dim]:   # 搜索右子树
        tmp = left
        left = right
        right = tmp
    search_data(left, data, heap)
    if len(heap) < 1:
        heapq.heappush(heap, (distance, cur_node.data))     # 目标节点所属叶子节点
    else:
        top_distance, top_node = heap[0]
        if top_distance > distance:
            top_distance, top_node = distance, cur_node.data
            heapq.heappushpop(heap, (top_distance, top_node))
        print('right', right.data)
        search_data(right, data, heap)

if __name__ == '__main__':
    tree_root = build_kd_tree(kd_data, 0, 2)
    que = []
    search_data(tree_root, aim_data, que)
    print(que)