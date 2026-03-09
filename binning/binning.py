import numpy as np
def binning(values, num_bins):
    """
    Assign each value to an equal-width bin.
    """
    # Write code here4
    element = np.unique(values)
    print(element)
    if len(element) == 1 and len(values)!= 1:
        return np.zeros((num_bins,)).astype(int).tolist()
    elif len(element) == 1 and len(values) ==1:
        return np.zeros((1,)).astype(int).tolist()
    
    values = np.array(values)

    min_v = min(values)
    max_v = max(values)

    w = (max_v - min_v)/num_bins
    bin = np.minimum(np.floor((values - min_v)/w), num_bins -1)
    return bin.astype(int).tolist()
    
values = [5,5,5]
num_bins = 3 
print(binning(values, num_bins))
