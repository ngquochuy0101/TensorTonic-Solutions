import numpy as np

def zscore_standardize(X, axis=0, eps=1e-12):
    """
    Standardize X: (X - mean)/std. If 2D and axis=0, per column.
    Return np.ndarray (float).
    """
    # Write code here
    X = np.array(X)
    mean_x = np.mean(X, axis = axis, keepdims = True)
    print(mean_x)
    std_x = np.std(X, axis = axis, keepdims = True)
    
    print(std_x)
    
    X = (X - mean_x)/(std_x + eps)

    return X
    
X = [[1,2],
[3,6]
,[5,10]]
zscore_standardize(X, axis=0, eps=1e-12)
