import numpy as np

def _entropy(y):
    """
    Helper: Compute Shannon entropy (base 2) for labels y.
    """
    y = np.asarray(y)
    if y.size == 0:
        return 0.0
    vals, counts = np.unique(y, return_counts=True)
    p = counts / counts.sum()
    p = p[p > 0]
    return float(-(p * np.log2(p)).sum()) if p.size else 0.0

def information_gain(y, split_mask):
    """
    Compute Information Gain of a binary split on labels y.
    Use the _entropy() helper above.
    """
    # Write code here
    N = len(y)
    if N == 0:
        return 0
    
    y = np.array(y)
    split_mask = np.array(split_mask)
    #step 1: tinh entropy cu y
    h_y = _entropy(y)
    #step 2: tinh entropy cua L va R
    element, counts = np.unique(split_mask, return_counts = True)
    if len(element) == 1:
        return 0.0
    N_R = counts[0]
    N_L = counts[1]
    y_L = y[split_mask]
    y_R = y[~split_mask]
    h_y_L = _entropy(y_L)
    h_y_R = _entropy(y_R)
    #step 3: tinh IG
    ig = h_y - ((N_L/N) * h_y_L +(N_R/N) * h_y_R)
    return ig
y = [0,0,1,1]
