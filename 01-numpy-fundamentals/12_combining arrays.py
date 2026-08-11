# for combining arrays in different ways we have functions 
import numpy as np


#np.hstack() adds just like side by side
#np.vstack() adds like one on top of the other
array=np.array([1,2,3,4])
array1=np.array([5,6,7,8])
print(array)
print(array1)

arraycombh=np.hstack((array,array1))
arraycombv=np.vstack((array,array1))
print(arraycombh)
print(arraycombv)

# same for ndarrays  but the dimensions  should be same/identical as required for matrices in numpy

arr=np.array([[1,2,3,4],
             [6,7,8,9],
             [10,11,12,13]])

print(arr)

arr2=np.array([[12,2,3,4],
               [15,16,17,18],
               [19,20,21,22]])
print(arr2)


comb1=np.hstack((arr,arr2))
comb2=np.vstack((arr,arr2))

print(comb1)
print(comb2)