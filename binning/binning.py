import numpy as np
def binning(values, num_bins):
    """
    Assign each value to an equal-width bin.
    """
    # Write code here4
    values = np.array(values)
    min_v = np.min(values)
    max_v = np.max(values)
    if min_v == max_v:
        return np.zeros((len(values),)).astype(int).tolist()
    w = (max_v - min_v)/num_bins
    bin = np.minimum(np.floor((values - min_v)/w), num_bins -1)
    return bin.astype(int).tolist()
    
values = [5,5,5]
num_bins = 3 
print(binning(values, num_bins))
