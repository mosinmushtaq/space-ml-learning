import numpy as np

##Using a non-singular system of linear equstions

A=np.array([[4,-3,1],
            [2,1,3],
            [-1,2,-5]] , dtype=np.dtype(float))

B=np.array([-10,0,17] , dtype=np.dtype(float))

print(f"A = \n{A}")

print(f"B = \n{B}")

print(f"Dimension of A : {np.shape(A)}")
print(f"Dimension of B : {np.shape(B)}")

det=np.linalg.det(A)   # we will gwt a non-zero det , no matter if its negative or postive
print(f"Determinant of A is : {det}")

soln=np.linalg.solve(A,B)
print(f"Solution : {soln}")

