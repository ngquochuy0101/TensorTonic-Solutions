import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    # y = np.array(y)
    _, count = np.unique(y, return_counts = True)
    p = count / len(y)
    s = sum (p * np.log2 (p) )
        
    
    return float(-s)
    
    