import numpy as np

arr1d = np.array([1, 2, 3, 4, 5])
print(arr1d)
print(arr1d.shape)

arr2d = np.array([[10, 20, 30], [40, 50, 60]])
print(arr2d)
print(arr2d.shape)
print(arr2d.size)
print(arr2d.dtype)

zeros_arr = np.zeros((2, 3))
print(zeros_arr)

ones_arr = np.ones((3, 2))
print(ones_arr)

range_arr = np.arange(0, 10, 2)
print(range_arr)

linspace_arr = np.linspace(0, 10, 5)
print(linspace_arr)