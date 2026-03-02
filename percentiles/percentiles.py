import numpy as np
import math

def percentiles(x, p):
    """
    Compute percentiles using linear interpolation.
    """
    # Write code here
    n = len(x)
    x = np.array(x)
    x = np.sort(x)
    p = np.array(p)
    
    index = p/100 * (n-1)
    low = np.floor(index).astype(int)
    high = np.ceil(index).astype(int)
    fraction = index - low
    
    result = x[low] + (x[high] - x[low]) * fraction
    return result
    
x = [4,1,3,2]
q =[25,75]
print(percentiles(x,q))
