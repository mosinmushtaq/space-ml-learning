import numpy as np

# so in order to solve a system of linear ewuations we have a funtion
    # the function is np.linalg.solve(A,B) which takes two inputs

# A here is the coefficients of x1 and x2 and x3 and so on or a and b and c  so on
# b here is the result of these equations i.e after the =
                         # This The function works only on square matrices. That is, if the number of equations is 4, the number of variables should also be 4. That is, the system should be complete, non-redundant, and non-contradictory. 
# e.g -1a + 3b = 7
#      3a + 2b = 1

# here A will be a matrix like [[-1, 3],
#                                [3, 2]]

# and B will be a 1d array of the constants i.e [7,1]

# this function will return an array of the resultant values of the variables as [x1,x2,x3]

A=np.array([[-1, 3],
             [3, 2]], dtype=np.int32)

B=np.array([7, 1], dtype=np.int32)


solved=np.linalg.solve(A,B)
print(solved)

print(f"x1 is : {solved[0]}")
print(f"x2 is : {solved[1]}")