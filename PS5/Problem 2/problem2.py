"""
Problem 2
-------------
This question requires us to write a routine that
will take the correlation function of two arrays. 
"""
import numpy as np
from matplotlib import pyplot as plt

def corr(f,g):
    
    ft1=np.fft.fft(f)
    ft2=np.conjugate(np.fft.fft(g))
    
    correlation = np.real(np.fft.ifft(ft1*ft2))
    
    return correlation

x=np.arange(-5,10,0.1)

N=np.size(x)
shift=0.5*np.size(x)
center=x[int(shift)]

y=np.exp(-(x-center)**2/(1.5**2))

gauss_corr=corr(y,y)

plt.plot(y)
plt.plot(gauss_corr)
