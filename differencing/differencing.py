import numpy as np
def differencing(series, order):
    """
    Apply d-th order differencing to the time series.
    """
    result = series
    for i in range(order):
        a = np.array(result[1:])
        b = np.array(result[:-1])
        result = (a - b).tolist()
        
        print(result)
        
    return result
print(differencing([1,3,6,10,15],1))