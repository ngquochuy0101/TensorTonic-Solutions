import numpy as np

def hinge_loss(y_true, y_score, margin=1.0, reduction="mean") -> float:
    """
    y_true: 1D array of {-1,+1}
    y_score: 1D array of real scores, same shape as y_true
    reduction: "mean" or "sum"
    Return: float
    """
    n = len(y_true)
    y_true = np.array(y_true)
    y_score = np.array(y_score)
    mul = margin - y_true * y_score
    l = np.maximum (0, mul)
    print(l)
    # Write code here
    if reduction == "mean":
        return float( sum(l)/n)
    else:
        return float(sum( l))
        
y_true = [ 1, 1, -1]
y_score = [ 2, 0, 0]

hinge_loss(y_true, y_score, margin=1.0, reduction="mean")