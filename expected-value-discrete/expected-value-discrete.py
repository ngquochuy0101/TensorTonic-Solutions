import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    if np.sum(p) != 1 :
        raise ValueError("Tổng các xác suất p phải bằng 1.") 
    x = np.array(x)
    p = np.array(p)
    return float(np.sum(x*p))
    
