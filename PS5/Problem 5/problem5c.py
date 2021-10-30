"""
Problem 5 c)
--------------
Must pick a non-integer value of k. 
Write the DFT of a non-integer sine wave.
"""

import numpy as np
from matplotlib import pyplot as plt

def analytic(N,k):
    
    kprime=np.arange(N)
    
    num1=1-np.exp(-2J*np.pi*(kprime-k))
    num2=1-np.exp(-2J*np.pi*(kprime+k))
    
    denom1=1-np.exp((-2J*np.pi*(kprime-k))/N)
    denom2=1-np.exp((-2J*np.pi*(kprime+k))/N)
    
    dft=-0.5*1J*((num1/denom1)-(num2/denom2))
    
    return dft

N=1000
x=np.arange(N)
k=20.34

ana_dft=analytic(N,k)
f=np.sin(2*np.pi*x*k/N)
f_dft=np.fft.fft(f)

plt.plot(ana_dft,'.')
plt.plot(f_dft,'*')

error=np.mean(np.abs(ana_dft-f_dft))

print(error)
