import numpy as np

def gini_impurity(y_left, y_right) -> float:
    # Code của em ở đây
    N = len(y_left) + len(y_right)
    if N == 0:
        return float(0)
    element_left, count_left = np.unique(y_left, return_counts=True)
    element_right, count_right = np.unique(y_right, return_counts=True)
    gini_left = 1 - np.sum((count_left  / len(y_left)) ** 2)
    gini_right = 1 - np.sum((count_right / len(y_right)) ** 2)
    gini_s = (len(y_left) / N) * gini_left + (len(y_right) / N) *gini_right
    return float (gini_s)
