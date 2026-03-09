import numpy as np
def frequency_encoding(values):
    """
    Replace each value with its frequency proportion.
    """
    # Write code here
    emplement, counts = np.unique(values, return_counts = True)
    counts_dict = dict(zip(emplement,counts))

    out = [counts_dict[v]/len(values) for v in values]
    return out

values = ["cat","dog","cat","cat","dog"]
print(frequency_encoding(values))
