import numpy as np


def list_mean(L):
    """evaluates the mean of a list"""
    if L is None:
        return None
    if len(L) == 0:
        return None
    
    s = 0
    
    for l in L:
        try:
            s += l
        except Exception:
            raise ValueError('Unsupported value in list')
        
    return s/len(L)

def list_stdev(L):
    """evaluates the standard deviation of a list"""
    if L is None:
        return None
    if len(L) == 0:
        return None

    s = 0
    
    for l in L:
        try:
            s += l
        except Exception:
            raise ValueError('Unsupported value in list')
        
    mean = s/len(L)
    
    sd = 0
    for num in L:
        sd += (num-mean)**2
    sd = np.sqrt(sd/(len(L)-1))
    
    return sd