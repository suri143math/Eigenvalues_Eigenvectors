import numpy as np
from scipy.linalg import det

def determinant():
    A=np.array([[1,2,3],[4,3,6],[2,1,4]])
    val=det(A)
    print(val)


determinant()
