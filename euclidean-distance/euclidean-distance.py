x = [3,4]
y = [0,0]
import numpy as np

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    x = np.array(x)
    y = np.array(y)
    return float(np.sqrt(sum((( x - y ))**2)))
print(euclidean_distance(x,y))
