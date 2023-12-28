import numpy as np
from scipy.linalg import solve

def solve_system():
    A=np.array([[1,2,3],[4,3,6],[2,1,4]])
    b=np.array([4,5,6])
    x = solve(A, b)
    print(x)


solve_system()
