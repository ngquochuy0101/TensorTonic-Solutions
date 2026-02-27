a=[1,2,3]
b=[2,4,6]
import numpy as np
def norm(x, y):
    return float(np.linalg.norm(x)*np.linalg.norm(y))
def dot(a, b):
    return float ( sum ( np.array(a) * np.array(b)))
def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code 
    print(dot(a,b))
    print(norm(a,b))
    n = norm(a, b)
    if n == 0:
        return 0
    return float(dot(a,b)/norm(a,b))
    
    
print(cosine_similarity(a, b))

