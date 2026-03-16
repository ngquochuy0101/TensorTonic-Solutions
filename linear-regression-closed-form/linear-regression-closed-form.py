import numpy as np

def linear_regression_closed_form(X, y):
    """
    Compute the optimal weight vector using the normal equation.
    """
    # Write code here
    X = np.array(X)
    y = np.array(y)
    w = np.linalg.inv(X.T @ X) @ (X.T @ y)

    return w
X = [[1,1],[1,2],[1,3]]
y = [3,5,7]

print(linear_regression_closed_form(X,y))