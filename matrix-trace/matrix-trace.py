import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    # Write code here
    s = 0
    for i in range(len(A)):
        s += A[i][i]
    return s
A=[[2, -1, 0], [3, 5, 1], [0, 2, -2]]
print(matrix_trace(A))