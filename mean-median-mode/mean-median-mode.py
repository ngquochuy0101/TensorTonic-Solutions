import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Write code here
    x = np.array(x)
    mean = float( np.mean(x))
    meidan = float( np.median(x))
    mode = float (Counter(x).most_common(1)[0][0])
    
    return (mean, meidan, mode)

    