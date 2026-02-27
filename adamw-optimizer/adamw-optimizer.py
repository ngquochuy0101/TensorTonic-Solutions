w=[1.0, -2.0]
m=[0.0, 0.0]
v=[0.0, 0.0]
grad=[0.3, -0.7]
lr=0.01
weight_decay=0.1
import numpy as np

def adamw_step(w, m, v, grad, lr=0.001, beta1=0.9, beta2=0.999, weight_decay=0.01, eps=1e-8):
    """
    Perform one AdamW update step.
    """
    # Write code here
    w = np.array(w)
    m = np.array(m)
    v = np.array(v)
    grad = np.array(grad)
    
    m = beta1 * m + (1 - beta1)* grad
    v = beta2 * v + (1 - beta2)* grad**2

    w = w - lr * (weight_decay * w) - lr * (m/(np.sqrt( v )+eps))
    return w ,m,v
    
    
print(adamw_step(w, m, v, grad, lr=0.001, beta1=0.9, beta2=0.999, weight_decay=0.01, eps=1e-8))