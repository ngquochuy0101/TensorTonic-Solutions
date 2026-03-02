import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    # Write code he
    n = len(x)
    x = np.array(x)
    mean = np.mean(x)

    s = ((1/(n-1)) * sum( (x - mean)**2 ))
    s = float(s)
    return (s, np.sqrt(s))