import numpy as np
def log_transform(values):
    """
    Apply the log1p transformation to each value.
    """
    # Write code here
    # check = lambda x: return None if x < 0 
    # check_vec = np.vectorize(check)

    # check_vec(values)
    
    values = np.array(values)
    y = np.log(1 + values)
    
    y = y.tolist()
    return y