import numpy as np

def one_hot(y, num_classes=None):
    """
    Convert integer labels y ∈ {0,...,K-1} into one-hot matrix of shape (N, K).
    """
    # Write code here
    N = len(y)
    y = np.array(y)
    if num_classes == None:
        K = np.max(y) + 1
        
    else:
        K = num_classes
    print(K)
    array = np.zeros((N, K))
    print(array)
    array[np.arange(N), y] = 1
    return array

y = [1,1,0]
num_classes = 4


print(one_hot(y, num_classes))