#eq1 --> -1a + 3b =7
#eq2 --> 3a +2b =1

import numpy as np

A=np.array([[-1, 3],
             [3, 2]], dtype=np.float32)

B=np.array([7, 1], dtype=np.float32) # this is because when we mutiply A with a,b i.e a 2by1 matric , we get 1 by 2 matrix as 2x2 with 3x4 = 2x4
# thats why these are in the same row and not in diff rows  

print("matrix A: ", A)
print("data type of A: ", A.dtype)

print("matrix B: ", B)
print("data type of B: ", B.dtype)

