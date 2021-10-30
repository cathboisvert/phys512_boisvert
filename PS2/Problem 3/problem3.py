"""
Problem 3
-------------
This question requires us to write a routine that takes
the correlation function of a gaussian (shifted by an arbitrary
amount with itself). 
"""
import numpy as np
from matplotlib import pyplot as plt

def corr_shift(f,shift):
    
    shifted=gauss_shift(f,shift)
    correlation=corr(shifted,f)
    
    return correlation

f=y #this is the same y as stated in previous question
shift1=0.9*np.size(x)
shift2=0.5*np.size(x)
shift3=0.1*np.size(x)
shift4=0.7827635*np.size(x)

shifted1=corr_shift(f,shift1)
shifted2=corr_shift(f,shift2)
shifted3=corr_shift(f,shift3)
shifted4=corr_shift(f,shift4)

#plt.plot(x,f)
plt.plot(shifted1)
plt.plot(shifted2)
plt.plot(shifted3)
plt.plot(shifted4)

