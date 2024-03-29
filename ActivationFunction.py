import numpy as np

#域値の計算については仕様などが絡んで複雑なので省略
sigmoid_range = 34.538776394910684


def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-np.clip(x, -sigmoid_range, sigmoid_range)))


def derivative_sigmoid(o):
    return o * (1.0 - o)
