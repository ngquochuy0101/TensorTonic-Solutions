import numpy as np

def rank_transform(values):
    """
    Replace each value with its average rank.
    """
    # Write code here
    em, inverse, counts = np.unique(values, return_inverse = True, return_counts = True)
    idx = np.cumsum(counts)-counts
    uniques_rank = idx + (counts - 1)/2
    values = uniques_rank[inverse] + 1
    return values.tolist()

values = [1,2,2,3]
print(rank_transform(values))
