import math
import numpy as np
def log_loss(y_true, y_pred, eps=1e-15):
    """
    Compute per-sample log loss.
    """
    # Write code here
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    p_hat = np.clip(y_pred, eps, 1- eps)
    l = -(y_true * np.log(p_hat) + (1 - y_true) * np.log(1 - p_hat))
    return l.tolist()
y_true = [1,0,1]
y_pred = [0.9,0.1,0.8]
print(log_loss(y_true, y_pred))