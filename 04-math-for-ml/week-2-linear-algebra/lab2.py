import numpy as np


#reducing rows



A=np.array([[2,6,1],
                [-3,0,5,],
                [5,4,-7]], dtype=np.float64)
B=np.array([4,8,6], dtype=np.float64 )

Matrix=np.hstack((A,B.reshape(3,1)))

def MultiplyRow(Matrix, row_num, row_multiple):
    Matrix_new=Matrix.copy()
    Matrix_new[row_num]=Matrix_new[row_num] * row_multiple
    return Matrix_new



result=MultiplyRow(Matrix, 0, 2)
print(result)
