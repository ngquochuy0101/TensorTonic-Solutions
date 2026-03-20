import numpy as np

def focal_loss(p, y, gamma=2.0):
    """
    Compute Focal Loss for binary classification.
    """
    # Write code 
    p = np.array(p)
    y = np.array(y)
    fl = - (1 - p)**gamma * y * np.log(p) - p**gamma *(1 - y) * np.log(1 - p)
    
    return np.mean(fl)
p = [0.9,0.2,0.7,0.1]
y= [1,0,1,0]
gamma = 2
print(focal_loss(p, y, gamma))