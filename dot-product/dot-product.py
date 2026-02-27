
import numpy as np

def dot_product(x, y):
    """
    Compute the dot product of two 1D arrays x and y.
    Must return a float.
    """
    # Write code here
    x = np.array(x)
    y = np.array(y)
    return float ( sum ( np.array(x) * np.array(y)))
    
x = [1,2,3]
y = [4,5,6]
print(dot_product(x,y))
