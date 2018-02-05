# coding: UTF-8

import numpy as np
A = np.array([1,2,3,4])
print(A)
print(np.ndim(A)) # 配列の次元の取得
print(A.shape) # 配列の形状はインスタンス変数から取得
print(A.shape[0])

B = np.array([[1,2],[3,4],[5,6]])
print(B)
print(np.ndim(B))
print(B.shape)
print(B.shape[0])

# 行列の積の実装
A = np.array([[1,2],[3,4]])
print(A.shape)

B = np.array([[5,6],[7,8]])
print(B.shape)

print(np.dot(A,B)) # 内積の計算
