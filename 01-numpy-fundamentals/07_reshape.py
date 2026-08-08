import numpy as np

arr = np.arange(12)
print(arr)

reshaped = arr.reshape(3, 4)
print(reshaped)
print(reshaped.shape)

reshaped2 = arr.reshape(2, 6)
print(reshaped2)

matrix = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
reshaped3 = matrix.reshape(4, 2)
print(reshaped3)