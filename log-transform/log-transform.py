import numpy as np
def log_transform(values):
    """
    Apply the log1p transformation to each value.
    """
    
    values = np.array(values)
    values = np.maximum(0, values)
    
    y = np.log(1 + values)
    
    y = y.tolist()
    return y