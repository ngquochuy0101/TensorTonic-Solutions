import numpy as np

def impute_missing(X, strategy='mean'):
    """
    Fill NaN values in each feature column using column mean or median.
    """
    # Write code here
    X = np.array(X).astype(float)
    if strategy == "mean":
        values = np.nanmean(X, axis = 0, keepdims = True)
    else:
        values = np.nanmedian(X, axis = 0,keepdims = True)
    values = np.nan_to_num(values, 0)
    is_nan = np.isnan(X)
    output = np.where(is_nan,values, X )
    return output
    
X = [1,"nan",3,"nan",5]
print(impute_missing(X, strategy='mean'))