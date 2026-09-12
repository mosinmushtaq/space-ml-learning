import numpy as np 

## Now using an example of a singular matrix having det =0

A=np.array([[1,1,1],
           [0,1,-3],
           [2,1,5]], dtype=np.dtype(float))

B=np.array([2,1,0])
print(f"A = \n{A}")

det=np.linalg.det(A)

print(f"Determinant of A is : {det}")

if (det==0):
    print("Matrix A is singular, no unique solution exists.")
else:
    print(f"Solution of A is : {np.linalg.solve(A,B)}")

# if the matrix is singular it will throw a error no matter what 
