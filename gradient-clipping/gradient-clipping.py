import numpy as np

def clip_gradients(g, max_norm):
    """
    Clip gradients using global norm clipping.
    """
    # Write code here
    g = np.array(g)

    if max_norm <= 0:
        return g
    # step 1: compute gradient norm
    grad_norm = np.sqrt(np.sum(g**2))
    # step 2: comput clipping gradient
    g_clip = np.where(grad_norm <= max_norm, g , g * (max_norm/grad_norm))
    return g_clip

g = [1,2,3]

max_norm = 2
print(clip_gradients(g, max_norm))