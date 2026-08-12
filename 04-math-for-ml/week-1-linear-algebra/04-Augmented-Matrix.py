import numpy as np# In order to visualize the system of equations, what we need is that we have to combine the equations and their constants together. That is the first part. 

# In order to do that, we have to combine those, but there is a catch. There is a thing that we need to consider:
# matrix A is a 2D matrix, but matrix B is a one-dimensional array, so we have to reshape that.


A=np.array([[-1, 3],
             [3, 2]])

B=np.array([7, 1])

print(A)

print(B)

reshapedb=np.reshape((B), (2, 1))
print("reshaped B:", reshapedb)

#NOW STACKING USING HSTACK

combined=np.hstack((A, reshapedb))
print("Hstacked matrix is: ", (combined ))

