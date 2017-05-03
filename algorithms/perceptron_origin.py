# -*- coding: utf-8 -*-

training_set = [[(3, 3), 1], [(4, 3), 1], [(1, 1), -1]]
w = [0, 0]
b = 0


def update(item):
    """
    update parameter using stochastic gradient descent
    :param item: an item which is classify to wrong class
    :return:
    """
    global w, b
    w[0] += 1 * item[1] * item[0][0]
    w[1] += 1 * item[1] * item[0][1]
    b += 1 * item[1]
    print(w, b)


def dis(item):
    """
    loss function to a item
    :param item:
    :return: loss value
    """
    res = 0
    for i in range(len(item[0])):
        res += item[0][i] * w[i]
    res += b
    res *= item[1]
    return res


def check():
    flag = True
    for item in training_set:
        if dis(item) <= 0:
            flag = False
            update(item)
    if flag:
        print('w is %s, b is %s' % (str(w), str(b)))
    return flag

if __name__ == '__main__':
    for i in range(10000):
        if check():
            break
