# coding: UTF-8

import numpy as np
def cross_entropy_error(y,t):
    delta = 1e-7
    return -np.sum(t*np.log(y+delta))

# [2]を正解とする．
t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]

# [2]の確率が最も高い場合
y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
print(cross_entropy_error(np.array(y),np.array(t)))

y = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.5, 0.0]
print(cross_entropy_error(np.array(y),np.array(t)))
