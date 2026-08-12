import numpy as np
#Singularity is no new concept. It is just a singular matrix or a non-singular matrix
# or we can say a singular equation or a non-singular equation or a system of equations. 
#Here is a thing: a matrix that is singular will not have a nonzero determinant and hence will have no real solutions. 

# Now, if an equation or a matrix repeats itself, as I have studied earlier,
#  then it is a redundant equation and is also singular. Therefore, there are infinite many solutions
#  or we can see that the lines coincide with each other. 

#Now, if the equations contradict each other, which means that they contradict each other and then have no real answers

A=np.array([[1,2,3],
           [4,5,6],
           [7,8,9]])
print(np.linalg.det(A)) # det is zero so no solving and therefore not real solutions

# Yes. If the matrix $A$ is singular, np.linalg.solve(A, b) will always throw an error, no matter what you put in the constant vector $b$.

b=np.array([3,4,5])
c=np.array([1,1,1])

result=np.linalg.solve(A, b)
print(result)

# # this prints the result flawlesly because the matrix is non-singular
# result2=np.linalg.solve(A,c)
# print(result2)