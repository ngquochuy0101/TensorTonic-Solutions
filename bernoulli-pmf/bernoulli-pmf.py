import numpy as np

def bernoulli_pmf_and_moments(x, p):
    """
    Compute Bernoulli PMF and distribution moments.
    """
    # Write code here
    P = lambda x:  p if x == 1 else  1 - p
    P = np.vectorize(P)
    x = np.array(x)
    pmf = P(x)
    mean = p
    var = p * (1 - p)
    return (pmf, mean, var)
x=[0, 1, 1]
p=0.3
print(bernoulli_pmf_and_moments(x, p))
