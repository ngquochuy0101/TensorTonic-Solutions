import numpy as np

def kfold_split(N, k, shuffle=True, rng=None):
    """
    Returns: list of length k with tuples (train_idx, val_idx)
    """
    # Write code here

    if shuffle == True:
        if rng is not None:
            arr = rng.permutation(N)
        else:
            arr = np.random.permutation(N)
    else:
        arr = np.arange(N)
    arr_split = np.array_split(arr, k)
    result = []
    for i in range(k):
        val = arr_split[i]
        train = arr_split[:i] + arr_split[i+1:]
        concate = np.concatenate(train, axis = 0)
        result.append((concate, val))
    return result
