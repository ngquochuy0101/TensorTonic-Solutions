import numpy as np
from scipy import stats
def random_forest_vote(predictions):
    """
    Compute the majority vote from multiple tree predictions.
    """
    # Write code here
    mode, count = stats.mode(predictions)
    return mode.tolist()