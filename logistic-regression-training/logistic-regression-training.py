import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """
    # Write code here
    b = 0.0
    N = len(y)
    X = np.array(X)
    y = np.array(y)
    w = np.zeros((X.shape[1],))

    for i in range(steps):
        #step 1: forward 
        y_hat = _sigmoid(X @ w+ b)
        #step 2: loss
        loss = (-1/N) * sum(y * np.log(y_hat) + (1 - y) * np.log(1 - y_hat))
        #step 3: gradients
        grad_w = X.T @ (y_hat - y) / N
        grad_b = np.mean(y_hat - y)
        # step 4: update
        w = w - lr * grad_w
        b = b - lr * grad_b
    return (w, b)
X = [[0],[1],[2],[3]]
y = [0,0,1,1]
lr = 0.1
steps = 10
print(train_logistic_regression(X, y, lr, steps))