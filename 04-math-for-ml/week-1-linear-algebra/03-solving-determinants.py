import numpy as np 

#Just like solving the value of x1 and x2 through Python NumPy, we can also calculate the determinant of a matrix. 

#That can be done only on the square matrices, as only the square matrices have a determinant. 
#If the determinant is equal to zero, then there is no solution that is unique to the system, or we can see the system is singular and either contradictory or redundant. Therefore, there are no unique solutions to the system. 
#If the determinant is not equal to zero, then there is a unique solution to the system. The system is complete and it is non-singular. 


# the funxtion to determine the determinant is np.linalg.det(A) where A is a square matrix

A=np.array([[-1, 3],
             [3, 2]])

d=np.linalg.det(A)

print(f"The determinant of the matrix is: {d:.2f}")
print(f"Is the determinant zero? {d == 0}")