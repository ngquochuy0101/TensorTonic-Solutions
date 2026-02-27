x = [100,-200]
y = [-100,200]
import numpy as np

def manhattan_distance(x, y):
    """
    Compute the Manhattan (L1) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    return float (sum(abs( np.array( x) - np.array(y) )))
print(manhattan_distance(x, y))