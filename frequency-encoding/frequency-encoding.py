import numpy as np
def frequency_encoding(values):
    """
    Replace each value with its frequency proportion.
    """
    # Write code here
    emplement,inverse, counts = np.unique(values,return_inverse = True, return_counts = True)
    out = counts[inverse]/len(values)
    
    return out.tolist()
    

values = ["cat","dog","cat","cat","dog"]

print(frequency_encoding(values))
