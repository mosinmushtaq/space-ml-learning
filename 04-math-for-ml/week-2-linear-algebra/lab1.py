import numpy as np 

A=np.array([[4,-3,1],
           [2,1,3],
           [-1,2,-5]], dtype=np.dtype(float))

B=np.array([-10,0,17], dtype=np.dtype(float))

print("A =")
print(A)
print("Dimension of A:")
print(np.shape(A))
print("B =")
print(B)
print("Dimension of B:")
print(np.shape(B))
print("Determinant of A is: ")
print(np.linalg.det(A))
print("Solution to matrix A ")
print(np.linalg.solve(A,B))

#NOw row Reduction

B=B.reshape(3,1)

Matrix=np.hstack((A,B))
print(Matrix)

