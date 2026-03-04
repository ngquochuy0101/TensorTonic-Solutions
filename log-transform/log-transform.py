import numpy as np
import numpy as np
def log_transform(values):
    """
    Apply the log1p transformation to each value.
    """
    

    return np.log1p(np.maximum(0,np.array(values))).tolist()
                    
values = [-1,1,2,3]
print(log_transform(values))