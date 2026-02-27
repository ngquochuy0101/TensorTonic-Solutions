v = [3, 5]
import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    # Write code here
    n = len(v)
    arr = np.zeros((n,n), dtype="float")
    arr.tolist()
    for i in range(n):
        arr[i][i]=v[i]
    return np.array(arr)
print(make_diagonal(v))