import numpy as np

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr[1:4])
print(arr[::2])
print(arr[1:8:2])
print(arr[-3:])
print(arr[::-1])

matrix = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(matrix[0:2, 1:3])
print(matrix[1, :])