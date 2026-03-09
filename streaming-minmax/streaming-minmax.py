def streaming_minmax_init(D):
    """
    Initialize state dict with min, max arrays of shape (D,).
    """
    # Write code here
    min_vals = np.full((D,), np.inf)
    max_vals = np.full((D,), -np.inf)
    dict_init = {"min": min_vals, "max": max_vals}

    return dict_init
def streaming_minmax_update(state, X_batch, eps=1e-8):
    
    
    batch_min = np.min(X_batch, axis=0)
    batch_max = np.max(X_batch, axis=0)
    
    state["min"] = np.minimum(state["min"], batch_min)
    state["max"] = np.maximum(state["max"], batch_max)
    
    x_scaled = (X_batch -  state["min"]) / (state["max"] - state["min"] + eps)
    return x_scaled