import numpy as np

import numpy as np

def huber_loss(y_true, y_pred, delta=1.0):
    """
    Compute Huber Loss for regression.
    """
    # Write code here
    y_pred = np.array(y_pred)
    y_true = np.array(y_true)
    
    e = y_true - y_pred
    print(e)
    L = lambda x: 0.5 * x**2 if abs(x) <= delta else( delta * (abs(x) - 0.5 * delta))
    L = np.vectorize(L)    # print(np.mean([1.5, 2.5]))
    return np.mean(L(e))
    

        
y_true = [0,5]

y_pred = [ 2,8]

print(huber_loss(y_true, y_pred, delta=1.0))