import numpy as np

def nesterov_momentum_step(w, v, grad, lr=0.01, momentum=0.9):
    """
    Perform one Nesterov Momentum update step.
    """
    # Write code here
    if len(w) == len(v) == len (grad) and 0 <= momentum < 1 and lr > 0:
        w = np.array(w)
        v = np.array(v)
        grad = np.array(grad)
    
        w1 = w - momentum * v
    
        v = momentum * v + lr * grad 
        
    
        w = w - v
        
        return (w, v)