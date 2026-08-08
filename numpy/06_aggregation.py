import numpy as np

data = np.array([10, 20, 30, 40, 50])
print(data.sum())
print(data.mean())
print(data.max())
print(data.min())

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix.sum())
print(matrix.mean())
print(matrix.sum(axis=0))
print(matrix.sum(axis=1))