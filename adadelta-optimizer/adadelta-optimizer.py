import numpy as np

def adadelta_step(w, grad, E_grad_sq, E_update_sq, rho=0.9, eps=1e-6):
    """
    Perform one AdaDelta update step.
    """
    # Write code here
    w = np.array(w)
    grad = np.array(grad)
    E_grad_sq = np.array(E_grad_sq)
    E_update_sq = np.array(E_update_sq)

    #step 1: update squered gradient averge
    new_E_grad_sq = rho * E_grad_sq + (1 - rho) * grad**2
    #step 2: comput parameter update
    delta_w = (- np.sqrt(E_update_sq + eps)/np.sqrt(new_E_grad_sq + eps) )* grad
    #step 3: update squared update averge
    new_E_update_sq = rho * E_update_sq + (1 - rho) * delta_w**2
    #step 4: update parameters
    new_w = w + delta_w
    
    return (new_w, new_E_grad_sq, new_E_update_sq)