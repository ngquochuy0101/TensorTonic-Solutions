import numpy as np
from scipy.special import comb



def binomial_pmf_cdf(n, p, k):
    """
    Compute Binomial PMF and CDF.
    """

         
        
    pmf = float (comb(n, k) * p**k *( 1 - p)**(n - k))
    list_k = np.arange(0, k+1)
    cdf = float ( sum (comb(n, list_k)* p**list_k *( 1 - p)**(n - list_k) ) )
    
    
    
    return (pmf, cdf)