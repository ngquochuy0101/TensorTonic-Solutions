import numpy as np
import math

def percentiles(x, p):
    """
    Compute percentiles using linear interpolation.
    """
    # Write code here
    n = len (x)
    x = np.array(x)
    p = np.array(p)
    x = np.sort(x)
    
    index = (p/100) * (n - 1)

    low = np.floor(index).astype(int)
    high = np.ceil(index).astype(int)
    fration = index - low

    result = x[low] + (x[high] - x[low])*fration

    return result

